# torRequests
Wrapper of the requests library that allows to make requests through TOR.

Author: Diego Fernandez


## Installation

```bash
pip install torrequests
```

## Usage

### Simple GET request (default Tor)

```python
from torrequests import Tor

# Default tor value: 127.0.0.1:9150
tor = Tor() 

r = tor.get('http://www.example.com')

if r.status_code == 200:
	print r.text

```

### Advanced POST request (custom Tor)

```python
from torrequests import Tor

tor = Tor(tor_ip='127.0.0.1', tor_port=9999, headers = {"User-Agent":"Mozilla/5.0 Gecko/20100101 Firefox/45.0"}) 

header = {
	"X-Custom-Header": "1"
}

cookie = {
	"SessionID": "123456789"
}

# Request is sended with both headers (User-Agent and X-Custom-Header), and a Cookie (SessionID)
r = tor.post('http://www.example.com', headers=header, cookies=cookie)

if r.status_code == 200:
	print r.text

```

### Check Public IP

```python
from torrequests import Tor

tor = Tor(tor_ip='127.0.0.1', tor_port=9999)

print getPublicIP()

```