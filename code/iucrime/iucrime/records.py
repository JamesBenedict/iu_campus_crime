""" module for parsing text files that are converted from pdfs """
import re
from datetime import *

class Record():
    """ class for keeping the daily IU police log """

    INFO_PATTERN = re.compile('^(location|incident|disposition|event #|report #)\s*:\s*(.+)', re.IGNORECASE)
    TIME_PATTERN = re.compile('^date and time occurred.*from.*to', re.IGNORECASE)

    def __init__(self, content):
        self.info = {} 
        self.parse(content)

    def parse(self, content):
        line_itr = iter(content.splitlines())
        for line in line_itr:
            m = re.search(Record.INFO_PATTERN, line)
            if m:
                key = m.group(1).lower().replace('#', 'number')
                val = m.group(2).lower()
                self.info[key] = val
                continue

            if re.match(Record.TIME_PATTERN, line):
                line = next(line_itr)
                t_from, t_to = self.parse_from_to_time(line)
                self.info['from datetime'] = t_from
                self.info['to datetime'] = t_to

    def parse_from_to_time(self, timestr):
        fromdate, fromtime, todate, totime = timestr.split('-')
        fromtime = fromtime.split('at')[1].strip()
        totime = totime.split('at')[1].strip()
        t_from = strptime(' '.join([fromdate.strip(), fromtime]), '%m/%d/%y %H:%M')
        t_to = strptime(' '.join([todate.strip(), totime]), '%m/%d/%y %H:%M')
        return (t_from, t_to)
    
