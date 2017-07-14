import subprocess
import datetime
import json
import os
import time
from progress.bar import Bar


##Executing the Tagging for the Images
print "Executing the Tagging for Images"
input_file = open("Volume_SnapShot_tags", 'r')
for line in input_file:
        line = line.strip()
        print line
	os.system(line)
#	subprocess.Popen("%s", line)
	#subprocess.call(['/bin/bash', '-c', line])
input_file.close()
