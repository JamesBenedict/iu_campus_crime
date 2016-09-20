import os,csv

home = os.getcwd()

data = os.path.join(home, 'data')
pdf = os.path.join(data, 'pdf')
text = os.path.join(data, 'text')

if not os.path.exists(data):
	os.makedirs(data)
if not os.path.exists(pdf):
	os.makedirs(pdf)
if not os.path.exists(text):
	os.makedirs(text)

os.chdir(data)
history = open('history.txt', 'a').close()

# crime_log = open('crime_log.csv', 'a').close

