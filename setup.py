import setuptools

with open("README.md", "r") as fh:
	long_description = fh.read()

setuptools.setup(
	name="ip2locationio",
	version="1.0.0", 
	author="IP2Location",
	author_email="support@ip2location.com",
	description="IP2Location.io Python SDK to get geolocation info from IPv4 and IPv6 address.",
	long_description=long_description,
	long_description_content_type="text/markdown",
	py_modules=['ip2locationio'],
	url="https://github.com/ip2location/ip2location-io-python",
	packages=setuptools.find_packages(),
	tests_require=['pytest>=3.0.6'],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Programming Language :: Python :: 3.11",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
)
