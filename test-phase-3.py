#/bin/python
import json


def fun_Instance_Name(Instance):
    for Tags in Instance["Instances"][0]["Tags"]:
        if Tags["Key"] == "Name":
            Instance_NAME = Tags["Value"]
            return Instance_NAME

def fun_Instance_State(Instance):
    return Instance["Instances"][0]["State"]["Name"]

def fun_Instance_Project(Instance):
    for Tags in Instance["Instances"][0]["Tags"]:
        if Tags["Key"] == "Project":
            Instance_PROJECT = Tags["Value"]
            return Instance_PROJECT

def fun_Instance_Volume(Instance):
    for Volumes in Instance["Instances"][0]["BlockDeviceMappings"]:
        print Volumes["Ebs"]["VolumeId"]


def fun_Instance_Tags(Instance):
    for Tags in Instance["Instances"][0]["Tags"]:
        print Tags["Key"], Tags["Value"]


def fun_Instance_Volume_Tagging(Instance_ID, Instance):
    #print Instance_ID
    #print Instance
    #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    for Volumes in Instance["Instances"][0]["BlockDeviceMappings"]:
        #print "*****************************"
        #print Volumes["Ebs"]["VolumeId"]
        VOL_ID = Volumes["Ebs"]["VolumeId"]
        for Tags in Instance["Instances"][0]["Tags"]:
            #print Tags["Key"], Tags["Value"]
            TAG_KEY = Tags["Key"]
            TAG_VALUE = Tags["Value"]
            print "aws ec2 create-tags --resources " + VOL_ID + " --tags Key=" + TAG_KEY + ",Value=" + TAG_VALUE +""
    #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"

with open("instances_full") as json_file:
    json_data = json.load(json_file)
    #print(json.dumps(json_data, indent=4))
    #print("=====================")
    #print "ID" " \t\t" "Name" "\t\t\t\t" "State"," \t\t" "Project"
    for Instances in json_data["Reservations"]:
        Instance_ID = Instances["Instances"][0]["InstanceId"];
        #Instance_NAME = fun_Instance_Name(Instances)
        #Instance_PROJECT = fun_Instance_Project(Instances)
        #Instance_STATE = fun_Instance_State(Instances)
        #print "+++++++++++"
        #print Instance_ID
        #print Instances
        #fun_Instance_Volume(Instances)
        #fun_Instance_Tags(Instances)
        fun_Instance_Volume_Tagging(Instance_ID, Instances)
        #for Tags in Instances["Instances"][0]["Tags"]:
        #    if Tags["Key"] == "Name":
        #        Instance_NAME = Tags["Value"]
        #print Instance_ID, "\t",Instance_NAME, "\t",Instance_STATE, "\t", Instance_PROJECT 
        #exit() 
