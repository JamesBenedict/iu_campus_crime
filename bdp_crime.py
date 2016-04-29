import os
from heapq import nsmallest
import datetime
import urllib
import bs4
import requests
import re

new_dates = []
site_links = []
log_links = []

history = open('data/past_dates.txt', 'r')
past_dates = history.readlines()
history.close()

def url_grab():
	# grabs a list of all urls from iupd webpage
	res = requests.get('http://www.indiana.edu/~iupd/dailyLog.html')
	res.raise_for_status()
	website = bs4.BeautifulSoup(res.text, 'html.parser')
	# finds all likes with '.../Daily...' in them,
	# then adds those to a list of links which I use to check if I have already anaylzed the pdfs
	for link in website.find_all('a', href=re.compile('Documents/Daily Log/')):
		site_links.append(link)

def history_check():
	# checks to see if date was already anaylzed
	for element in site_links:
		# splits var into indexable thing
		element_list = (str(element).split())
		# extracting the section of the url with the date in it
		date = element_list[2][4:11]
		# single digit days messed my system up and I needed a workaround
		if date[-1] == '.':
			date = date[0:6]
		date += '\n'

		# stores new dates in var outside for loop, to later be added to my past dates. 
		if date in past_dates:
			pass
		else: 
			new_dates.append(date)

	# takes all new dates from new_dates and adds to a text file. 
	# This file is then used to make sure I don't duplicate a file I've already scraped
	log = open('data/past_dates.txt', 'a')
	log.writelines(new_dates)
	log.close()
	# print(new_dates)


def scrapper():
	# takes all the new dates I haven't scraped, and inserts that date into a url
	for day in new_dates:
		day = day.strip('\n')
		input1 = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
		output = "data/"+day+'.pdf'
		# Downloads the pdf and saves with date as name.
		testfile = urllib.URLopener()
		testfile.retrieve(input1, output)

#runs my three functions. I orginally had all of my scrapping as a class,
#but then I wanted my date to be a universal 
url_grab()
history_check()
scrapper()

# strips line break from each day
for day in new_dates:
	day = day.strip('\n')
	os.system("pdftotext '%s' '%s'" % ('data/'+day+'.pdf', 'data/'+day+'.txt'))


class Bdp_crime(object):
	'anaylzes a text file from bdp crime logs'
	crime_list =[]

	today = str(datetime.datetime.now().month)
	today += '/'
	today += str(datetime.datetime.now().day)
	today += '/'
	today += str(datetime.datetime.now().year)
	
	def __init__(self, file, day):
		self.day = day
		self.file = file
		open_file = open(file, 'r')
		self.content = open_file.read()
		open_file.close()
		self.key_word_search()
		self.crime_today()
		self.crimes_all()
		self.cleanup()
		

	def __str__(self):
		reply = self.name

	def test(self):
		# print(self.content.split('\n'))
		pass
	
	def readlines(self):
		return self.content.split('\n')
		# print(self.content.split())


	def key_word_search(self):
		lines = self.readlines()
		chunk_indexs =[]
		key_words = ['RAPE', 'ASSAULT', 'HARASSMENT/INTIMIDATION', 'FORCIBLE ENTRY', 'TRESPASS', 'HARASSMENT', 'INTIMIDATION', 'ATTEMPTED FORCIBLE ENTRY', 'RAPE;', 'FORCIBLE FONDLING', 'INDECENT EXPOSURE', 'INDECENT EXPOSURE', 'AGGRAVATED INJURY', 'FORCIBLE FONDLING;', 'STALKING', 'CONFINEMENT']
		key_word_index = []
		closest_index = []
		temp_list = []
		start_key_chunk = []
		end_key_chunk = []
		chunks = {}

		# fiding the start of each block of info from the crime report.
		#'#:' is the most consistent indicator in the begining of each block or chunk 
		# This is the first step of chunking, finding where to start and end in the overall text document
		for i in range(len(lines)):
			if '#:' in lines[i]:
				chunk_indexs.append(i)
				# print(lines[i])
				# print(i)
				
		#finding indexes of keywords
		#I use this to then find the closest start/end of a chunk 
		#building the chunk middle out
		for i in range(len(lines)):
			for word in key_words:
				if word in lines[i]:
					# Storing the location of every key crime we're interested in
					key_word_index.append(i)
					# print(word)
					# print(key_word_index)

		# finds the index of the begining of the crime's chunk
		# I overstackexchanged here and just got something that takes the closest item in chunk_index that is less than the key_word_index
		for num in key_word_index:
			for item in chunk_indexs:
				if item < num and item not in closest_index:
					closest_index.append(item)

			temp_list.append(nsmallest(1, closest_index, key=lambda x: abs(x-num)))
			# flattens my list of lists in a list
			start_key_chunk = [val for sublist in temp_list for val in sublist]
		

		# finds end of current crime chunk by searching for start of next chunk
		for num in start_key_chunk:
			for item in chunk_indexs:
				if item > num:
					end_key_chunk.append(item)
					break
			# if the last crime chunk is a keyword, there is no '#:' to index after it, this uses the end of the document
			#this is needed if the last crime of the page is a key crime
			if num >= int(chunk_indexs[-1]):
				end_key_chunk.append(len(lines))


		# makes a dictonary with item = start, key = end
		for i in range(len(start_key_chunk)):
			chunks[start_key_chunk[i]] = end_key_chunk[i]

		# appends every line between key and end to the crimes_list list
		# This is a long way of writing:
			# 	for key, value in chunks.items():
			# 	crimes.append(lines[key:value])
			# 	print(lines[key:value])
		# But I didn't want to append the ' ' and I wanted to add a linebreak

		for key, value in chunks.items():	
			i = key
			crimes = []
			while i < value:
				if lines[i] == '':
					pass
				else:
					crimes.append(lines[i])
					crimes.append('\n')
				i += 1
			# print(crimes)
			# print()
			crimes.append('\n')
			self.crime_list.append(crimes)
		# print(self.crime_list)
		# print()

	def crime_today(self):
		log = open('data/crime_new.txt', 'a')		
		log.write('\n'+ '-'*10 +'Start of ' +str(self.day) + '-'*10 + '\n')

		print(self.crime_list)
		# for crime in self.crime_list:
		# 	crime_string = ''.join(crime)
		# 	print(crime_string)
		# 	log.writelines(crime_string)


		
		log.write('-'*10 +'End of ' + str(self.day) + '-'*10 + '\n')
		log.close()




	def crimes_all(self):
		
		new_crimes = open('data/crime_new.txt', 'r')
		new_content = new_crimes.readlines()
		new_crimes.close()


		log = open('data/crimes_all.txt', 'a')
		log.writelines(' ')
		log.close()

	def cleanup(self):
		pass
		
		
for day in new_dates:
	day = day.strip('\n')
	t = Bdp_crime('data/'+day+'.txt', day)
# t.test()
# t.key_word_search()
# t.chunking()