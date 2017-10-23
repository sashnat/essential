import requests
url = 'https://sjfjrnkjrnrkngkng.org/media/attachments/course67/3.6.2/626.txt'
r = requests.get(url.strip())
print(len(r.text.splitlines()))
# or print(r.text.count('\n'))
