# Import packages
import pandas as pd
import numpy as np
import requests
#from scrapy.selector import Selector
from IPython.display import clear_output
import time
import re

# Array of search titles
search_title = ["Data Analist", "Data Analyst", "Data Engineer", "Data Scientist", "Data Management", "Business Intelligence", "BI Specialist", "BI Consultant", "Business Analist", "Business Analyst")
webpage = "test"


timer = time.time()

for title in search_title
path = f"https://nl.indeed.com/jobs?q={title.replace( ' ', '%20')}"
req = requests.get(path)


                