# Quickstart

## Dependencies

This module requires API key to function. You may sign up for a free API key at <https://www.ip2location.io/pricing>.

## Installation

Use the following command to install the module:
```Bash
pip install ip2location-io
```

## Sample Codes

### Lookup IP Address Geolocation Data

You can make a geolocation data lookup for an IP address as below:

``` python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
ipgeolocation = ip2locationio.IPGeolocation(configuration)

# Lookup ip address geolocation data
print(ipgeolocation.lookup('8.8.8.8', 'en')) # The language parameter is only available for Plus and Security plan only.
```

### Lookup Domain Information

You can lookup domain information as below:

```python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Lookup domain information
print(domainwhois.lookup('example.com'))
```

### Convert Normal Text to Punycode

You can convert an international domain name to Punycode as below:

```python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Convert normal text to punycode
print(domainwhois.getpunycode('täst.de'))
```

### Convert Punycode to Normal Text

You can convert a Punycode to international domain name as below:

```python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Convert punycode to normal text
print(domainwhois.getnormaltext('xn--tst-qla.de'))
```

### Get Domain Name

You can extract the domain name from an url as below:

```python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Get domain name from URL
print(domainwhois.getdomainname('https://www.example.com/exe'))
```

### Get Domain Extension

You can extract the domain extension from a domain name or url as below:

```python
import ip2locationio

# Configures IP2Location.io API key
configuration = ip2locationio.Configuration('YOUR_API_KEY')
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Get domain extension (gTLD or ccTLD) from URL or domain name
print(domainwhois.getdomainextension('example.com'))
```