#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import sys

n = 1

def gcd(a, b):
 
   while(b):
       a, b = b, a % b
 
   return a

def g(x):
	return (x**2 - 1) % n

x = 2
y = 2
d = 1

n = int(sys.argv[1])
iterations = 0

while d == 1:
	iterations += 1
	x = g(x)
	y = g(g(y))
	d = gcd(abs(x-y), n)

	if d == n:
		print "We failed!"
		exit()

print "Number of iterations: " + str((iterations-1))
print "Answer: " + str(d) + ", " + str(n/d)
