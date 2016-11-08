import numpy as np
import pandas as pd
import os
import glob
import geopy
from geopy.geocoders import Nominatim


path = ''
files = glob.glob(os.path.join(path, '*'))
fpath = path+'offical/IU_crime_13-15.csv'