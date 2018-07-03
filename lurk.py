#!/usr/bin/env python
import optparse
import requests
import os

def exists(path):
    r = requests.head(path)
    results = requests.codes.ok

    if (r.status_code == requests.codes.ok):
        print('[+]File Discovered: %s' % path)

def scan(url):
    for root, dirs, files in os.walk("patterns"):  
        for filename in files:
            with open("patterns/"+filename) as f:
                file = f.read().splitlines()
                
            for f in file:
                exists(url+"/"+f)

def run():
    parser = optparse.OptionParser('usage -u <target host>')
    parser.add_option('-u', dest='url', type='string', help='specify target host')
    (options, args) = parser.parse_args()
    url = options.url
    if (url == None):
        print('[-] Usage: -u https://www.enigmagroup.org')
        exit(0)
    scan(url)
    print "DONE"

if __name__ == '__main__':
    run()