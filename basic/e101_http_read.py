#from http.client import HTTPConnection
#conn = HTTPConnection("cadastre.data.gouv.fr/data/etalab-cadastre/")
#conn.request("GET", "/")  
#result = conn.getresponse()
## retrieves the entire contents.  
#contents = result.read() 
#print(contents)

import urllib3
http = urllib3.PoolManager()

response = http.request('GET', 'https://cadastre.data.gouv.fr/data/etalab-cadastre')

#print(response.data) # Raw data.
print(response.status) # Status code.
print(response.headers['Content-Type']) # Content type.
print(response.data.decode('utf-8')) # Text.
