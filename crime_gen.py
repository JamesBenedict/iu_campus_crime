import os
import shutil

from heapq import nsmallest
from datetime import date, datetime, timedelta
import urllib.request
import bs4
import requests
import re

open('data/history.txt', 'w').close()

# date_generator is for when the website is down and for the first bulk download of data
def date_generator_range(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta

def date_generator():
	generated_dates = []
	for result in date_generator_range(date(2016, 1, 1), date(2016, 1, 10), timedelta(days=1)):
		result = result.strftime('%m-%e-%y').lstrip('0')
		result= result.replace(' ', '')
		generated_dates.append(result)
	return generated_dates

# print(date_generator())

def history_compare():
	# compares all the dates extracted from urls against a history file containing days already anaylzed
	# all_dates = date_extract()
	all_dates = date_generator()
	new_dates = []

	for date in all_dates:
		history_file = open('data/history.txt', 'r+')
		history = history_file.readlines()
		date += '\n'
		if date not in history:
			history_file.writelines(date)
			# updates history before checking if the date is in it agian
			history = history_file.readlines()

			new_dates.append(date)
		history_file.close()

	return new_dates
new_dates = history_compare()
print(new_dates)
# print(history_compare())

def scrapper():
	# downloads mi pdf
	# formatted_dates = date_formatter()
	# for day in formatted_dates:
	for day in new_dates:
		day = day.strip()
		download = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
		output = 'data/pdf/'+day+'.pdf'
		print(download)
		try:
			urllib.request.urlretrieve(download, output)
		except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')

def pdf_2_txt():
	scrapper()
	# formatted_dates = date_formatter()
	# for day in formatted_dates:
	for day in new_dates:
		day = day.strip()
		os.system("pdftotext '%s' '%s'" % ('data/pdf/'+day+'.pdf', 'data/text/'+day+'.txt'))
pdf_2_txt()


def pdf_del():
	# deletes all old pdfs
	shutil.rmtree('data/pdf')
	# makes a new folder for next run
	os.makedirs('data/pdf')
# pdf_del()

# def chunker():
# 	print(new_dates)
# chunker()




