# A wrapper module for the USGS Earthquake API. At this point, the primary purpose is ETL for further data analysis.
#Additional features may be added in the future. (c) Jared J. Gerschler 2017

import json
from datetime import datetime
from urllib2 import Request, urlopen, HTTPError

data = """{"type":"FeatureCollection","metadata":{"generated":1485032187000,"url":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson","title":"USGS All Earthquakes, Past Hour","status":200,"api":"1.5.4","count":4},"features":[{"type":"Feature","properties":{"mag":1.29,"place":"10km S of Idyllwild, CA","time":1485030412340,"updated":1485030630866,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572167","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572167.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":26,"net":"ci","code":"37572167","ids":",ci37572167,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":40,"dmin":0.06121,"rms":0.15,"gap":52,"magType":"ml","type":"earthquake","title":"M 1.3 - 10km S of Idyllwild, CA"},"geometry":{"type":"Point","coordinates":[-116.7081667,33.65,14.36]},"id":"ci37572167"},
{"type":"Feature","properties":{"mag":4.8,"place":"37km NW of Taron, Papua New Guinea","time":1485029037350,"updated":1485030240040,"tz":600,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/us10007une","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us10007une.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":354,"net":"us","code":"10007une","ids":",us10007une,","sources":",us,","types":",geoserve,origin,phase-data,","nst":null,"dmin":0.599,"rms":1.19,"gap":114,"magType":"mb","type":"earthquake","title":"M 4.8 - 37km NW of Taron, Papua New Guinea"},"geometry":{"type":"Point","coordinates":[152.7595,-4.2685,48.24]},"id":"us10007une"},
{"type":"Feature","properties":{"mag":1.6,"place":"34km WNW of Valdez, Alaska","time":1485028874122,"updated":1485029718351,"tz":-540,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ak15118874","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak15118874.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":39,"net":"ak","code":"15118874","ids":",ak15118874,","sources":",ak,","types":",geoserve,origin,","nst":null,"dmin":null,"rms":0.59,"gap":null,"magType":"ml","type":"earthquake","title":"M 1.6 - 34km WNW of Valdez, Alaska"},"geometry":{"type":"Point","coordinates":[-146.9679,61.2126,2]},"id":"ak15118874"},
{"type":"Feature","properties":{"mag":1.37,"place":"10km SE of Gorman, CA","time":1485028812530,"updated":1485029029748,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572159","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572159.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":29,"net":"ci","code":"37572159","ids":",ci37572159,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":12,"dmin":0.05247,"rms":0.19,"gap":51,"magType":"ml","type":"earthquake","title":"M 1.4 - 10km SE of Gorman, CA"},"geometry":{"type":"Point","coordinates":[-118.7875,34.7256667,10.9]},"id":"ci37572159"}],"bbox":[-146.9679,-4.2685,2,152.7595,61.2126,48.24]}"""


class Quaky(object):

    def __init__(self):
        pass
    def connect(self, data):
        self.parsed_data = json.loads(data)
        # bbox
        min_longitude = self.parsed_data['bbox'][0]
        min_latitude = self.parsed_data['bbox'][1]
        min_depth = self.parsed_data['bbox'][2]
        max_longitude = self.parsed_data['bbox'][3]
        max_latitude = self.parsed_data['bbox'][4]
        max_depth = self.parsed_data['bbox'][5]
        # metadata
        revision_status = self.parsed_data['metadata']['status']
        stream_title = self.parsed_data['metadata']['title']
        url = self.parsed_data['metadata']['url']
        time_generated = self.parsed_data['metadata']['generated']
        api_version = self.parsed_data['metadata']['api']

        self.event_count = self.parsed_data['metadata']['count']        
        
    def output_csv(self, filename):


        



# to be continued


# (self.data_collection_time, datetime.fromtimestamp(int(self.data_collection_time)).strftime('%Y-%m-%d %H:%M:%S'))



# features
# scan through these values for each seismic event!
geometry_type = self.parsed_data['features'][0]['geometry']['type']
event_latitude = self.parsed_data['features'][0]['geometry']['coordinates'][0]
event_longitude = self.parsed_data['features'][0]['geometry']['coordinates'][1]
event_depth = self.parsed_data['features'][0]['geometry']['coordinates'][2]

event_id = self.parsed_data['features'][0]['id']

rms_travel_time_residual = self.parsed_data['features'][0]['properties']['rms']
id_code = self.parsed_data['features'][0]['properties']['code']
max_reported_intensity = self.parsed_data['features'][0]['properties']['cdi']
event_sources = self.parsed_data['features'][0]['properties']['sources']
network_contributors = {'ak':'','at':'','ci':'','hv':'','ld':'','mb':'','nc':'','nm':'',
                        'nn':'','pr':'','pt':'','se':'','us':'','uu':'','uw':''}
num_seismic_stations = self.parsed_data['features'][0]['properties']['nst']
utc_offset = self.parsed_data['features'][0]['properties']['tz']
event_summary = self.parsed_data['features'][0]['properties']['title']
magnitude_methods = {'Duration':('MD','Md','md'),'Local':('ML','Ml','ml'),'Short-period surface wave':('mb_Lg','mb_lg','MLg'),
                     'Short-period body wave':('mb'),'Twenty-second surface wave':('Ms','Ms_20'),
                     'Moment':('Mw','mw','Mwb','mwb','Mwc','mwc','Mwr','mwr','Mww','mww','Mi','Mwp','mwp'),'Energy':('Me')}
magnitude_method = self.parsed_data['features'][0]['properties']['magType']
extra_info = self.parsed_data['features'][0]['properties']['detail']
event_significance = self.parsed_data['features'][0]['properties']['sig']# 0 to 1000
preferred_net = self.parsed_data['features'][0]['properties']['net']
event_type = self.parsed_data['features'][0]['properties']['type']
review_status = self.parsed_data['features'][0]['properties']['status']# automatic, reviewed or deleted
most_recent_update = self.parsed_data['features'][0]['properties']['updated']
dyfi_index = self.parsed_data['features'][0]['properties']['felt']# range 40 - 843
pager_alert = self.parsed_data['features'][0]['properties']['alert']# green orange red yellow PAGER alert
dist_to_nearest_station = self.parsed_data['features'][0]['properties']['dmin']# degrees; 111.2 km
event_magnitude = self.parsed_data['features'][0]['properties']['mag']
azimuthal_gap = self.parsed_data['features'][0]['properties']['gap']
event_products = self.parsed_data['features'][0]['properties']['types']
event_url = self.parsed_data['features'][0]['properties']['url']
associated_ids = self.parsed_data['features'][0]['properties']['ids']
oaceanic_event = self.parsed_data['features'][0]['properties']['tsunami']
event_place = self.parsed_data['features'][0]['properties']['place']
event_time = self.parsed_data['features'][0]['properties']['time']
instrumental_intensity = self.parsed_data['features'][0]['properties']['mmi']

