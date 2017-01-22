import json

data = """{"type":"FeatureCollection","metadata":{"generated":1485032187000,"url":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson","title":"USGS All Earthquakes, Past Hour","status":200,"api":"1.5.4","count":4},"features":[{"type":"Feature","properties":{"mag":1.29,"place":"10km S of Idyllwild, CA","time":1485030412340,"updated":1485030630866,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572167","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572167.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":26,"net":"ci","code":"37572167","ids":",ci37572167,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":40,"dmin":0.06121,"rms":0.15,"gap":52,"magType":"ml","type":"earthquake","title":"M 1.3 - 10km S of Idyllwild, CA"},"geometry":{"type":"Point","coordinates":[-116.7081667,33.65,14.36]},"id":"ci37572167"},
{"type":"Feature","properties":{"mag":4.8,"place":"37km NW of Taron, Papua New Guinea","time":1485029037350,"updated":1485030240040,"tz":600,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/us10007une","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us10007une.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":354,"net":"us","code":"10007une","ids":",us10007une,","sources":",us,","types":",geoserve,origin,phase-data,","nst":null,"dmin":0.599,"rms":1.19,"gap":114,"magType":"mb","type":"earthquake","title":"M 4.8 - 37km NW of Taron, Papua New Guinea"},"geometry":{"type":"Point","coordinates":[152.7595,-4.2685,48.24]},"id":"us10007une"},
{"type":"Feature","properties":{"mag":1.6,"place":"34km WNW of Valdez, Alaska","time":1485028874122,"updated":1485029718351,"tz":-540,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ak15118874","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak15118874.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":39,"net":"ak","code":"15118874","ids":",ak15118874,","sources":",ak,","types":",geoserve,origin,","nst":null,"dmin":null,"rms":0.59,"gap":null,"magType":"ml","type":"earthquake","title":"M 1.6 - 34km WNW of Valdez, Alaska"},"geometry":{"type":"Point","coordinates":[-146.9679,61.2126,2]},"id":"ak15118874"},
{"type":"Feature","properties":{"mag":1.37,"place":"10km SE of Gorman, CA","time":1485028812530,"updated":1485029029748,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572159","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572159.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":29,"net":"ci","code":"37572159","ids":",ci37572159,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":12,"dmin":0.05247,"rms":0.19,"gap":51,"magType":"ml","type":"earthquake","title":"M 1.4 - 10km SE of Gorman, CA"},"geometry":{"type":"Point","coordinates":[-118.7875,34.7256667,10.9]},"id":"ci37572159"}],"bbox":[-146.9679,-4.2685,2,152.7595,61.2126,48.24]}"""

parsed_data = json.loads(data)

min_longitude = parsed_data['bbox'][0]
min_latitude = parsed_data['bbox'][1]
min_depth = parsed_data['bbox'][2]
max_longitude = parsed_data['bbox'][3]
max_latitude = parsed_data['bbox'][4]
max_depth = parsed_data['bbox'][5]

# to be continued


# (self.data_collection_time, datetime.fromtimestamp(int(self.data_collection_time)).strftime('%Y-%m-%d %H:%M:%S'))

revision_status = parsed_data['metadata']['status']
event_count = parsed_data['metadata']['count']
stream_title = parsed_data['metadata']['title']
url = parsed_data['metadata']['url']
time_generated = parsed_data['metadata']['generated']
api_version = parsed_data['metadata']['api']

