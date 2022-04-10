# web solution
import requests
r = requests.get('https://api.github.com/')
response = r.headers

print("Headers information of the said response:")
print(response)
print('set of keys...')
for k in response.keys():
    print(k)

print("\nVarious Key-value pairs information of the said resource and request:")

if 'date' in response:
    print("Date: ",r.headers['date'])
print("server: ",r.headers['server'])
print("cache-control: ",r.headers['cache-control'])
print("vary: ",r.headers['vary'])
print("x-github-media-type: ",r.headers['x-github-media-type'])
print("access-control-expose-headers: ",r.headers['access-control-expose-headers'])
print("strict-transport-security: ",r.headers['strict-transport-security'])
print("x-content-type-options: ",r.headers['x-content-type-options'])
print("x-xss-protection: ",r.headers['x-xss-protection'])
print("referrer-policy: ",r.headers['referrer-policy'])
print("content-security-policy: ",r.headers['content-security-policy'])
print("content-encoding: ",r.headers['content-encoding'])
print("X-Ratelimit-Remaining: ",r.headers['X-Ratelimit-Remaining'])
print("X-Ratelimit-Reset: ",r.headers['X-Ratelimit-Reset'])
print("X-Ratelimit-Used: ",r.headers['X-Ratelimit-Used'])
print("Accept-Ranges:",r.headers['Accept-Ranges'])
print("X-GitHub-Request-Id:",r.headers['X-GitHub-Request-Id'])

#error: no key 'status'
#print("status: ",r.headers['status'])
