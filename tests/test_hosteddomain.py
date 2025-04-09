# -*- coding: utf-8 -*-

import pytest

import ip2locationio

def testinvalidapikey(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    hosteddomain = ip2locationio.HostedDomain(configuration)
    try:
        result = hosteddomain.lookup('8.8.8.8')
    except IP2LocationIOAPIError as e:
        assert str(e) == 'Invalid API key or insufficient credit.'

def testfunctionexist(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    hosteddomain = ip2locationio.HostedDomain(configuration)
    functions_list = ['lookup']
    for x in range(len(functions_list)): 
        assert hasattr(hosteddomain, functions_list[x]) == True, "Function did not exist."

# def testlookup(global_data):
    # configuration = ip2locationio.Configuration(global_data["apikey"])
    # hosteddomain = ip2locationio.HostedDomain(configuration)
    # result = hosteddomain.lookup('8.8.8.8')
    # assert result['country_code'] == "US", "Test failed because country code not same."
        
