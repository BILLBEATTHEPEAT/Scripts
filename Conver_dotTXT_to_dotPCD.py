# Reference: http://blog.csdn.net/qq_15332903/article/details/54089161

##########
# This is a simple script works to convert point cloud data from the .txt format to .pcd format.
# Characteristic: 1. No need for specific .pcd package; 
#				  2. Work faster then using file.open() when dealing with large dataset (more than 10M);
#				  3. The header of the .pcd can be modified.
#
########### 


#coding:utf-8

import time, re, linecache
import pandas as pd
import numpy as np
from sys import argv

script, filename = argv
print "The input filename is:%r." % filename

start = time.time()
print "Open the file..."
f = pd.read_csv(filename, header = None)


count = f.shape[0] # get the point number


f_prefix = filename.split('.')[0]
output_filename = '{prefix}.pcd'.format(prefix=f_prefix)
output = open(output_filename, "w+")

list = ['# .PCD v0.7 - Point Cloud Data file format\n',
			'VERSION 0.7\n',
			'FIELDS x y z\n',
			'SIZE 4 4 4\n',
			'TYPE F F F\n',
			'COUNT 1 1 1\n']

output.writelines(list)
output.write('WIDTH ')
output.write(str(count))
output.write('\nHEIGHT ')
output.write(str(1))
output.write('\nVIEWPOINT 0 0 0 1 0 0 0')
output.write('\nPOINTS ')
output.write(str(count))
output.write('\nDATA ascii\n')

f = np.array(f)
for line in f:
	point = str('')
	for coor in line:
		point += str(coor)
		point += ' '
	point += '\n'
	output.write(point)


output.close()

end = time.time()
print "points: ", count
print "run time is: ", end-start
