#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

# Elliptic curve class
class curve:

	# Init class
	def __init__(self, p, a, b):
		# y^2 = x^3 + a*x + b (mod p)
		self.p = p
		self.a = a
		self.b = b

	# Get the Z_value 
	def getOver(self):
		return self.p

	# Determine if point is on curve
	def isOnCurve(self, x, y):
		return (y * y - (x * x * x + self.a * x + self.b)) % self.p == 0

	# Calculate the value given 
	def calculateValue(self, x):
		return ( x**3 + (self.a * x) + self.b ) % self.p

c = curve(71, 1, 28)

for x in range(0, c.getOver()):
	val = c.calculateValue(x)
	stringy = ""
	stringy += "X: " + str(x) + ", x^3 + " + str(c.a) + " * x + " + str(c.b) + " mod " + str(c.p) + ": " + str(val)
	for t in range(0, c.getOver()):
		if c.isOnCurve(x,t):
			stringy += ", On Curve: (" + str(x) + ", " + str(t) + ")" 
	print stringy
