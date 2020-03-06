# import numpy as np
# import pandas as pd
import requests
import re   #regex
# from tqdm import tqdm_notebook
from datetime import datetime


start_time = datetime.now()

# specializations
url = 'https://api.hh.ru/specializations'
specializations = requests.get(url).json()

print("saving to json...")
today = datetime.now().strftime("%Y%m%d")
import json # https://stackoverflow.com/questions/7100125/storing-python-dictionaries
with open("outputs/specializations" + "_dt" + today + ".json", "w") as outfile:
    json.dump(specializations, outfile)


# industries
url = 'https://api.hh.ru/industries'
industries = requests.get(url).json()

print("saving to json...")
today = datetime.now().strftime("%Y%m%d")
import json # https://stackoverflow.com/questions/7100125/storing-python-dictionaries
with open("outputs/industries" + "_dt" + today + ".json", "w") as outfile:
    json.dump(industries, outfile)


print('Время выполнения скрипта=', datetime.now() - start_time)