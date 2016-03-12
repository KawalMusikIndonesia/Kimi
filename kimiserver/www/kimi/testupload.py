import requests
url = 'http://localhost/uploads.php'
files = {'file': open('test3.mp3', 'rb')}
r = requests.post(url, files=files)
