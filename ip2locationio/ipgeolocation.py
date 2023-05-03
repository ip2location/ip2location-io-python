import socket
from ip2locationio.common import urlencode, httprequest, is_valid_ip

# Windows version of Python does not provide it
# for compatibility with older versions of Windows.
if not hasattr(socket, 'inet_pton'):
    def inet_pton(t, addr):
        import ctypes
        a = ctypes.WinDLL('ws2_32.dll')
        in_addr_p = ctypes.create_string_buffer(b(addr))
        if t == socket.AF_INET:
            out_addr_p = ctypes.create_string_buffer(4)
        elif t == socket.AF_INET6:
            out_addr_p = ctypes.create_string_buffer(16)
        n = a.inet_pton(t, in_addr_p, out_addr_p)
        if n == 0:
            raise ValueError('Invalid address')
        return out_addr_p.raw
    socket.inet_pton = inet_pton

class IPGeolocation:

    def __init__(self,configuration):
        # print('apikey: ' + configuration.getapikey())
        self.apikey = configuration.getapikey()
        self.moduleversion = configuration.getmoduleversion()
    
    def lookup(self,ip,language=''):
        '''This function will look the given IP address up in IP2Location web service.'''
        parameters = urlencode((("key", self.apikey), ("ip", ip), ("format", "json"), ("lang", language), ("source", "sdk-python-iplio"), ("source_version", self.moduleversion)))
        response = httprequest("api.ip2location.io", "/?", parameters)
        if (response == None):
            # return False
            raise IP2LocationIOAPIError('IPGeolocation lookup error.')
        if ('error' in response):
        # if (('response' in response) and (response['response'] != 'OK')):
            raise IP2LocationIOAPIError(response['error']['error_message'])
            # return(response['response'])
        return response
  
class IP2LocationIOAPIError(Exception):
    """Raise for IP2Location API Error Message"""