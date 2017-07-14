import subprocess
import datetime

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

###Initializing the Image Json will all the details of Images of Currnet Account
time = datetime.datetime.now().strftime ("%Y-%m-%d-%H:%M:%S")
filename_image = ('Full_Json_Images-' + time + '.json')
print ("Creating the Image Description File \t: " + filename_image )
f = open(filename_image , 'w')
subprocess.call(['aws', 'ec2', 'describe-images', '--owner', '397912580622'], stdout = f)
f.close()

print "=================================="


