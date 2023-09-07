import requests

payload = {'key1': 'value1', 'key2': 'value2'}

# r = requests.get('https://httpbin.org/get', params=payload)
# r = requests.post('https://httpbin.org/post', data=payload)
# r = requests.put('https://httpbin.org/put', data=payload)
r = requests.delete('https://httpbin.org/delete', data=payload)

print(r.status_code)
print(r.text)
print(r.json())