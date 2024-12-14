import requests

files = {'file': open('audio/Recording.m4a', 'rb')}

response = requests.post('http://localhost:5000/transcribe', files=files)
print(response.status_code)
print(response.text)
