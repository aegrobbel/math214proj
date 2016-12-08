import requests

# USDA Food Composition Database api
url = 'http://api.nal.usda.gov/ndb/reports/?api_key=dVP7gbzixR1XiqebXaMCaiqEHQOSRV33QHkB5EAv&type=b'


lines = [line.rstrip('\n') for line in open('prices.txt')]
for line in lines:
	if (line.find("lb") != -1):
		line = float(line.replace(' lb', '')) * 0.220462
	elif (line.find("oz") != -1):
		line = float(line.replace(' oz', '')) * 3.5274
	elif (line.find("Gallon") != -1):
		line = float(line.replace(' Gallon', '')) / 0.0227024456
	print(line)

# selected food codes
ndbnos = ["11354", "11529", "45056237", "11282", "11251", "11205", "11333", "11124", "11109", "11090", "09202", "09003", "09040", "09326", "09132", "09266", "09316", "09236", "09117", "16042", "11304", "16014", "16091", "45047656", "45035423", "45087177", "45108433", "45017350", "20120", "20137", "05118", "13317", "10165", "15076", "05304", "17370", "17142", "01086", "16098", "04585"]
# our chose nutrients from the db
nutrient_ids = ["204", "601", "307", "306", "205", "269", "291", "203", "320", "401", "301", "303", "208"]

for ndbno in ndbnos:
	thisUrl = url + "&ndbno=" + ndbno
	response = requests.get(thisUrl).json()
	if ("errors" in response):
		print(response["errors"])
	else:
		# success
		print(response["report"]["food"]["name"])
		report = response["report"]["food"]["nutrients"]
		for nutr in report:
			for _id in nutrient_ids:
				if (nutr["nutrient_id"] == _id):
					value = nutr["value"]
					unit = nutr["unit"]
					name = nutr["name"]
					# convert units to g
					if (unit == "mg"):
						value = float(value) / 1000
					elif (unit[0] == '\xc2'):
						value = float(value) / 1000000000

					# print(str(value) + " g " + name)
					# print(str(value))
		# print('')