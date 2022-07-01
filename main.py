import requests


places = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']
payloads = {'n': '', 'T': '', 'q': '', 'm': '', 'lang': 'ru'}
url_sample = 'https://wttr.in/{}'
for place in places:
    url = url_sample.format(place)
    response = requests.get(url, params=payloads)
    response.raise_for_status()
    print(response.text)