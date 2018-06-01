#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import textwrap

message="TGEEMNELNNTDROEOAAHDOETCSHAEIRLM"
m=[3,0,5,1,6,2,7,4]
key="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# split our messgae into strings of length 8
splits=textwrap.wrap(message, 8)

# iterate our split strings
for x in range(len(splits)):
	actual=['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
	holder = list(splits[x])
	# iterate over our pi method
	for index in range(8):
		# replace actual index with proper letter
		actual[m[index]] = holder[index]
	# replace our splits string with the decrypted message
	splits[x] = actual

# gather our string together for output
output = ""
for x in range(len(splits)):
	d_msg = "".join(splits[x])
	output += d_msg
print output
