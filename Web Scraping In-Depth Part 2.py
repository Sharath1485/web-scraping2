# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lu87DEu2sPqvR3TzpLANwgGfZ68KVuAC
"""

#Name Sharath Kumar M
#Creation date- 31/03/2021
#version - Python3.6
#in this assignment we will display lowest rated books from http://books.toscrape.com/


#importing all the required libraries
import requests
import bs4

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# Make our request
res = requests.get(base_url.format(1))
# Create our soup
soup = bs4.BeautifulSoup(res.text, 'lxml')
one_star_titles = []
# Now iterate to get info from each page.
# We want to include page 5, so index should go up to, but not include 6,
for n in range (1,6):
  scrape_url = base_url.format(n)
  res = requests.get(scrape_url)
  soup = bs4.BeautifulSoup(res.text,'lxml')
  books = soup.select(".product_pod")
  # within our loop, we'll create another loop to parse the books and select star rating five.
  for book in books:
    if len(book.select('.star-rating.One')) != 0: # if the list is not empty, then we do have a 5 star book. Could also use if 'star-rating Five' in str(book)
      book_title = book.select('a')[1]['title']
      one_star_titles.append(book_title)

for tit in one_star_titles:
	print(tit)