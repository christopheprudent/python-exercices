# web solution
import requests
res = requests.get('https://google.com/')
print("Response of https://google.com/:")
print(res.status_code)
res = requests.get('https://amazon.com/')
print("Response of https://amazon.com/:")
print(res.status_code)
res = requests.get('https://w3resource.com/')
print("Response of https://w3resource.com/:")
print(res.status_code)
print("\nMethods and attributes available to objects on successful\nrequest of https://w3resource.com:\n")
print(dir(res)) 
