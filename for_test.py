import requests
from trace_way import find_way

url_hulk = "https://superheroapi.com/api/2619421814940190/search/Hulk"
url_captain_america = "https://superheroapi.com/api/2619421814940190/search/Captain America"
url_thanos = "https://superheroapi.com/api/2619421814940190/search/Thanos"

dir_int = {}


@find_way('logs/logs.log')
def take_int(url):
    resp = requests.get(url)
    id = resp.json()['results'][0]['id']
    name = resp.json()['results'][0]['name']
    tmp_url = f'https://superheroapi.com/api/2619421814940190/{id}/powerstats'
    resp_tmp = requests.get(tmp_url)
    int = resp_tmp.json()['intelligence']
    dir_int[name] = int


take_int(url_hulk)
take_int(url_captain_america)
take_int(url_thanos)

calc = 0
name = ''
for i in dir_int.items():
    if int(i[1]) > calc:
        calc = int(i[1])
        name = i[0]

print(f'Самый умный супергерой - {name}\nИмеет {calc} очков интеллекта')