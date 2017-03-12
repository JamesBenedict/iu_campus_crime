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


def pdf_2_txt():
	# turns my pdf into super unstructed text
	os.system("pdftotext '%s' '%s'" % ('09-25-16.pdf', 'crime.txt'))



def day_log_open():
	# for the moment just sticking to one day
	file = open('crime.txt', 'r')
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
		if 'Arrest Time/Date' in log[i]:
			chunk_start.append(i)
		elif 'Clearance Code' in log[i]:
			chunk_end.append(i+2)

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

for crime in crime_list():
	for item in crime:
		if 'TRANSIENT' in item:
			

