#!/usr/bin/env python3

import ovh
import os

ENDPOINT='ovh-ca'


# Instantiate. Visit https://api.ovh.com/createToken/?GET=/me
# to get your credentials
client = ovh.Client(
    endpoint=ENDPOINT,
    application_key=os.environ['OVH_AK'],
    application_secret=os.environ['OVH_AS'],
    consumer_key=os.environ['OVH_CK'],
)

# Print nice welcome message
print("Welcome", client.get('/me')['firstname'],client.get('/me')['name'])
print("Email:", client.get('/me')['email'])
bills = client.get('/me/bill')
for bill in bills:
    details = client.get('/me/bill/%s' % bill)
    print("%12s (%s): %10s --> %s" % (
        bill,
        details['date'],
        details['priceWithTax']['text'],
        details['pdfUrl'],
    ))