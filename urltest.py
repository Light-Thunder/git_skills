#!/usr/bin/env python
#2015/09/28

import urllib2
url=raw_input("Enter URL:")
req=urllib2.Request(url)
response=urllib2.urlopen(req)
the_page=response.read()
print the_page
