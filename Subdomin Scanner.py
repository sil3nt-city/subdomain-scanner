#!/usr/bin/python
 
import urllib2
import cookielib
import sys
import time
import urllib2 
import sys
import os
import time
import httplib
import re
from socket import * 
from ipwhois import IPWhois
from pprint import pprint
import shutil 

 
domain = raw_input('Enter Your Domain: ')
domain = domain.lower()
print "\n|---------------------------------------------------------------|"
print "|     Start Subdomin Scanner                                      |"
print "|-----------------------------------------------------------------|\n"
print "\n[-] %s" % time.strftime("%X")          
print "[+] Target:",domain
siteIP = gethostbyname(domain)
print '[+] Target ip : ', siteIP
print "[+] Checking subDomains..."
print "[+] Code sil3nt-city"
print "[+] Email sil3nt.city@gmail.com"


def sub():
 
        try:
 
                cj = cookielib.CookieJar()
                coder = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
 
                agent = {'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:28.0) Gecko/20100101 Firefox/28.0'}
 
                url = "http://www.pagesinventory.com/search/?s="+domain
                su = urllib2.Request(url)
                conn = coder.open(su).read()
 
                find = re.findall('/domain/\S+', conn)
 
                for i, p in map(None,find,range(1,500)):
                        s = i.replace('/domain/',"sub => ").split('.html')[0]
                        print str(p)+ ". " + s
                        time.sleep(0.3)
 
        except Exception, e:
                pass
 
sub()
raw_input("press enter To Exit ")
