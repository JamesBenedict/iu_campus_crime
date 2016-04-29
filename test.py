import bs4 
import requests
import datetime
import urllib
import re

new_dates = []
site_links = []
log_links = []


history = open('data/past_dates.txt', 'r')
past_dates = history.readlines()
# print(past_dates)
history.close()

def url_grab():
	# grabs a list of all urls from iupd webpage
	res = requests.get('http://www.indiana.edu/~iupd/dailyLog.html')
	res.raise_for_status()
	website = bs4.BeautifulSoup(res.text, 'html.parser')
	# .site_links = website.select('li > a')
	for link in website.find_all('a', href=re.compile('Documents/Daily Log/')):
		site_links.append(link)
		# print(link)

def history_check():
	# checks to see if date was already anaylzed
	for element in site_links:
		element_list = (str(element).split())
		date = element_list[2][4:11]
		if date[-1] == '.':
			date = date[0:6]

		date += '\n'

		if date in past_dates:
			pass
		else: 
			new_dates.append(date)

	log = open('data/past_dates.txt', 'a')
	log.writelines(new_dates)
	log.close()
	# print(new_dates)

def scrapper():
	for day in new_dates:
		day = day.strip('\n')
		input1 = 'http://www.indiana.edu/~iupd/Documents/Daily%20Log/'+day+'.pdf'
		print(input1)
		output = "data/"+day+'.pdf'
		print(output)
		testfile = urllib.URLopener()
		testfile.retrieve(input1, output)

url_grab()
history_check()
scrapper()

