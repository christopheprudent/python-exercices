import requests
url = 'http://www.example.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh) Gecko/20100101 Firefox/38.0'}
request = requests.get(url, headers=headers)
print("Web page status: ", request)
print("\nHTML code of the above web page:")
if request.ok:
    print(request.text)

