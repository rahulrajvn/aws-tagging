##Script to Tag the Images, Volumes and Snapshots with Tags of the Instances
##Version 2.0
##This Script will tag all the Volumes, Images and Snapshots again with Tags of Instances
##It will not check wheather Volumes, Images and Snapshots are already tagged.
import subprocess
import datetime
import json
import os
import time
from progress.bar import Bar


def fun_Instance_Volume_Tagging(Instance_ID, Instance):
    for Volumes in Instance["Instances"][0]["BlockDeviceMappings"]:
        VOL_ID = Volumes["Ebs"]["VolumeId"]
        for Tags in Instance["Instances"][0]["Tags"]:
            TAG_KEY = Tags["Key"]
            TAG_VALUE = Tags["Value"]
	    with open(filename_volume) as json_file:
    		json_data = json.load(json_file)
    		for Volume in json_data["Volumes"]:
        	    if Volume["VolumeId"] == VOL_ID:
		        try:
			    for Vol_Tags in Volume["Tags"]:
			        if Tags["Key"] == TAG_KEY:
				    continue
				    #print "Volume Already Tagged"			 
			except KeyError:
			    fo.write ("\naws ec2 create-tags --resources " + VOL_ID + " --tags Key=" + TAG_KEY + ",Value=" + TAG_VALUE +"")

def fun_Volume_Snapshot_Tagging(SnapshotID, VolumeID):
   	with open(filename_volume) as json_file:
	       	json_data = json.load(json_file)
        	for Volume in json_data["Volumes"]:
            		if Volume["VolumeId"] == VolumeID:
                		for Tags in Volume["Tags"]:
					with open(filename_snapshot) as json_file:
	        				json_data = json.load(json_file)
	        				for Snapshot in json_data["Snapshots"]:
							if Snapshot["SnapshotId"] == SnapshotID:
								try:
									for Tags in Snapshot["Tags"]:
										continue
								except KeyError:
									fo.write ("\naws ec2 create-tags --resources " + SnapshotID + " --tags Key=" + Tags["Key"] + ",Value=" + Tags["Value"] +"")
	


def fun_Image_Snapshot_Tagging(ImageID, SnapshotID):
        with open(filename_snapshot) as json_file:
                json_data = json.load(json_file)
                for Snapshot in json_data["Snapshots"]:
                        if Snapshot["SnapshotId"] == SnapshotID:
                                try :
                                        for Tags in Snapshot["Tags"]:
                                                with open(filename_image) as json_file:
                                                        json_data = json.load(json_file)
                                                        for Image in json_data["Images"]:
                                                                if Image["ImageId"] == ImageID:
                                                                        try:
                                                                                for Tags in Image["Tags"]:
                                                                                        continue
                                                                        except KeyError:
                                                                                fo.write ("\naws ec2 create-tags --resources " + ImageID + " --tags Key=" + Tags["Key"] + ",Value=" + Tags["Value"] +"")
                                except KeyError:
                                        continue




print "Collecting the Details needed....."
print "=================================="
###Initializing the Instance Json File having details of all Instances
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_instance = ('Full_Json_Instances-' + time + '.json')
print ("Creating the Instance Description File \t: " + filename_instance )
f = open(filename_instance , 'w')
subprocess.call(['aws', 'ec2', 'describe-instances'], stdout = f)
f.close()

###Initializing the Volume Json File having details of all Volume
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_volume  = ('Full_Json_Volume-' + time + '.json')
print ("Creating the Volume Description File \t: " + filename_volume )
f = open(filename_volume , 'w')
subprocess.call(['aws', 'ec2', 'describe-volumes'], stdout = f)
f.close()

###Initializing the Snapshot Json File having details of all Snapshot of current Account
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_snapshot = ('Full_Json_Snapshots-' + time + '.json')
print ("Creating the Snapshot Description File \t: " + filename_snapshot )
f = open(filename_snapshot, 'w')
subprocess.call(['aws', 'ec2', 'describe-snapshots', '--owner', '397912580622'], stdout = f)
f.close()

##Initializing the Image Json will all the details of Images of Currnet Account
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_image = ('Full_Json_Images-' + time + '.json')
print ("Creating the Image Description File \t: " + filename_image )
f = open(filename_image , 'w')
subprocess.call(['aws', 'ec2', 'describe-images', '--owner', '397912580622'], stdout = f)
f.close()

print "=================================="
print "=================================="
Instance_Count = 0;
with open(filename_instance) as f:
    for line in f:
        finded = line.find('InstanceId')
        if finded != -1 and finded != 0:
            Instance_Count += 1 
