#!/usr/bin/env python3 
# 
# Pull current network data from Hitron CGN3 and CODA-4582
# Rogers Rocket CGN3 Modem, or Rogers Ignite Modem
#
# https://nko.gg/
# https://github.com/neko/

import requests

router_ip= "192.168.0.1"    # Your router's IP address
data = {
  'user': 'cusadmin',       # Admin username
  'pws': 'Password9',       # Default is your wifi password
}

with requests.Session() as se:
    se.post('http://192.168.0.1/goform/login', data=data)
    recv = se.get('http://192.168.0.1/data/getSysInfo.asp')
    sysInfo = recv.json()
    print(sysInfo[0]['hwVersion'])
    print(sysInfo[0]['swVersion'])
    print(sysInfo[0]['serialNumber'])
    print(sysInfo[0]['rfMac'])
    print(sysInfo[0]['priDNS'])
    print(sysInfo[0]['secDNS'])
    print(sysInfo[0]['systemLanUptime'])
    print(sysInfo[0]['systemWanUptime'])
    print(sysInfo[0]['systemTime'])
    print(sysInfo[0]['timezone'])
    print(sysInfo[0]['WRecPkt'])
    print(sysInfo[0]['WSendPkt'])
    print(sysInfo[0]['lanIp'])
    print(sysInfo[0]['LRecPkt'])
    print(sysInfo[0]['LSendPkt'])
    print(sysInfo[0]['routerMode'])
