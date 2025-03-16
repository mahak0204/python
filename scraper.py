import requests
from bs4 import BeautifulSoup
import sqlite3

url='http://quotes.toscrape.com'

conn=sqlite3.connect('quotes.db')
cursor=conn.cursor()

cursor.execute('''
	CREATE TABLE IF NOT EXISTS quotes (
		id INTEGER PRIMARY KEY AUTOINCREMENT,
		quote TEXT, 
		author TEXT
	)
''')

try:
	response = requests.get(url)
	response.raise_for_status()

	soup = BeautifulSoup(response.text, 'html.parser')

	quotes = soup.find_all('div', class_='quote')
	
	for quote in quotes:
		text = quote.find('span', class_='text').get_text()
		author = quote.find('small', class_='author').get_text()

	cursor.execute('''
		INSERT INTO quotes (quote, author)
		VALUES(?,?)
	''', (text, author))

	conn.commit()



except requests.exceptions.HTTPError as err:
	print(f"HTTP error occured: {err}")
except Exception as err:
	print(f"An error occured: {err}")
finally:
	conn.close()

