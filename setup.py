from setuptools import find_packages, setup

setup(
    name='torrequests',
    version='1.1.5',
    author='Diego Fernandez',
    author_email='di3g0bs0n@gmail.com',
    description=('Wrapper for requests over Tor'),
    long_description='Wrapper of the requests library that allows to make requests through TOR.',
    license='GPLv3',
    keywords='tor requests',
    packages=find_packages(),
    url='https://github.com/di3g0bs0n/torrequests',
    install_requires=['requests==2.20.0','requesocks==0.10.8'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities'
    ]
)