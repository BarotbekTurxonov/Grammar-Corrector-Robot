import requests
r = requests.get('https://live.api.mohirdev.uz/v1/users/register')
print(r.status_code)