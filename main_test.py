import requests
import re   #regex
from tqdm import tqdm_notebook
# import my_timer

import time

def my_timer(f):
    def tmp(*args, **kwargs):
        start_time=time.time()
        result=f(*args, **kwargs)
        delta_time=time.time() - start_time
        print ('Время выполнения функции {}' .format(delta_time))
        return result

    return tmp

@my_timer
def method1():
    employer_id = 3159173
    url = 'https://api.hh.ru/vacancies?employer_id=' + str(employer_id)
    request = requests.get(url).json()
    pages = request['pages']
    # pages = 1
    per_page = request['per_page']

    vac = []
    for i in tqdm_notebook(range(0, pages)):
        vac.append(requests.get(url, params={'page': i, 'per_page':per_page}).json())

    # id всех вакансий

    try:
        pac = []
        for i in tqdm_notebook(range(0, pages)):
            for j in tqdm_notebook(range(0, per_page)):
                pac.append(vac[i]['items'][j]['alternate_url'])
    except Exception :
        print("error")

    lili = [re.sub(r'[^0-9]', '', e) for e in pac]


    vak_url = 'https://api.hh.ru/vacancies/{}'
    var = []
    for i in lili:
        var.append(requests.get(vak_url.format(i)).json())

    # save to json
    import json # https://stackoverflow.com/questions/7100125/storing-python-dictionaries
    with open('assets/data_' + str(employer_id) + '.json', 'w') as outfile:
        json.dump(var, outfile)

    return "done1"

@my_timer
def method2():
    employer_id = 3529
    url = 'https://api.hh.ru/vacancies?employer_id=' + str(employer_id)
    request = requests.get(url).json()
    pages = request['pages']
    pages = 3
    per_page = request['per_page']


    # id всех вакансий без промежуточного vac, но по скорости даже медленнее, кажись
    vah = []
    for i in range(0, pages):
        for j in range(0, per_page):
            vah.append(requests.get(url, params={'page': i, 'per_page':per_page}).json()['items'][j]['alternate_url'])
    lulu = [re.sub(r'[^0-9]', '', e) for e in vah]


    vak_url = 'https://api.hh.ru/vacancies/{}'

    var = []
    for i in lulu:
        var.append(requests.get(vak_url.format(i)).json())

    # save to json
    import json # https://stackoverflow.com/questions/7100125/storing-python-dictionaries
    with open('assets/data_' + str(employer_id) + '.json', 'w') as outfile:
        json.dump(var, outfile)

    return "done2"


from datetime import datetime
import time

start_time = datetime.now()

print (method1())
# print (method2())

print(datetime.now() - start_time)