print ("Total No of Instances \t: "+ str(Instance_Count))

Volume_Count = 0;
with open(filename_volume) as f:
    for line in f:
        finded = line.find('VolumeId')
        if finded != -1 and finded != 0:
            Volume_Count += 1 
print ("Total No of Volume \t: "+ str(Volume_Count))


Snapshot_Count = 0;
with open(filename_snapshot) as f:
    for line in f:
        finded = line.find('SnapshotId')
        if finded != -1 and finded != 0:
		Snapshot_Count += 1
print ("Total No of Snapshot \t: "+ str(Snapshot_Count))


Image_Count = 0;
with open(filename_image) as f:
    for line in f:
        finded = line.find('ImageId')
        if finded != -1 and finded != 0:
            Image_Count += 1
print ("Total No of Image \t: "+ str(Image_Count))
          


print "=================================="
print "=================================="

print "Creating Tag Command for Volume from Instnace"
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_volume_tags = ('volume-tag-creation-' + time + '.sh')
fo = open(filename_volume_tags, 'w')
with open(filename_instance) as json_file:
    json_data = json.load(json_file)
    bar = Bar('Processing', max=Instance_Count)
    for Instances in json_data["Reservations"]:
        Instance_ID = Instances["Instances"][0]["InstanceId"];
        fun_Instance_Volume_Tagging(Instance_ID, Instances)
	bar.next()
bar.finish()
fo.close()
print ("Completed Creating Command \t: " + filename_volume_tags)

print "Creating Tag Command for Snapshots from Volume"
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_snapshot_tags = ('snapshot-tag-creation-' + time + '.sh')
fo = open(filename_snapshot_tags, 'w')
with open(filename_snapshot) as json_file:
    json_data = json.load(json_file)	
    bar = Bar('Processing', max=Snapshot_Count)
    for Snapshot in json_data["Snapshots"]:
        SnapshotID = Snapshot["SnapshotId"]
        VolumeID = Snapshot["VolumeId"]
        fun_Volume_Snapshot_Tagging(SnapshotID, VolumeID)
	bar.next()
bar.finish()
fo.close()
print ("Completed Creating Command \t: " + filename_snapshot_tags)



print "Creating Tag Command for Images from Snapshot"
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_image_tags = ('image-tag-creation-' + time + '.sh')
fo = open(filename_image_tags, 'w')
with open(filename_image) as json_file:
    json_data = json.load(json_file)
    bar = Bar('Processing', max=Image_Count)
    for image in json_data["Images"]:
	ImageID = image["ImageId"]
	SnapshotID = image["BlockDeviceMappings"][0]["Ebs"]["SnapshotId"]
	fun_Image_Snapshot_Tagging(ImageID, SnapshotID)
	bar.next()
bar.finish()
fo.close()
print ("Completed Creating Command \t: " + filename_image_tags)



print "=================================="
print "=================================="

#Counting the volume tags to be created 
input_file = open(filename_volume_tags, 'r')
vol_tags_count = 0
for line in input_file:
	line = line.strip()
    	vol_tags_count += 1
input_file.close()


#Counting the Snapshot tags to be created
input_file = open(filename_snapshot_tags, 'r')
snapshot_tags_count = 0
for line in input_file:
        line = line.strip()
        snapshot_tags_count += 1
input_file.close()

#Counting the Image tags to be created
input_file = open(filename_image_tags, 'r')
image_tags_count = 0
for line in input_file:
        line = line.strip()
        image_tags_count += 1
input_file.close()

print "=================================="
print "=================================="

##Executing the Tagging for the Volumes
print "Executing the Tagging for Volumes"
input_file = open(filename_volume_tags, 'r')
bar = Bar('Processing', max=vol_tags_count)
for line in input_file:
        line = line.strip()
        print line
	os.system(line)
	#subprocess.call(['/bin/bash', '-c', line])
	bar.next()
bar.finish()
input_file.close()

#Executing the Tagging for the Snapshots
print "Executing the Tagging for Snapshots"
input_file = open(filename_snapshot_tags, 'r')
bar = Bar('Processing', max=snapshot_tags_count)
for line in input_file:
        line = line.strip()
        print line
	os.system(line)
	#subprocess.call(['/bin/bash', '-c', line])
        bar.next()
bar.finish()
input_file.close()


##Executing the Tagging for the Images
print "Executing the Tagging for Images"
input_file = open(filename_image_tags, 'r')
bar = Bar('Processing', max=image_tags_count)
for line in input_file:
        line = line.strip()
        print line
	os.system(line)
	#subprocess.call(['/bin/bash', '-c', line])
        bar.next()
bar.finish()
input_file.close()

