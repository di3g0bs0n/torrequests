#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017 Diego Fernandez <di3g0bson@gmail.com>.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#


import requests, requesocks, json, socket


class Tor(object):

	def __init__(self, tor_ip = '127.0.0.1', tor_port = 9150, cookies = {}, headers = {}, auth=None, verify=False):
		if not self.__ping(tor_ip, tor_port):
			raise Exception("Tor is not detected on %s:%s" % (tor_ip, tor_port))
		self.session = requesocks.session()
		self.session.proxies = {
		    'http': 'socks5://%s:%s' % (tor_ip, tor_port),
		    'https': 'socks5://%s:%s' % (tor_ip, tor_port)
		}
		self.cookies = cookies
		self.headers = headers
		self.auth = auth
		self.session.verify = verify

	def __ping(self, ip, port):
		"""Checks the connectivity of an IP and a port."""
		try:
			s = socket.create_connection((ip, port), 2)
			return True
		except:
			return False

	def __intersect(self, base, item):
		"""Joins two items with the same type, usually dict."""
		if item is None:
			return base
		if base is None:
			return item
			
		if type(base) != type(item):
			raise Exception("Incompatible types")
		elif type(base) is dict:
			r = base
			if type(item) is dict:
				for k in item.keys():
					r[k] = item[k]
			return base

	def getPublicIP(self):
		"""Gets the public IP from the Internet connection."""
		try:
			url = 'http://httpbin.org/ip'
			r = self.get(url)
			return json.loads(r.text)['origin']
		except Exception as e:
			print "[!] %s" % e
			return -1

	def get(self, url, data = None, files = None, cookies = None, headers = None, auth = None):
		"""Make a GET request"""
		_cookies = self.__intersect(self.cookies, cookies)
		_headers = self.__intersect(self.headers, headers)
		_auth = auth if auth is not None else self.auth
		return self.session.get(url=url, data=data, files=files, cookies=_cookies, headers=_headers, auth=auth)

	def post(self, url, data = None, files = None, cookies = None, headers = None, auth = None):
		"""Make a POST request"""
		_cookies = self.__intersect(self.cookies, cookies)
		_headers = self.__intersect(self.headers, headers)
		_auth = auth if auth is not None else self.auth
		return self.session.post(url=url, data=data, files=files, cookies=_cookies, headers=_headers, auth=auth)


