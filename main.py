# import numpy as np
# import pandas as pd
import os

import requests
import re   #regex
# from tqdm import tqdm_notebook
from datetime import datetime


start_time = datetime.now()

# рейтинг Банков РФ https://www.banki.ru/banks/ratings/
# банки на HH https://hh.ru/employers_company/finansovyj_sektor/bank?vacanciesRequired=true

# вытащим перечень id интересующих банков из csv-файла
import csv
banki = []
with open("inputs/employers_in.csv", "r") as file:
    bankiru = csv.DictReader(file, delimiter=';')
    for bank in bankiru:
        # if (bank['employer_id'] == '3529'):
        if (bank['employer_id'] != ""):
            # print(bank['employer_id'], "-", bank['Название банка'])
            banki.append(bank)
            # print(banki)

today = datetime.now().strftime("%Y%m%d")
path = "outputs/" + today + "/"
os.makedirs(path)

for bank in banki:
    print(bank['employer_id'], "-", bank['employer_name'])
    employer_id = bank['employer_id']
    url = 'https://api.hh.ru/vacancies?employer_id=' + str(employer_id)
    request = requests.get(url).json()
    pages = request['pages']
    # pages = 1
    per_page = request['per_page']
    if (request['found'] < per_page):
        per_page = request['found']

    vacancies_pages = []
    for i in range(0, pages):
        print("vacancies_pages", i, "of", pages)
        vacancies_pages.append(requests.get(url, params={'page': i, 'per_page':per_page}).json())

    vacancies_url = []
    try:
        for i in range(0, pages):
            print("alternate_url pages:", i, "of", pages)
            for j in range(0, per_page):
                vacancies_url.append(vacancies_pages[i]['items'][j]['alternate_url'])
    except IndexError:
        print("IndexError")

    vacancies_id = [re.sub(r'[^0-9]', '', e) for e in vacancies_url]


    vacancy_url = 'https://api.hh.ru/vacancies/{}'
    vacancies = []
    for i in vacancies_id:
        vacancies.append(requests.get(vacancy_url.format(i)).json())

    # # to DataFrame
    # df = pd.DataFrame(var)
    # # remove tags
    # df['description'] = df['description'].apply(lambda x: (re.sub(r'<.*?>', '', str(x))))


    print("saving to json...")
    import json # https://stackoverflow.com/questions/7100125/storing-python-dictionaries
    with open(path + bank['employer_type'] + "_vacancies_id" + str(employer_id) + ".json", "w") as outfile:
        json.dump(vacancies, outfile)

    # # load from json
    # with open('assets\data.json', 'r') as infile:
    #    data = json.load(infile)


print('Время выполнения скрипта=', datetime.now() - start_time)