import json

data = """{"type":"FeatureCollection","metadata":{"generated":1485032187000,"url":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson","title":"USGS All Earthquakes, Past Hour","status":200,"api":"1.5.4","count":4},"features":[{"type":"Feature","properties":{"mag":1.29,"place":"10km S of Idyllwild, CA","time":1485030412340,"updated":1485030630866,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572167","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572167.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":26,"net":"ci","code":"37572167","ids":",ci37572167,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":40,"dmin":0.06121,"rms":0.15,"gap":52,"magType":"ml","type":"earthquake","title":"M 1.3 - 10km S of Idyllwild, CA"},"geometry":{"type":"Point","coordinates":[-116.7081667,33.65,14.36]},"id":"ci37572167"},
{"type":"Feature","properties":{"mag":4.8,"place":"37km NW of Taron, Papua New Guinea","time":1485029037350,"updated":1485030240040,"tz":600,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/us10007une","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/us10007une.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"reviewed","tsunami":0,"sig":354,"net":"us","code":"10007une","ids":",us10007une,","sources":",us,","types":",geoserve,origin,phase-data,","nst":null,"dmin":0.599,"rms":1.19,"gap":114,"magType":"mb","type":"earthquake","title":"M 4.8 - 37km NW of Taron, Papua New Guinea"},"geometry":{"type":"Point","coordinates":[152.7595,-4.2685,48.24]},"id":"us10007une"},
{"type":"Feature","properties":{"mag":1.6,"place":"34km WNW of Valdez, Alaska","time":1485028874122,"updated":1485029718351,"tz":-540,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ak15118874","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ak15118874.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":39,"net":"ak","code":"15118874","ids":",ak15118874,","sources":",ak,","types":",geoserve,origin,","nst":null,"dmin":null,"rms":0.59,"gap":null,"magType":"ml","type":"earthquake","title":"M 1.6 - 34km WNW of Valdez, Alaska"},"geometry":{"type":"Point","coordinates":[-146.9679,61.2126,2]},"id":"ak15118874"},
{"type":"Feature","properties":{"mag":1.37,"place":"10km SE of Gorman, CA","time":1485028812530,"updated":1485029029748,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572159","detail":"http://earthquake.usgs.gov/earthquakes/feed/v1.0/detail/ci37572159.geojson","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":29,"net":"ci","code":"37572159","ids":",ci37572159,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":12,"dmin":0.05247,"rms":0.19,"gap":51,"magType":"ml","type":"earthquake","title":"M 1.4 - 10km SE of Gorman, CA"},"geometry":{"type":"Point","coordinates":[-118.7875,34.7256667,10.9]},"id":"ci37572159"}],"bbox":[-146.9679,-4.2685,2,152.7595,61.2126,48.24]}"""

