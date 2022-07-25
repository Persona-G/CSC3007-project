import json
import csv

# Open file with subzone and population
subZoneFile = open('17560.csv')

# Opening JSON file
f = open('cleanStage1.geojson')

# returns JSON object as 
# a dictionary
data = json.load(f)

# # Iterating through the json list
# with open('17560.csv', newline='') as csvfile:
# 	csvreader = csv.reader(csvfile)
# 	for row in csvreader:
# 		# print("row :", row)
# 		# print("first: ", row[0])
# 		# print("sec: ", row[1])



# 		if (currentSubZoneName.upper() == subzoneName):
# 			print("found subzone " + subzoneName)
# 			item['properties']['population'] = currentPop 
# 			break;	

csvreader = csv.reader(subZoneFile)

for row in csvreader:

	currentSubZoneName = row[0].upper().strip()
	currentPop = row[1]
	
	# print("current subzone ", currentSubZoneName)

	for item in data['features']:
		# properties = item['properties']
		# description = item['properties']['Description']

		subZoneName = item['properties']['subZoneName']
		# print(item['properties'])
		# print(" ==== json subzone: " + subZoneName)
		if (currentSubZoneName == subZoneName):
			# print("|||||||||||||||| match found ||||||||||||||||")
			item['properties']['population'] = currentPop

		# break

updatedFile = open("cleanStage2.geojson", "w")
json.dump(data, updatedFile, indent=4)

f.close()
subZoneFile.close()

