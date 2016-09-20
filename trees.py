import re, glob, csv

# dictionary holding each regex selector
cols = {
	'forest': r"SF[ ]?200[ ,\n\r]+([\w \-]*STATE FOREST)",
	'sold_to': r"SOLD TO[:]?([\w ,.\"\n\r]+)TOTAL",
	'sale_number': r"SALE NUMBER[:]?[ ,]*([0-9]+)",
	'date_of_sale': r"([A-Z]+ [0-9]{1,2},[ ]?[0-9]{4,4})|([0-9]{1,4}/[0-9]{1,2}/[0-9]{1,4})|([0-9]{1,2}-[A-Z]{3,3}-[0-9]{2,4})|([0-9]{1,2}-[0-9]{1,2}-[0-9]{2,4})",
	'total_sale_price': r"TOTAL SALE P[A-Z']+[:]?[ ,\n\r\"\:]*([$]?[0-9,]+\.[0-9]{2,2})",
	'total_cost': r"TOTAL COST[:]?[ ,\n\r\"\:]*([$]?[0-9,]+\.[0-9]{2,2})",
	'net': r"NET[:]?[ ,\n\r\"\:]*([$]?[0-9,]+\.[0-9]{2,2})"
}

# read each csv as a large text block
# loop through selections (in cols) and grab any data
# send results back to main for inclusion in results CSV
def parse_file(filename):
	with open(filename, encoding='ISO-8859-1') as f:
		data = f.read()
		row = {'filename': filename}
		for col, expr in cols.items():
			val = get_value(expr, data)
			row[col] = clean_value(val)
	return row

# use regex to search for matching data, print NOT FOUND if no result
def get_value(expr, data):
	hits = re.search(expr, data, re.IGNORECASE)
	if hits is not None:
		for hit in hits.groups():
			if hit is not None:
				return hit
	return 'NOT FOUND'

# clean up the data
def clean_value(val):
	if val is not None:
		result = val.strip().replace("\n", "|")
		result = re.sub(r",{2,}|\"", "", result)
		result = re.sub(r" {2,}", " ", result)
		return result
	else:
		return 'WTF??'

# main
# grab all csv files, open a connection "csvfile"
# write the header row for results CSV based on keys in dictionary "cols"
# loop through all files and write in any data found as a new line in results CSV
filenames = glob.glob('data/*/*.csv')
with open('trees.csv', 'w') as csvfile:
	writer = csv.DictWriter(csvfile, ['filename'] + list(cols.keys()))
	writer.writeheader()

	for filename in filenames:
		writer.writerow(parse_file(filename))
