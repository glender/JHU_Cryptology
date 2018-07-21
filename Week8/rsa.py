#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

DEBUG = False

alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

message = ("6340 8309 14010")

for i in message.split():
	
	import numpy as np
	import math 

	i = int(i)

	# We need to solve the following system of equations 
	eq1 = "-26/676 * y - 1/676 * z + 1/676 * " + str(i)
	eq2 = "-676 / 26 * x - 1/26 * z + 1/26 * " + str(i)
	eq3 = "-676 * x - 26 * y + " + str(i)

	if DEBUG:
		print "Solving the following system of equations:"
		print eq1
		print eq2
		print eq3

	# Define x,y,z for our solution
	x = 1
	y = 1
	z = 1

	# Setup our np arrays to solve for x
	a = np.array( [ [-1 * x, -26/676 * y, -1/676 * z], [-676/26 * x, -1 * y, -1/26 * z], [-676 * x, -26 * y, -1 * z] ])
	b = np.array( [(-1 * i)/676, (-1 * i)/26, -1 * i] )
	ans = np.linalg.solve(a,b)
	x = math.floor(ans[0])

	# Setup our np arrays to solve for y
	a = np.array( [ [-1 * y, -1/26 * z], [-26 * y, -1 * z] ])
	b = np.array( [(-1 * i)/26 + ((676/26) * x), (-1 * i) + (676 * x)] )
	ans = np.linalg.solve(a,b)	
	y = math.floor(ans[0])

	# Solve for z since we know x and y already
	z = -676 * x - 26 * y + float(i)

	print alphabet[int(x)] + alphabet[int(y)] + alphabet[int(z)]
