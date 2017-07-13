import urllib2
request = urllib2.Request("http://www.surfline.com")
response = urllib2.urlopen(request)
payload = response.read()
print(payload)
