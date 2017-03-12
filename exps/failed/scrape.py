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


# open('data/history.txt', 'w').close()

def date_generator_range(start, end, delta):
	# used with date_generator() below
    curr = start
    while curr < end:
        yield curr
        curr += delta


def date_generator():
	# generates dates for a given range, needs above function
	# when program goes live, the end date will be programed to update to today
	generated_dates = []
	for result in date_generator_range(date(2013, 1, 1), date(2016, 9, 21), timedelta(days=1)):
		# formatting
		result = result.strftime('%m-%e-%y').lstrip('0')
		result= result.replace(' ', '')
		generated_dates.append(result)
		# print(result)
	return generated_dates

# print(date_generator())

def history_compare():
	# stores dates in history.txt and puts new dates in a list
	# removes all the dates that have already been anaylzed from going further
	# during tests, must delete content of history.txt
	all_dates = date_generator()
	# print(all_dates)
	new_dates = []

	for date in all_dates:
		# print(type(date))
		history_file = open('data/history.txt', 'r+')
		history = history_file.readlines()
		date += '\n'
		if date not in history:
			history_file.write(date)
			# updates history before checking if the date is in it agian
			new_dates.append(date)
			history = history_file.readlines()
			# print(date)
		history_file.close()
	print(new_dates)
	return new_dates

#this seems to work better than calling the function multiple times, i don't know why 
new_dates = history_compare()

# print(new_dates)
# print(history_compare())


def scrapper():
	# downloads mi pdf
	for day in new_dates:
		day = day.strip()
		download = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
		output = 'data/pdf/'+day+'.pdf'
		# print(download)
		try:
			urllib.request.urlretrieve(download, output)
		# some dates don't have any crimes, this deals with them
		except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')

def pdf_2_txt():
	# turns my pdf into super unstructed text
	scrapper()
	if not os.path.exists('data/text/2013'):
		os.makedirs('data/text/2013')
	if not os.path.exists('data/text/2014'):
		os.makedirs('data/text/2014')
	if not os.path.exists('data/text/2015'):
		os.makedirs('data/text/2015')
	if not os.path.exists('data/text/2016'):
		os.makedirs('data/text/2016')

	for day in new_dates:
		day = day.strip()
		print(day[-2:])
		year_folder = 'data/text/20'+day[-2:]
	
		# if not os.path.exists(year_folder):
		# 	os.makedirs(year_folder)


		os.system("pdftotext '%s' '%s'" % ('data/pdf/'+day+'.pdf', year_folder+'/'+day+'.txt'))		
pdf_2_txt()

# def scrapper():
# 	# downloads mi pdf
# 	for day in new_dates:
# 		day = day.strip()
# 		download = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
# 		output = 'data/pdf/'+day+'.pdf'
# 		print(download)
# 		try:
# 			urllib.request.urlretrieve(download, output)
# 		# some dates don't have any crimes, this deals with them
# 		except urllib.error.URLError as e: ResponseData = e.read().decode("utf8", 'ignore')

# def pdf_2_txt():
# 	# turns my pdf into super unstructed text
# 	scrapper()
# 	for day in new_dates:
# 		day = day.strip()
# 		os.system("pdftotext '%s' '%s'" % ('data/pdf/'+day+'.pdf', 'data/text/'+day+'.txt'))
# # pdf_2_txt()

def pdf_del():
	# deletes all pdfs, only keep text for record purposes
	shutil.rmtree('data/pdf')
	# makes a new folder for next run
	os.makedirs('data/pdf')
# pdf_del()

# This is the end of my first section, turning pdfs online to text locally

# This is where the program starts to fall apart
# my thinking it to open each text documents, split it into individual crime chunks
# then send each crime chunk through a regex program to pull out key info and append to a csv
# then move onto the next crime in the day, 
# when a day is done move to the next day for all days in new_dates

def day_log_open():
	# for the moment just sticking to one day
	file = open('data/text/1-5-16.txt', 'r')
	log = file.readlines()
	file.close()
	return log

# print(day_log_open()) 


def chunk():
	# take the entire text crime log and chunks each crime into a list
	# the chunk is jsut the index positions before and after each crime
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

# turns the chunk indexs into lists for each crime. 
# slices the log based off the chunk indexs to select an individual crime 
# all crimes stored in lists, a day with many crimes is a list of lists
def crime_list():
	log = chunk()[0]
	chunks = chunk()[1]
	crime_list = []
	
	for key, value in chunks.items():
		crime_list.append(log[key:value])

	return crime_list



#Everything below is me throwing code at the wall 
# print(crime_list())

# def check():
# 	crimes = crime_list()
# 	for crime in crimes:
# 		csv_magic(crime)

# def csv_magic(alist):
# 	crime_dict = {'date_reported': 0, 'time': 0, 'general_loc': 0, 'report_num': 0, 'occured_from': 0, 'occured_to': 0, 'incident':0, 'disposition':0, 'modified_date':0}
	
# 	alist = ''.join(alist)

# 	# pulls the date out of the list
# 	match = re.search(r'\d{2}/\d{2}/\d{2}', alist)
# 	date = datetime.strptime(match.group(), '%m/%d/%y').date()
# 	crime_dict['date_reported'] = date.strftime('%m/%d/%y')

# 	# general locatoin
# 	time = re.search(r'\d{2}:\d{2}', alist)
# 	print(time)
# alist = ['date reported: 01/05/16 - TUE at 18:14\n', 'general location:\n', '\n', 'report #:\n', '\n', '160015\n', '\n', 'IU CREDIT UNION - Non-campus building or property\n', '\n', 'date occurred from: 01/05/16 - TUE at 18:00\n', 'date occurred to:\n', '\n', '01/05/16 - TUE at 18:14\n', '\n', 'incident/offenses:\n', '\n', 'RESISTING LAW ENFORCEMENT // OTHER DISTURBANCES // PUBLIC INTOXICATION\n', '\n', 'disposition: CLOSED CASE- ARREST\n', 'modified date: 01/06/16 - WED at 08:45\n']
# # print(alist)

# csv_magic(alist)


