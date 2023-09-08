import requests

# r = requests.post(
#     'http://0.0.0.0:8000/post', data={'username': 'mike'}
# )

r = requests.get(
    'http://0.0.0.0:8000/employee/mike'
)
r = requests.post(
    'http://0.0.0.0:8000/employee', data={'name': 'mike'}
)
r = requests.put(
    'http://0.0.0.0:8000/employee', data={'name': 'mike', 'new_name': 'mike2'}
)
r = requests.delete(
    'http://0.0.0.0:8000/employee', data={'name': 'mike'}
)
print(r.text)