import requests


r = requests.get("https://gipfelgold.de")
print(r.status_code)
