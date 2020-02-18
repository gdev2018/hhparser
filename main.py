import numpy as np
import requests
from tqdm import tqdm_notebook
import pandas as pd


r = requests.get('https://api.hh.ru/vacancies?employer_id=39305').json()
