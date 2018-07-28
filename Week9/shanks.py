#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import math

# class def for pairs
class pair:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def getX(self):
		return self.x
	
	def getY(self):
		return self.y


# function to calculate (a ^ b)%p 
def modRaisedByPower(a, b, p):
    	value = 1
  
	# find a mod p
    	a = a % p
    	while (b > 0):

    	    #for odd b multiply with a
    	    if b & 1:

    	        value = (value*a) % p

    	  
    	    b = b>>1
    	    a = (a*a) % p

    	return value


# function for shanks
def shanks(a, b, p):
	num = int (math.ceil(math.sqrt(p) + 1))

	value = list()

	for i in reversed(range(1, num)):
    		pa = pair(modRaisedByPower (a, i * num, p), i)
		value.append(pa)

	for j in range(0, num):

    	    	# collision check
    	    	cur = (modRaisedByPower (a, j, p) * b) % p

    	    	#if LHS is equal to RHS, collision occured
    	    	for x in value:

			if x.getX() == cur:

    	        		ans = x.getY() * num - j

    	        		#check whether answer is valid
    	        		if ans < p:
    	            			
					return ans


    	return -1


space = 2 * "\n"

a = 106
b = 12375
p = 24691	
print shanks(a, b, p)
print space
a = 6
b = 248388
p = 458009
print shanks(a, b, p)
print space
