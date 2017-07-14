#/bin/python
import json

def fun_Volume_Snapshot_Tagging(SnapshotID, VolumeID):
    with open("Full_Json_Volumes.json") as json_file:
        json_data = json.load(json_file)
        for Volume in json_data["Volumes"]:
            if Volume["VolumeId"] == VolumeID:
                for Tags in Volume["Tags"]:
                    print "aws ec2 create-tags --resources " + SnapshotID + " --tags Key=" + Tags["Key"] + ",Value=" + Tags["Value"] +""

with open("Full_Json_Snapshots.json") as json_file:
    json_data = json.load(json_file)
    for Snapshot in json_data["Snapshots"]:
        SnapshotID = Snapshot["SnapshotId"]
        VolumeID = Snapshot["VolumeId"]
        fun_Volume_Snapshot_Tagging(SnapshotID, VolumeID)
