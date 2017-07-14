#/bin/python
import json

def fun_Instance_Volume_Tagging(Instance_ID, Instance):
    for Volumes in Instance["Instances"][0]["BlockDeviceMappings"]:
        VOL_ID = Volumes["Ebs"]["VolumeId"]
        for Tags in Instance["Instances"][0]["Tags"]:
            TAG_KEY = Tags["Key"]
            TAG_VALUE = Tags["Value"]
            print "aws ec2 create-tags --resources " + VOL_ID + " --tags Key=" + TAG_KEY + ",Value=" + TAG_VALUE +""

with open("Instances_full") as json_file:
    json_data = json.load(json_file)
    for Instances in json_data["Reservations"]:
        Instance_ID = Instances["Instances"][0]["InstanceId"];
        fun_Instance_Volume_Tagging(Instance_ID, Instances)
