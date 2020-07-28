#!/usr/bin/env python3

import ovh
import os
import json

client = ovh.Client(
    endpoint=os.environ['OVH_EP'],
    application_key=os.environ['OVH_AK'],
    application_secret=os.environ['OVH_AS'],
    consumer_key=os.environ['OVH_CK'],
)

print("Welcome", client.get('/me')['firstname'],client.get('/me')['name'])
print("Email:", client.get('/me')['email'])
bill_list = client.get('/me/bill')
for bill in bill_list:
    details = client.get('/me/bill/%s' % bill)
    print("%12s (%s): %10s --> %s" % (
        bill,
        details['date'],
        details['priceWithTax']['text'],
        details['pdfUrl'],
    ))

vps_list = client.get('/vps')
for vps in vps_list:
    details = client.get('/vps/%s' % vps)
    print(json.dumps(details, indent=4))
    result = client.post('/vps/%s/reboot' % vps)
    print(json.dumps(result, indent=4))