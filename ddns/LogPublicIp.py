#!/usr/bin/env python

from datetime import datetime
import os
import requests

LOG = 'ip.log'
URL = 'https://ipinfo.io/ip'

try:
    print('{} getting ip from {}'.format(datetime.now(), URL))
    r = requests.get(URL, timeout=10)
    print('{} response {}'.format(datetime.now(), r.status_code))
    if r.status_code == 200:
        ip = r.content.decode('ascii').rstrip('\n')
        last_ip = None
        if os.path.exists(LOG):
            f = open(LOG, 'r')
            last_ip = f.readlines()[-1].split()[-1]
            f.close()

        if ip != last_ip:
            f = open(LOG, 'a+')
            f.write("{} {}\n".format(datetime.now(), ip))
        
        print('{} ip:{} lastip:{}'.format(datetime.now(), ip, last_ip))
    else:   
        msg="{} {} {}\n".format(datetime.now(), r.status_code, r.reason)
        print(msg)
        f = open(LOG, 'a+')
        f.write(msg)
except Exception as inst:
        msg="{} No connection {} {}\n".format(datetime.now(), type(inst), inst.args)
        print(msg)
        f = open(LOG, 'r')
        if 'No connection' not in (f.readlines()[-1]):
            f = open(LOG, 'a+')
            f.write(msg)
