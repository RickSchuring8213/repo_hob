from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

search_title = 'data business intelligence'
page_start = 0
page_end = 0
interval = 10

df = pd.DataFrame(columns=['Title']) #, 'location', 'company', 'salary', 'rating', 'job_description'])
for i in range(page_start, page_end + interval, interval):
    url = f"https://nl.indeed.com/vacatures?q={search_title.replace(' ', '%20')}&radius=0&start={str(i)}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    for x in soup.find_all('div', attrs = {'class': ' row result'}):
        job_title = x.find('a', attrs = {'data-tn-element':'jobTitle'}).text
       
 

        df.append({'job_title': job_title}, ignore_index=True)

    print("Output:",df.shape)
df.to_csv('output.csv')
