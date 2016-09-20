import os
import shutil

from heapq import nsmallest
from datetime import date, datetime, timedelta
import urllib.request
import bs4
import requests
import re
import glob
import csv

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
# print(new_dates)
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
# pdf_2_txt()

def pdf_del():
	# deletes all old pdfs
	shutil.rmtree('data/pdf')
	# makes a new folder for next run
	os.makedirs('data/pdf')
# pdf_del()


def day_log_open():
	# for file in new_files:
		# file = open('data/text'+file+"'", 'r')
	file = open('data/text/1-5-16.txt', 'r')
	log = file.readlines()
	file.close()
	return log

# print(day_log_open()) 

def chunk():
	chunk_start = []
	chunk_end = []
	chunks = {}

	log = day_log_open()	

	for i in range(len(log)):
		if 'date reported' in log[i]:
			chunk_start.append(i)
		elif 'modified date' in log[i]:
			chunk_end.append(i+1)

	for i in range(len(chunk_start)):
		chunks[chunk_start[i]] = chunk_end[i]
	
	# for key, value in chunks.items():
		# print(log[key:value])
		# print()
		# print()

	return log, chunks

def crime_list():
	log = chunk()[0]
	chunks = chunk()[1]
	crime_list = []
	
	for key, value in chunks.items():
		crime_list.append(log[key:value])

	return crime_list
# print(crime_list())

def check():
	crimes = crime_list()
	for crime in crimes:
		csv_magic(crime)

def csv_magic(alist):
	crime_dict = {'date_reported': 0, 'time': 0, 'general_loc': 0, 'report_num': 0, 'occured_from': 0, 'occured_to': 0, 'incident':0, 'disposition':0, 'modified_date':0}
	
	alist = ''.join(alist)

	# pulls the date out of the list
	match = re.search(r'\d{2}/\d{2}/\d{2}', alist)
	date = datetime.strptime(match.group(), '%m/%d/%y').date()
	crime_dict['date_reported'] = date.strftime('%m/%d/%y')

	# general locatoin
	time = re.search(r'\d{2}:\d{2}', alist)
	print(time)




	

alist = ['date reported: 01/05/16 - TUE at 18:14\n', 'general location:\n', '\n', 'report #:\n', '\n', '160015\n', '\n', 'IU CREDIT UNION - Non-campus building or property\n', '\n', 'date occurred from: 01/05/16 - TUE at 18:00\n', 'date occurred to:\n', '\n', '01/05/16 - TUE at 18:14\n', '\n', 'incident/offenses:\n', '\n', 'RESISTING LAW ENFORCEMENT // OTHER DISTURBANCES // PUBLIC INTOXICATION\n', '\n', 'disposition: CLOSED CASE- ARREST\n', 'modified date: 01/06/16 - WED at 08:45\n']
# print(alist)

csv_magic(alist)


