import json
import csv

# Open file with subzone and population
subZoneFile = open('17560.csv')

# Opening JSON file
f = open('master-plan-2019-subzone-boundary-no-sea-geojson.geojson')

# returns JSON object as 
# a dictionary
data = json.load(f)


	
for item in data['features']:
	# properties = item['properties']
	# description = item['properties']['Description']
	item['properties']['Description'] = item['properties']['Description'].replace("<table>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<center>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<tr>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<td>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("</center>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("</table>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("</tr>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("</td>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<th colspan='2' align='center'><em>Attributes</em></th><tr bgcolor=\"#E3E3F3\"> <th>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<th>", "")
	item['properties']['Description'] = item['properties']['Description'].replace("</th>", "")
	item['properties']['Description'] = item['properties']['Description'].replace(" <tr bgcolor=\"#E3E3F3\">", "")
	item['properties']['Description'] = item['properties']['Description'].replace("<tr bgcolor=\"\">", "")

	item['properties']['Description'] = item['properties']['Description'].replace("SUBZONE_NO ", "SUBZONE_NO:")
	item['properties']['Description'] = item['properties']['Description'].replace("SUBZONE_N ", "SUBZONE_N:")
	item['properties']['Description'] = item['properties']['Description'].replace("SUBZONE_C ", "SUBZONE_C:")
	item['properties']['Description'] = item['properties']['Description'].replace("CA_IND ", "CA_IND:")
	item['properties']['Description'] = item['properties']['Description'].replace("PLN_AREA_N ", "PLN_AREA_N:")
	item['properties']['Description'] = item['properties']['Description'].replace("PLN_AREA_C ", "PLN_AREA_C:")
	item['properties']['Description'] = item['properties']['Description'].replace("REGION_N ", "REGION_N:")
	item['properties']['Description'] = item['properties']['Description'].replace("REGION_C ", "REGION_C:")
	item['properties']['Description'] = item['properties']['Description'].replace("INC_CRC ", "INC_CRC:")
	item['properties']['Description'] = item['properties']['Description'].replace("FMEL_UPD_D ", "FMEL_UPD_D:")
	item['properties']['Description'] = item['properties']['Description'].strip()

	descriptionSplitArray = item['properties']['Description'].split("  ")


	# for item in descriptionSplitArray:
	# 	print(item)


	subzoneNo = descriptionSplitArray[0].replace("SUBZONE_NO:", "");
	subzoneNandC = descriptionSplitArray[1].replace("SUBZONE_C:", " SUBZONE_C:")
	subzoneName = subzoneNandC.split("  ")[0].replace("SUBZONE_N:", "")
	subzoneCode = subzoneNandC.split("  ")[1].replace("SUBZONE_C:", "")
	caIndAndPlnAreaName= descriptionSplitArray[2].replace("PLN_AREA_N:", " PLN_AREA_N:")
	planningAreaName = caIndAndPlnAreaName.split("  ")[1].replace("PLN_AREA_N:", "")
	plnAreaCandRegionName= descriptionSplitArray[3].replace("REGION_N:", " REGION_N:")
	regionName = plnAreaCandRegionName.split("  ")[1].replace("REGION_N:", "")

	
	# print(subzoneNo)
	# # print(subzoneNandC)
	# print(subzoneName)
	# # print(subzoneCode)
	# print(planningAreaName)
	# print(regionName)

	item['properties']['subZoneNo'] = subzoneNo
	item['properties']['subZoneName'] = subzoneName
	item['properties']['planningAreaName'] = planningAreaName
	item['properties']['regionName'] = regionName

	# print(item['properties'])


	# item['features']['properties']['Description'] = description

	# print(properties)
	# print(item['properties']['Description'])

updatedFile = open("cleanStage1.geojson", "w")
json.dump(data, updatedFile, indent=4)

f.close()
updatedFile.close()
# csvfile.close()
