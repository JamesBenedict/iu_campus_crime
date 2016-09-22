# Indiana University Violent Crime Scrapper and Map

This scrapper goes to the Bloomington Police Department [crime log](http://www.indiana.edu/~iupd/dailyLog.html) and downloads the listed pdfs. The pdfs are posted all the way back to 1-1-2013 if you just change the url and don't use the html page. 

I'm using urllib to download the pdfs and os to convert the pdfs to text. If there is a better method, please let me know. 

My initial algorithm was this:
	1	Get crime logs
			-download pdfs 
			-append new_dates history file
			-convert pdf to txt
	2	Get individual crimes
			-open each text file
			-chunk each crime
			-send a chunk to be analyzed
	3	Append each chunk to crime list
			-look through each chunk with regex
			-find 'date reported', 'date from', 'date to' 'location', 'incident', 'disposition', 'modified date'
			-append each crime to csv
	4	Analyze and map crime
			-run specific stats like #of crime per week, # of each type of crime, etc.
			-manually geocode the location
			-automatically map all the locations
	5	Repeat weekly / as needed 

A sample of three months of data can be found in my data folder.

