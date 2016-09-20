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

alist = ['date reported: 01/05/16 - TUE at 18:14\n', 'general location:\n', '\n', 'report #:\n', '\n', '160015\n', '\n', 'IU CREDIT UNION - Non-campus building or property\n', '\n', 'date occurred from: 01/05/16 - TUE at 18:00\n', 'date occurred to:\n', '\n', '01/05/16 - TUE at 18:14\n', '\n', 'incident/offenses:\n', '\n', 'RESISTING LAW ENFORCEMENT // OTHER DISTURBANCES // PUBLIC INTOXICATION\n', '\n', 'disposition: CLOSED CASE- ARREST\n', 'modified date: 01/06/16 - WED at 08:45\n']

match = re.search(r'\d{2}/\d{2}/\d{2}', alist[0])
date = datetime.strptime(match.group(), '%m/%d/%y').date()

print(date)
