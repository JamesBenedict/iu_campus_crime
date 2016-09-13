import os
from heapq import nsmallest
import datetime
import urllib.request
import bs4
import requests
import re

def all_url():
	# grabs all the urls from the bpd webpage
	all_links = []
	# directs program to IUPD webpage
	res = requests.get('http://www.indiana.edu/~iupd/dailyLog.html')
	res.raise_for_status()
	base_website = bs4.BeautifulSoup(res.text, 'html.parser')

	# returns all links with 'Docu..' in the url.
	for link in base_website.find_all('a', href=re.compile('Documents/Daily Log/')):
		all_links.append(str(link))

	# returns a list of all the links on the website
	return all_links


def date_extract():
	# extracts dates from all the urls
	all_dates = []
	for url in all_url():
		all_dates.append(url[-24:-13].strip('>').strip(' ')+'\n')
	
	return all_dates


def history_compare():
	# compares all the dates extracted from urls against a history file containing days already anaylzed
	all_dates = date_extract()
	new_dates = []

	for date in all_dates:
		history_file = open('data/history.txt', 'r+')
		history = history_file.readlines()
		if date not in history:
			history_file.writelines(date)
			# updates history before checking if the date is in it agian
			history = history_file.readlines()
			new_dates.append(date)
		history_file.close()
	return new_dates

def date_formatter():
	new_dates = history_compare()
	# gets the freaking dates in the right format
	bad_year_dates = []
	formatted_dates = []
	bad_year_date = ''

	# converts list to str bc it was taking too long with a list
	new_dates = ','.join(new_dates)
	# looks at each character and only moves over the relevant ones to formatted date str

	for char in new_dates:
		if char in '1234567890':
			bad_year_date += char
		elif char == '/':
			bad_year_date += '-'
		elif char == ',':
			bad_year_date += ','
	
	bad_year_dates = bad_year_date.split(',')
	
	if len(bad_year_dates) > 1:
		for day in bad_year_dates:	
			dt = datetime.datetime.strptime(day, '%m-%d-%Y').strftime('%m-%e-%y').lstrip('0')
			dt= dt.replace(' ', '')
			# print(dt)
			formatted_dates.append(dt)
	else:
		print('no new dates')

	return formatted_dates		
# print(date_formatter())

formatted_dates = date_formatter()

def scrapper():
	# downloads mi pdf
	# formatted_dates = date_formatter()
	for day in formatted_dates:
		download = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
		output = 'data/pdf/'+day+'.pdf'
		print(download)
		urllib.request.urlretrieve(download, output)

def pdf_2_txt():
	scrapper()
	# formatted_dates = date_formatter()
	for day in formatted_dates:
		os.system("pdftotext '%s' '%s'" % ('data/pdf/'+day+'.pdf', 'data/txt/'+day+'.txt'))
pdf_2_txt()

# def pdf_del():


