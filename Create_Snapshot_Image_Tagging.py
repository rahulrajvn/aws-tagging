#/bin/python
import json

def fun_Image_Snapshot_Tagging(ImageID, SnapshotID):
	print ImageID, SnapshotID
	with open("Full_Json_Snapshots.json") as json_file:
        	json_data = json.load(json_file)
	        for Snapshot in json_data["Snapshots"]:
			if Snapshot["SnapshotId"] == SnapshotID:
				try:
					for Tags in Snapshot["Tags"]:
						print "aws ec2 create-tags --resources " + ImageID + " --tags Key=" + Tags["Key"] + ",Value=" + Tags["Value"] +""
				except KeyError:
					print "Error"
				

with open("Full_Json_Images.json") as json_file:
    json_data = json.load(json_file)
    for image in json_data["Images"]:
	ImageID = image["ImageId"]
	SnapshotID = image["BlockDeviceMappings"][0]["Ebs"]["SnapshotId"]
	print SnapshotID, ImageID
	fun_Image_Snapshot_Tagging(ImageID, SnapshotID)
	#exit()
