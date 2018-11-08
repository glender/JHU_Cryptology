# usage is test.py
# class chi calculates the Chi-Squared value for a given string
class chi:

    key="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total=0

    # stats for letters in english alphabet
    E = 12.02
    T = 9.10
    A = 8.12
    O = 7.68
    I = 7.31
    N = 6.95
    S = 6.28
    R = 6.02
    H = 5.92
    D = 4.32
    L = 3.98
    U = 2.88
    C = 2.71
    M = 2.61
    F = 2.30
    Y = 2.11
    W = 2.09
    G = 2.03
    P = 1.82
    B = 1.49
    V = 1.11
    K = 0.69
    X = 0.17
    Q = 0.11
    J = 0.10
    Z = 0.07

    alphaList = { 'A':A, 'B':B, 'C':C, 'D':D, 'E':E, 'F':F, 'G':G, 'H':H, 'I':I, 'J':J, 'K':K, 'L':L, 'M':M, 'N':N, 'O':O, 'P':P, 'Q':Q, 'R':R, 'S':S, 'T':T, 'U':U, 'V':V, 'W':W, 'X':X, 'Y':Y, 'Z':Z}
    
    freqList = { 'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
    
    resultsList = { 'A':0.0, 'B':0.0, 'C':0.0, 'D':0.0, 'E':0.0, 'F':0.0, 'G':0.0, 'H':0.0, 'I':0.0, 'J':0.0, 'K':0.0, 'L':0.0, 'M':0.0, 'N':0.0, 'O':0.0, 'P':0.0, 'Q':0.0, 'R':0.0, 'S':0.0, 'T':0.0, 'U':0.0, 'V':0.0, 'W':0.0, 'X':0, 'Y':0.0, 'Z':0.0}
    
    # calculate chi square
    def chi(self):
    	ret = 0.0
    	for letter in self.key:
    		e = ( self.alphaList[letter] / 100.0 * self.total )
    		self.resultsList[letter] = ( self.freqList[letter] - e )**2 / e
    			
    
    	for letter in self.key:
    		ret += self.resultsList[letter]
    
    	return ret
    
    # count the frequency 
    def freq(self, message):
        self.total=len(message)
    	for letter in message:
            # skip non-alpha
            if letter.upper() in self.key:
    	        self.freqList[letter.upper()] = self.freqList[letter.upper()] + 1


    # clear the frequency list and results list
    def clear(self):
	for letter in self.key:
	    self.freqList[letter] = 0
	
	for letter in self.key:
            self.resultsList[letter] = 0.0
