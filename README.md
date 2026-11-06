# IP2Location.io Python SDK — IP Geolocation, Domain WHOIS & Hosted Domain Lookup

[![PyPI Version](https://img.shields.io/pypi/v/ip2location-io.svg)](https://pypi.org/project/ip2location-io/)
[![Python Versions](https://img.shields.io/pypi/pyversions/ip2location-io.svg)](https://pypi.org/project/ip2location-io/)

**IP2Location.io Python SDK** (`ip2location-io`) is a Python package for retrieving **IPv4 and IPv6 geolocation, network and IP intelligence data** through the [IP2Location.io API](https://www.ip2location.io/). It also provides **domain WHOIS lookup** and **hosted domain lookup**, along with helpers for internationalized domain names. Integrate IP and domain intelligence into Python applications, scripts and data-processing workflows without manually constructing API requests.

**Quick links:** [Get an API key](https://www.ip2location.io/pricing) · [Developer documentation](https://ip2location-io-python.readthedocs.io/en/latest/index.html) · [API reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html) · [PyPI package](https://pypi.org/project/ip2location-io/)

## Features

- **IPv4 and IPv6 geolocation:** Retrieve available country, region, district, city, ZIP/postal code, latitude, longitude and time zone.
- **Network and ASN information:** Access ASN, AS name, ISP, associated domain, connection speed and usage type where available.
- **Time zone and localization data:** Access time zone information, including available daylight saving time data, and request translated location names on Plus and Security plans.
- **Proxy and threat-related signals:** Access available proxy, VPN, Tor, data center, crawler and other security indicators, along with fraud score where supported by the plan.
- **Additional IP intelligence:** Retrieve available mobile carrier information (MCC/MNC), country metadata, advertising category, elevation and related attributes.
- **Domain WHOIS lookup:** Retrieve available domain registration records, such as registrar, creation/expiration dates, domain status, nameservers and contact information.
- **Internationalized domain and URL utilities:** Convert domain names to and from Punycode, extract domain names from URLs and obtain domain extensions.
- **Hosted domains:** Retrieve domains hosted on an IPv4 or IPv6 address, including paginated results.

> **Plan availability:** Attributes and security indicators vary by API plan and IP address. Optional fields may be absent or have no value. See the [pricing page](https://www.ip2location.io/pricing) and [Python API response field reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html).

## SDK classes

The [Python API reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html) documents four classes:

| Class | Description |
| --- | --- |
| [`Configuration`](https://ip2location-io-python.readthedocs.io/en/latest/code.html#configuration-class) | Stores the API key used by SDK clients. |
| [`IPGeolocation`](https://ip2location-io-python.readthedocs.io/en/latest/code.html#ipgeolocation-class) | Retrieves IPv4/IPv6 geolocation and available network/security information. |
| [`DomainWHOIS`](https://ip2location-io-python.readthedocs.io/en/latest/code.html#domainwhois-class) | Retrieves domain WHOIS information and provides domain/Punycode utilities. |
| [`HostedDomain`](https://ip2location-io-python.readthedocs.io/en/latest/code.html#hosteddomain-class) | Retrieves domains hosted on an IP address, with optional pagination. |

## API access and query limits

IP2Location.io offers keyless IP geolocation queries through its REST API and a Free plan with an API key:

| API service | Keyless (no API key) | Free plan (with API key) |
| --- | --- | --- |
| IP Geolocation API | **1,000 queries/day** | **50,000 queries/month** |
| Domain WHOIS API | — | **500 queries/month** |
| Hosted Domain API | — | **50 queries/month** |

- **Keyless access:** No registration is required for limited direct [IP Geolocation REST API](https://www.ip2location.io/ip2location-documentation) requests. The daily allowance resets at **00:00 UTC**. The Python SDK examples below use an API key, as required by the official Python quickstart.
- **Free plan:** Register for an API key to use the published monthly allowances.
- **Attribution:** Keyless and Free-plan usage require attribution; follow the [pricing page](https://www.ip2location.io/pricing) for current requirements.
- **Paid plans:** See the [pricing page](https://www.ip2location.io/pricing) for higher quotas, supported attributes and current prices.

For authentication and rate-limiting details, see the [IP Geolocation API documentation](https://www.ip2location.io/ip2location-documentation).

## Requirements

- **Python 3:** The current package metadata lists Python **3.5 through 3.13** among its supported-version classifiers. For a new project, use a currently supported Python release compatible with your environment.
- **pip** for installing the published package (or a compatible Python package installer).
- Network access to the IP2Location.io services.
- An [IP2Location.io API key](https://www.ip2location.io/pricing) for SDK lookups (free signup available).

The SDK package is published on [PyPI](https://pypi.org/project/ip2location-io/); no local IP geolocation database download is required for API lookups.

## Installation

Install the package from PyPI, as described in the [official quickstart](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html):

```bash
python -m pip install ip2location-io
```

On systems where Python 3 is invoked as `python3`, use `python3 -m pip install ip2location-io` instead. The official documentation also shows `pip install ip2location-io`.

**Arch Linux (alternative documented installation):**

```bash
git clone https://aur.archlinux.org/ip2location-io-python.git
cd ip2location-io-python
makepkg -si
```

The Arch Linux procedure comes from the official Python quickstart. If you install through PyPI, the Arch Linux steps are unnecessary.

Set your API key as an environment variable rather than committing it to source code:

**Linux / macOS:**

```bash
export IP2LOCATION_API_KEY='YOUR_API_KEY'
```

**Windows Command Prompt:**

```bat
set IP2LOCATION_API_KEY=YOUR_API_KEY
```

**Windows PowerShell:**

```powershell
$env:IP2LOCATION_API_KEY = 'YOUR_API_KEY'
```

## Quickstart: IP geolocation lookup

Create a file named `lookup.py`:

```python
import os
import ip2locationio

api_key = os.environ.get('IP2LOCATION_API_KEY')
if not api_key:
    raise SystemExit('Set the IP2LOCATION_API_KEY environment variable.')

configuration = ip2locationio.Configuration(api_key)
ipgeolocation = ip2locationio.IPGeolocation(configuration)

# Look up an IPv4 address.
result = ipgeolocation.lookup('8.8.8.8')
print(result)
```

Run the script:

```bash
python lookup.py
```

The initialization and `lookup()` method follow the [official Python quickstart](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html). The environment-variable step is a practical adaptation to avoid hard-coding credentials. The contents of the returned response depend on your plan and the queried IP address. See the [geolocation field reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html#ipgeolocation-class).

## More usage examples

The examples below assume that you have imported `ip2locationio` and created `configuration` as shown in the quickstart. These use the same classes and method names as the official [sample codes](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html).

### Request translated location names

The optional second argument to `IPGeolocation.lookup(ip_address, language)` requests translation information for supported continent, country, region and city names. This option is available on **Plus and Security** plans.

```python
ipgeolocation = ip2locationio.IPGeolocation(configuration)
result = ipgeolocation.lookup('8.8.8.8', 'es')
print(result)
```

### Look up IPv6 geolocation

The geolocation API supports IPv6 addresses using the same lookup method:

```python
ipgeolocation = ip2locationio.IPGeolocation(configuration)
result = ipgeolocation.lookup('2001:4860:4860::8888')
print(result)
```

### Inspect available ASN and network information

**Additional example:** The API response documentation lists `asn`, `as` and `isp`, subject to plan availability. This example illustrates how to inspect these values without assuming they are always present.

```python
ipgeolocation = ip2locationio.IPGeolocation(configuration)
result = ipgeolocation.lookup('8.8.8.8')

print(result.get('asn', 'N/A'))
print(result.get('as', 'N/A'))
print(result.get('isp', 'N/A'))
```

### Inspect available proxy indicators

**Additional example:** The API reference documents top-level `is_proxy` and the optional `proxy` object, including `is_vpn` and `is_tor`. Some fields require higher-tier plans.

```python
ipgeolocation = ip2locationio.IPGeolocation(configuration)
result = ipgeolocation.lookup('8.8.8.8')

print('Proxy:', result.get('is_proxy', 'N/A'))
proxy = result.get('proxy') or {}
print('VPN:', proxy.get('is_vpn', 'N/A'))
print('Tor:', proxy.get('is_tor', 'N/A'))
```

### Look up domain WHOIS information

The official quickstart demonstrates `DomainWHOIS.lookup()` for retrieving available domain registration information:

```python
domainwhois = ip2locationio.DomainWHOIS(configuration)
result = domainwhois.lookup('example.com')
print(result)
```

WHOIS fields such as registrar details, nameservers and contact information may be unavailable or redacted. See the [DomainWHOIS API reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html#domainwhois-class).

### Use domain and Punycode utilities

The following four helper methods and input examples are documented in the official Python quickstart:

```python
domainwhois = ip2locationio.DomainWHOIS(configuration)

# Unicode domain name to Punycode.
print(domainwhois.getpunycode('täst.de'))

# Punycode back to a Unicode domain name.
print(domainwhois.getnormaltext('xn--tst-qla.de'))

# Extract the domain name from a URL.
print(domainwhois.getdomainname('https://www.example.com/exe'))

# Extract the domain extension.
print(domainwhois.getdomainextension('example.com'))
```

### Find domains hosted on an IP address

The [official hosted-domain example](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html) uses `HostedDomain.lookup()`:

```python
hosteddomain = ip2locationio.HostedDomain(configuration)
result = hosteddomain.lookup('8.8.8.8')
print(result)
```

The `lookup(ip_address, page)` method accepts an optional page number. The first page is used when no page is specified:

```python
result = hosteddomain.lookup('8.8.8.8', 2)
print(result)
```

The [API reference](https://ip2location-io-python.readthedocs.io/en/latest/code.html#hosteddomain-class) documents pagination fields including `total_domains`, `page`, `per_page`, `total_pages` and `domains`.

## Testing and troubleshooting

The official [Python SDK quickstart](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html) documents running the repository tests with `pytest`. After cloning the repository and preparing the test dependencies, set your API key and run:

```bash
export IP2LOCATION_API_KEY='YOUR_API_KEY'
pytest
```

Alternatively, the official instructions document providing the API key using `pytest --apikey YOUR_API_KEY`.

If a Python script reports `ModuleNotFoundError: No module named 'ip2locationio'`, check that the package was installed into the Python environment used to run your script:

```bash
python -m pip show ip2location-io
python -c "import ip2locationio; print(ip2locationio.__file__)"
```

If a lookup fails, verify the API key, network connection and applicable query quota. If optional fields are missing, check the API plan rather than assuming every response includes all attributes.

## Common use cases

- **Website and application localization:** Suggest relevant language, regional content or currency based on approximate IP location.
- **Traffic and log analysis:** Enrich visitor events, access logs and datasets with country and network context.
- **Security review:** Supplement other security signals with proxy, VPN, Tor or fraud indicators where supported, rather than using them as sole evidence of malicious activity.
- **Domain research:** Retrieve available WHOIS dates, registrar information, nameservers and domain metadata.
- **Network and hosting research:** Investigate ASN/ISP information and domains hosted on an IP address.
- **Python automation and data pipelines:** Integrate repeatable geolocation or hosted-domain lookups into scripts and analysis workflows while respecting API quotas.

## Documentation and support

- [Python SDK quickstart, installation and sample codes](https://ip2location-io-python.readthedocs.io/en/latest/quickstart.html)
- [Python SDK API reference and response fields](https://ip2location-io-python.readthedocs.io/en/latest/code.html)
- [Official GitHub repository](https://github.com/ip2location/ip2location-io-python)
- [Python package on PyPI](https://pypi.org/project/ip2location-io/)
- [IP2Location.io API plans and query limits](https://www.ip2location.io/pricing)
- [IP Geolocation API authentication and rate limits](https://www.ip2location.io/ip2location-documentation)
- [Report a Python SDK issue or request a feature](https://github.com/ip2location/ip2location-io-python/issues)
- [API and account support](https://www.ip2location.io/contact-us)

## License

Licensed under the **MIT License**. See [LICENSE.TXT](./LICENSE.TXT).
