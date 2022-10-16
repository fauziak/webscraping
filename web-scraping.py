import bs4
from matplotlib.pyplot import title
import requests 
from bs4 import BeautifulSoup
import pandas as pd 

# Assigning variables to HTML pages to ebing webscraping 

response1 = requests.get("https://www.npd.com/news/entertainment-top-10/2022/top-10-books/")
# print(response1.text)
# print(response2.text)

# Creating BeautifulSoup object for first website
npd_books = BeautifulSoup(response1.text, 'html.parser')

table = npd_books.table
table_rows = table.find_all('tr')
rows = []
table_headers = [header.text for header in table.find_all('th')]
for tr in table_rows:
    td = tr.find_all('td')
    if td:  
        row = []
        for column in td:
            row.append(column.text.strip())
        rows.append(row)
data_frame = pd.DataFrame(rows, columns=table_headers)
data_frame.to_csv('output1.csv', index=False)


# Creating BeautifulSoup object for second website
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
response2 = requests.get("https://www.the-numbers.com/market/2022/top-grossing-movies", headers=agent)
topgrossing_movies = BeautifulSoup(response2.text, 'html.parser')
print(topgrossing_movies)
table2 = topgrossing_movies.table
table_rows = table2.find_all('tr')
rows = []
table_headers = [header.text for header in table2.find_all('th')]
for tr in table_rows:
    td = tr.find_all('td')
    if td:  
        row = []
    for column in td:
            row.append(column.text.strip())
    rows.append(row)
data_frame = pd.DataFrame(rows, columns=table_headers)
data_frame.to_csv('output2.csv', index=False)
