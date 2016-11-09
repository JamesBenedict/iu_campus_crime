import numpy as np
import pandas as pd
import os
import glob
import json

path = '../data'
files = glob.glob(os.path.join(path, '*'))
file = path+'/offical/master_iu_crime.csv'

crime_df = pd.read_csv(file, sep=',')


cleaned_long = crime_df.loc[crime_df['long'] != 'ba']
cleaned_lat = cleaned_long.loc[cleaned_long['lat'] != 'na']
# cleaned_lat = cleaned_lat.fillna('status')
cleaned_lat['status']=cleaned_lat['status'].fillna('missing')

def df_to_geojson(df, properties, lat='lat', lon='long'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        lon_float = float(row[lon])
        lat_float = float(row[lat])
        # if row['status'] == 'NaN':

        feature['geometry']['coordinates'] = [lon_float, lat_float]
        for prop in properties:
            feature['properties'][prop] = row[prop]
        geojson['features'].append(feature)
    return geojson


cols = ['report_num', 'date', 'crime_class', 'crime', 'location', 'city', 'state', 'lat', 'long', 'status', ]
# geojson = df_to_geojson(clean_lat, cols)
geojson_dict = df_to_geojson(cleaned_lat, properties=cols)
geojson_str = json.dumps(geojson_dict, indent=2)

 # save the geojson result to a file
output_filename = path + '/json/clean_crime.geojson'
with open(output_filename, 'w') as output_file:
    output_file.write('{}'.format(geojson_str))
    
# how many features did we save to the geojson file?
print('{} geotagged features saved to file'.format(len(geojson_dict['features'])))


# lint w/ http://geojsonlint.com/