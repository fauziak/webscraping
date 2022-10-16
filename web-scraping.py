import bs4
from matplotlib.pyplot import title
import requests 
from bs4 import BeautifulSoup
import pandas as pd 

# Assigning variables to HTML pages to ebing webscraping 

response1 = requests.get("https://www.npd.com/news/entertainment-top-10/2022/top-10-books/")
print(response1.text)

response2 = requests.get("https://editorial.rottentomatoes.com/guide/best-movies-2022/")
print(response2.text)

# Creating BeautifulSoup object for both websites
npd_books = BeautifulSoup(response1.text, 'html.parser')
print(npd_books.prettify())

#rottentomatoes_movies = BeautifulSoup(response2.text, 'html.parser')
#print(rottentomatoes_movies.prettify())

# Extracting the top 10 books from response1 
top10books = npd_books.find('table',class_='a-min-width-table__inner')
print(top10books)
df = pd.read_html(str(top10books)) [0]

table = npd_books.table
table_rows = table.find_all('tr')

data = {}
for tr in table_rows:
    td = tr.find_all('td')
    if len(td) != 2 : continue
    data[td[0].text] = td[1].text.strip()

data_frame = pd.DataFrame([data], columns=data.keys())

data_frame.to_csv('output.csv', index=False)
