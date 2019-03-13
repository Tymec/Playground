import requests

URL = "http://detectportal.firefox.com/success.txt"

login_data = {
  'user.username': 'xxx',
  'user.password': 'xxx'
}

response = requests.post(URL, data=login_data)
