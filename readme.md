# Indiana University Violent Crime Scrapper and Map

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

A sample of three months of data can be found in my data folder.

## PDF groupings
The PDFS aren't standard. Each has its own pattern7

1. Pattern 1* 1/26/16 - today
1. Pattern 2* 12/11/14 - 1/24/15
1. Pattern 3* 1/1/13 - 12/10/14

## Examples
[Bloomington crime map w/short timespan](https://jamesbenedict.carto.com/viz/886db910-0030-11e6-9f73-0e8c56e2ffdb/embed_map)

[Crime in Chicagoland](http://crime.chicagotribune.com/)

[Crime LA](http://maps.latimes.com/crime/)
