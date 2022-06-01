import http.client, urllib.parse
import json
import socket

socket.getaddrinfo('127.0.0.1', 8080)

subscriptionKey = 'ENTER YOUR KEY HERE'
host = 'F6311E470BB6F937F9F695196552682B'
path = '/v7.0/search'
mkt = 'en-US'
query = 'italian restaurants near me'

params = '?mkt=' + mkt + '&q=' + urllib.parse.quote (query)



def get_suggestions ():
 headers = {'Ocp-Apim-Subscription-Key': subscriptionKey}
 conn = http.client.HTTPSConnection (host)
 conn.request("GET", path + params, None, headers)
 response = conn.getresponse ()
 return response.read()


result = get_suggestions ()
print (json.dumps(json.loads(result), indent=4))