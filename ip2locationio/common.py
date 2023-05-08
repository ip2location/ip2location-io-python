import sys
import socket
import json
import os
import urllib.parse, http.client


def urlencode(x):
    return urllib.parse.urlencode(x)
def httprequest(hostname, path, parameters):
    try:
        conn = http.client.HTTPSConnection(hostname)
        conn.request("GET", path + parameters)
        res = conn.getresponse()
        return json.loads(res.read())
    except:
        return None
def u(x):
    if isinstance(x, bytes):
        return x.decode()
    return x
def b(x):
    if isinstance(x, bytes):
        return x
    return x.encode('ascii')

def is_ipv4(ip):
    if '.' in ip:
        ip_parts = ip.split('.')
        if len(ip_parts) == 4:
            for i in range(0,len(ip_parts)):
                if str(ip_parts[i]).isdigit():
                    if int(ip_parts[i]) > 255:
                        return False
                else:
                    return False
            pattern = r'^([0-9]{1,3}[.]){3}[0-9]{1,3}$'
            if match(pattern, ip) is not None:
                return 4
        else:
            return False
    else:
        return False
    return False

def is_ipv6(hostname):
    if ':' in hostname:
        return 6
    return False

def is_valid_ip(hostname):
    if is_ipv4(hostname) is not False or is_ipv6(hostname) is not False:
        return True
    else:
        return False