import os
import subprocess
import time

from progress.bar import Bar
bar = Bar('Processing', max=20)
for i in range(20):
    # Do some work
    bar.next()
bar.finish()

filename = "volume-tag-creation-2016-12-26-12:49:36.sh"
input_file = open(filename, 'r')
count_lines = 0
for line in input_file:
	line = line.strip()
    	count_lines += 1
input_file.close()

filename = "volume-tag-creation-2016-12-26-12:49:36.sh"
input_file = open(filename, 'r')
bar = Bar('Processing', max=count_lines)
for line in input_file:
        line = line.strip()
#        print line
        subprocess.call(['/bin/bash', '-c', line])
	bar.next()
#	time.sleep(1)
bar.finish()
input_file.close()


print 'number of lines:', count_lines
