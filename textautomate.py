import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': 'xxxxxxx78',
  'message': 'Hello world',
  'key': 'textbelt',
})
print(resp.json())