detail_1 = """{"type":"Feature","properties":{"mag":1.29,"place":"10km S of Idyllwild, CA","time":1485030412340,"updated":1485030630866,"tz":-480,"url":"http://earthquake.usgs.gov/earthquakes/eventpage/ci37572167","felt":null,"cdi":null,"mmi":null,"alert":null,"status":"automatic","tsunami":0,"sig":26,"net":"ci","code":"37572167","ids":",ci37572167,","sources":",ci,","types":",geoserve,nearby-cities,origin,phase-data,","nst":40,"dmin":0.06121,"rms":0.15,"gap":52,"magType":"ml","type":"earthquake","title":"M 1.3 - 10km S of Idyllwild, CA","products":{"geoserve":[{"indexid":"3806482","indexTime":1485030635084,"id":"urn:usgs-product:us:geoserve:ci37572167:1485030630360","type":"geoserve","code":"ci37572167","source":"us","updateTime":1485030630360,"status":"UPDATE","properties":{"eventsource":"ci","eventsourcecode":"37572167","location":"10km S of Idyllwild-Pine Cove, California","tsunamiFlag":"false","utcOffset":"-480"},"preferredWeight":1,"contents":{"geoserve.json":{"contentType":"application/json","lastModified":1485030633000,"length":1114,"url":"http://earthquake.usgs.gov/realtime/product/geoserve/ci37572167/us/1485030630360/geoserve.json"}}}],"nearby-cities":[{"indexid":"3806480","indexTime":1485030632077,"id":"urn:usgs-product:ci:nearby-cities:ci37572167:1485030630866","type":"nearby-cities","code":"ci37572167","source":"ci","updateTime":1485030630866,"status":"UPDATE","properties":{"eventsource":"ci","eventsourcecode":"37572167"},"preferredWeight":6,"contents":{"nearby-cities.json":{"contentType":"application/json","lastModified":1485030630000,"length":606,"url":"http://earthquake.usgs.gov/realtime/product/nearby-cities/ci37572167/ci/1485030630866/nearby-cities.json"}}},{"indexid":"3806476","indexTime":1485030538188,"id":"urn:usgs-product:ci:nearby-cities:ci37572167-cities1:1485030536274","type":"nearby-cities","code":"ci37572167-cities1","source":"ci","updateTime":1485030536274,"status":"UPDATE","properties":{"eventsource":"ci","eventsourcecode":"37572167"},"preferredWeight":6,"contents":{"nearby-cities.json":{"contentType":"application/json","lastModified":1485030535000,"length":606,"url":"http://earthquake.usgs.gov/realtime/product/nearby-cities/ci37572167-cities1/ci/1485030536274/nearby-cities.json"}}}],"origin":[{"indexid":"3806481","indexTime":1485030633116,"id":"urn:usgs-product:ci:origin:ci37572167:1485030630360","type":"origin","code":"ci37572167","source":"ci","updateTime":1485030630360,"status":"UPDATE","properties":{"azimuthal-gap":"52","depth":"14.36","depth-type":"from location","evaluation-status":"preliminary","event-type":"earthquake","eventParametersPublicID":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?eventid=37572167","eventsource":"ci","eventsourcecode":"37572167","eventtime":"2017-01-21T20:26:52.340Z","horizontal-error":"0.21","latitude":"33.65","longitude":"-116.7081667","magnitude":"1.29","magnitude-azimuthal-gap":"31.8","magnitude-error":"0.161","magnitude-num-stations-used":"27","magnitude-source":"CI","magnitude-type":"ml","minimum-distance":"0.06121","num-phases-used":"64","num-stations-used":"40","origin-source":"CI","quakeml-magnitude-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?magnitudeid=108449837","quakeml-origin-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?originid=105056949","quakeml-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?eventid=37572167","review-status":"automatic","standard-error":"0.15","title":"10km S of Idyllwild, CA","version":"3","vertical-error":"0.32"},"preferredWeight":156,"contents":{"contents.xml":{"contentType":"application/xml","lastModified":1485030631000,"length":195,"url":"http://earthquake.usgs.gov/realtime/product/origin/ci37572167/ci/1485030630360/contents.xml"},"quakeml.xml":{"contentType":"application/xml","lastModified":1485030630000,"length":3087,"url":"http://earthquake.usgs.gov/realtime/product/origin/ci37572167/ci/1485030630360/quakeml.xml"}}}],"phase-data":[{"indexid":"3806483","indexTime":1485030636499,"id":"urn:usgs-product:ci:phase-data:ci37572167:1485030630360","type":"phase-data","code":"ci37572167","source":"ci","updateTime":1485030630360,"status":"UPDATE","properties":{"azimuthal-gap":"52","depth":"14.36","depth-type":"from location","evaluation-status":"preliminary","event-type":"earthquake","eventParametersPublicID":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?eventid=37572167","eventsource":"ci","eventsourcecode":"37572167","eventtime":"2017-01-21T20:26:52.340Z","horizontal-error":"0.21","latitude":"33.65","longitude":"-116.7081667","magnitude":"1.29","magnitude-azimuthal-gap":"31.8","magnitude-error":"0.161","magnitude-num-stations-used":"27","magnitude-source":"CI","magnitude-type":"ml","minimum-distance":"0.06121","num-phases-used":"64","num-stations-used":"40","origin-source":"CI","quakeml-magnitude-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?magnitudeid=108449837","quakeml-origin-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?originid=105056949","quakeml-publicid":"quakeml:service.scedc.caltech.edu/fdsnws/event/1/query?eventid=37572167","review-status":"automatic","standard-error":"0.15","title":"10km S of Idyllwild, CA","version":"3","vertical-error":"0.32"},"preferredWeight":156,"contents":{"contents.xml":{"contentType":"application/xml","lastModified":1485030631000,"length":195,"url":"http://earthquake.usgs.gov/realtime/product/phase-data/ci37572167/ci/1485030630360/contents.xml"},"quakeml.xml":{"contentType":"application/xml","lastModified":1485030630000,"length":249488,"url":"http://earthquake.usgs.gov/realtime/product/phase-data/ci37572167/ci/1485030630360/quakeml.xml"}}}]}},"geometry":{"type":"Point","coordinates":[-116.7081667,33.65,14.36]},"id":"ci37572167"}"""


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

geometry_type = parsed_data['features'][0]['geometry']['type']
event_latitude = parsed_data['features'][0]['geometry']['coordinates'][0]
event_longitude = parsed_data['features'][0]['geometry']['coordinates'][1]
event_depth = parsed_data['features'][0]['geometry']['coordinates'][2]

event_id = parsed_data['features'][0]['id']

parsed_data['features'][0]['properties']['rms']
parsed_data['features'][0]['properties']['code']
parsed_data['features'][0]['properties']['cdi']
parsed_data['features'][0]['properties']['sources']
parsed_data['features'][0]['properties']['nst']
parsed_data['features'][0]['properties']['tz']
parsed_data['features'][0]['properties']['title']
parsed_data['features'][0]['properties']['magType']
parsed_data['features'][0]['properties']['detail']
parsed_data['features'][0]['properties']['sig']
parsed_data['features'][0]['properties']['net']
parsed_data['features'][0]['properties']['type']
parsed_data['features'][0]['properties']['status']
parsed_data['features'][0]['properties']['updated']
parsed_data['features'][0]['properties']['felt']
parsed_data['features'][0]['properties']['alert']
parsed_data['features'][0]['properties']['dmin']
parsed_data['features'][0]['properties']['mag']
parsed_data['features'][0]['properties']['gap']
parsed_data['features'][0]['properties']['types']
parsed_data['features'][0]['properties']['url']
parsed_data['features'][0]['properties']['ids']
parsed_data['features'][0]['properties']['tsunami']
parsed_data['features'][0]['properties']['place']
parsed_data['features'][0]['properties']['time']
parsed_data['features'][0]['properties']['mmi']

