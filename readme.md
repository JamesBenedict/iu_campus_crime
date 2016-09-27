# Indiana University Violent Crime Scrapper and Map

<<<<<<< HEAD
This scrapper goes to the Bloomington Police Department [crime log](http://www.indiana.edu/~iupd/dailyLog.html) and downloads the listed pdfs. The pdfs are posted all the way back to 1-1-2013 but can only be accessed by changing the date in the url.

I'm using urllib to download the pdfs and os to convert the pdfs to text. If there is a better method, please let me know. 

My plan is:
- Get crime logs
	- download pdfs 
	- append downloaded dates to a history file
	- convert pdf to txt
- Get individual crimes
	- open each text file
	- break it into list for each crime
	- send a these chunks to be analyzed
- Append each chunk to crime list
	- look through each chunk with regex
	- find 'date reported', 'date from', 'date to' 'location', 'incident', 'disposition', 'modified date'
	- append each crime to csv
- Analyze and map crime
	- run specific stats like #of crime per week, # of each type of crime, etc.
	- manually geocode the location because most of the locations are general (e.g. Franklin Hall)
	- automatically map all the locations
- Repeat weekly / as needed 
=======
Hi YY,

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
>>>>>>> parent of 4a08a4f... more documentation

A sample of three months of data can be found in my data folder.

## Examples
[Bloomington crime map w/short timespan](https://jamesbenedict.carto.com/viz/886db910-0030-11e6-9f73-0e8c56e2ffdb/embed_map)

[Crime in Chicagoland](http://crime.chicagotribune.com/)

[Crime LA](http://maps.latimes.com/crime/)
