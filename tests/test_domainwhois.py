# -*- coding: utf-8 -*-

import pytest

import ip2locationio

def testfunctionexist(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    domainwhois = ip2locationio.DomainWHOIS(configuration)
    errors = []
    functions_list = ['lookup', 'getpunycode', 'getnormaltext', 'getdomainname', 'getdomainextension']
    for x in range(len(functions_list)): 
        # assert hasattr(mbv, functions_list[x]) == True, "Function did not exist."
        if (hasattr(domainwhois, functions_list[x]) is False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def test_get_puny_code(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    domainwhois = ip2locationio.DomainWHOIS(configuration)
    result = domainwhois.getpunycode('täst.de')
    assert result == "xn--tst-qla.de"

def test_get_normal_text(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    domainwhois = ip2locationio.DomainWHOIS(configuration)
    result = domainwhois.getnormaltext('xn--tst-qla.de')
    assert result == "täst.de"

def test_get_domain_name(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    domainwhois = ip2locationio.DomainWHOIS(configuration)
    result = domainwhois.getdomainname('https://www.example.com/exe')
    assert result == "example.com"

def test_get_domain_extension(global_data):
    configuration = ip2locationio.Configuration(global_data["apikey"])
    domainwhois = ip2locationio.DomainWHOIS(configuration)
    result = domainwhois.getdomainextension('https://www.example.com/exe')
    assert result == ".com"