# A wrapper module for the USGS Earthquake API. At this point, the primary purpose is ETL for further data analysis.
#Additional features may be added in the future. (c) Jared J. Gerschler 2017

import json
from datetime import datetime
from urllib2 import Request, urlopen, HTTPError

class Quaky(object):

    def __init__(self):
        pass# update this later
    
    def connect(self):
        request = Request('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_month.geojson')# add error handling!
        data = urlopen(request).read()
        self.parsed_data = json.loads(data)
        # bbox
        self.min_longitude = self.parsed_data['bbox'][0]
        self.min_latitude = self.parsed_data['bbox'][1]
        self.min_depth = self.parsed_data['bbox'][2]
        self.max_longitude = self.parsed_data['bbox'][3]
        self.max_latitude = self.parsed_data['bbox'][4]
        self.max_depth = self.parsed_data['bbox'][5]
        # metadata
        self.revision_status = self.parsed_data['metadata']['status']
        self.stream_title = self.parsed_data['metadata']['title']
        self.url = self.parsed_data['metadata']['url']
        self.time_generated = self.parsed_data['metadata']['generated']
        self.api_version = self.parsed_data['metadata']['api']
        self.event_count = self.parsed_data['metadata']['count']        
        # features
        self.geometry_type = [self.parsed_data['features'][i]['geometry']['type'] for i in range(self.event_count)]
        self.event_latitude = [self.parsed_data['features'][i]['geometry']['coordinates'][0] for i in range(self.event_count)]
        self.event_longitude = [self.parsed_data['features'][i]['geometry']['coordinates'][1] for i in range(self.event_count)]
        self.event_depth = [self.parsed_data['features'][i]['geometry']['coordinates'][2] for i in range(self.event_count)]
        self.event_id = [self.parsed_data['features'][i]['id'] for i in range(self.event_count)]
        self.rms_travel_time_residual = [self.parsed_data['features'][i]['properties']['rms'] for i in range(self.event_count)]
        self.id_code = [self.parsed_data['features'][i]['properties']['code'] for i in range(self.event_count)]
        self.max_reported_intensity = [self.parsed_data['features'][i]['properties']['cdi'] for i in range(self.event_count)]
        self.event_sources = [self.parsed_data['features'][i]['properties']['sources'] for i in range(self.event_count)]
        self.network_contributors = {'ak':'','at':'','ci':'','hv':'','ld':'','mb':'','nc':'','nm':'',
                                'nn':'','pr':'','pt':'','se':'','us':'','uu':'','uw':''}
        self.num_seismic_stations = [self.parsed_data['features'][i]['properties']['nst'] for i in range(self.event_count)]
        self.utc_offset = [self.parsed_data['features'][i]['properties']['tz'] for i in range(self.event_count)]
        self.event_summary = [self.parsed_data['features'][i]['properties']['title'] for i in range(self.event_count)]
        self.magnitude_methods = {'Duration':('MD','Md','md'),'Local':('ML','Ml','ml'),'Short-period surface wave':('mb_Lg','mb_lg','MLg'),
                             'Short-period body wave':('mb'),'Twenty-second surface wave':('Ms','Ms_2i'),
                             'Moment':('Mw','mw','Mwb','mwb','Mwc','mwc','Mwr','mwr','Mww','mww','Mi','Mwp','mwp'),'Energy':('Me')}
        self.magnitude_method = [self.parsed_data['features'][i]['properties']['magType'] for i in range(self.event_count)]
        self.extra_info = [self.parsed_data['features'][i]['properties']['detail'] for i in range(self.event_count)]
        self.event_significance = [self.parsed_data['features'][i]['properties']['sig'] for i in range(self.event_count)]
        self.preferred_net = [self.parsed_data['features'][i]['properties']['net'] for i in range(self.event_count)]
        self.event_type = [self.parsed_data['features'][i]['properties']['type'] for i in range(self.event_count)]
        self.review_status = [self.parsed_data['features'][i]['properties']['status'] for i in range(self.event_count)]
        self.most_recent_update = [self.parsed_data['features'][i]['properties']['updated'] for i in range(self.event_count)]
        self.dyfi_index = [self.parsed_data['features'][i]['properties']['felt'] for i in range(self.event_count)]
        self.pager_alert = [self.parsed_data['features'][i]['properties']['alert'] for i in range(self.event_count)]
        self.dist_to_nearest_station = [self.parsed_data['features'][i]['properties']['dmin'] for i in range(self.event_count)]
        self.event_magnitude = [self.parsed_data['features'][i]['properties']['mag'] for i in range(self.event_count)]
        self.azimuthal_gap = [self.parsed_data['features'][i]['properties']['gap'] for i in range(self.event_count)]
        self.event_products = [self.parsed_data['features'][i]['properties']['types'] for i in range(self.event_count)]
        self.event_url = [self.parsed_data['features'][i]['properties']['url'] for i in range(self.event_count)]
        self.associated_ids = [self.parsed_data['features'][i]['properties']['ids'] for i in range(self.event_count)]
        self.oaceanic_event = [self.parsed_data['features'][i]['properties']['tsunami'] for i in range(self.event_count)]
        self.event_place = [self.parsed_data['features'][i]['properties']['place'] for i in range(self.event_count)]
        self.event_time = [self.parsed_data['features'][i]['properties']['time'] for i in range(self.event_count)]
        self.instrumental_intensity = [self.parsed_data['features'][i]['properties']['mmi'] for i in range(self.event_count)]
    
    def output_csv(self, filename):
        datafile = open(filename, 'w')
        datafile.write("id,time,place,depth,intensity,dyfi\n")
        for i in range(self.event_count):
            datafile.write("{0},{1},{2},{3},{4},{5}\n".format(self.event_id[i], self.event_time[i], self.event_place[i],
                                                         self.event_depth[i], self.max_reported_intensity[i], self.dyfi_index[i]))
        datafile.close()

# to be continued!
# (self.data_collection_time, datetime.fromtimestamp(int(self.data_collection_time)).strftime('%Y-%m-%d %H:%M:%S'))
