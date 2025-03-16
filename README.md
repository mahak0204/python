# python
# Web Scraping Project: Quotes to Scrape

## Overview
This project is a simple web scraper built in Python to extract quotes and their authors from the website [Quotes to Scrape](http://quotes.toscrape.com). The data is stored in an SQLite database for easy access and analysis.

## Project Structure
- `scraper.py`: The main Python script that performs the web scraping and stores data in `quotes.db`.
- `quotes.db`: The SQLite database file containing the scraped quotes and authors.
- `quotes.csv`: (Optional) A CSV file with the exported data for easy viewing and sharing.

## Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`, `sqlite3`, `pandas`

## Installation
1. Clone the repository:
    ```
    git clone https://github.com/yourusername/repositoryname.git
    cd repositoryname
    ```
2. Install the required Python libraries:
    ```
    pip install requests beautifulsoup4 pandas
    ```

## Usage
1. Run the `scraper.py` script to scrape data from the website:
    ```
    python3 scraper.py
    ```
2. The scraped data will be stored in `quotes.db`.

## Export Data
To export data to a CSV file, use the following command:
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('quotes.db')
df = pd.read_sql_query("SELECT * FROM quotes", conn)
df.to_csv('quotes.csv', index=False)
conn.close()
