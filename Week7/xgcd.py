def extended(a,b):
	s = 0
	old_s = 1
	t = 1
	old_t = 0
	r = b
	old_r = a
	
	while r != 0:
		quotient = old_r / r
		(old_r, r) = (r, old_r - quotient * r)
        	(old_s, s) = (s, old_s - quotient * s)
        	(old_t, t) = (t, old_t - quotient * t)

	print "Bezout coefficients:"
	print (old_s, old_t)
	print "greatest common divisor:"
	print old_r
	print "quotients by the gcd:"
	print t
	print s

space = 2 * "\n"

extended(57, 93)
print space
extended(357, 1234)
print space
extended(3125, 9987)
