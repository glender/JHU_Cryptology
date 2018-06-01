#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import collections, re

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message= "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUD DKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYC QKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRL SVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMV GKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFS PEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHI FFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"
letters = collections.Counter(message)

DICT_WORDS = open("/usr/share/wordlists/wfuzz/general/megabeast.txt").read().splitlines() 

word_file = "/usr/share/wordlists/rockyou.txt"
WORDS = open(word_file).read().splitlines()

total = len(message)
LETTER = 'A'

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
def chi():
        ret = 0.0
        for letter in alpha:
                e = ( alphaList[letter] / 100.0 * total )
                resultsList[letter] = ( freqList[letter] - e )**2 / e


        for letter in alpha:
                ret += resultsList[letter]

        return ret

# count the frequency
def freq(message):
        for letter in message:
		if letter != ' ':
                	freqList[letter] = freqList[letter] + 1

# Get our original frequency and Chi Statistic
freq(message)
CHI = chi()

for word in WORDS:
	# skip words that have digits in them
	if word.isdigit() or bool(re.search(r'\d', word)):
		continue
	result = ""
	count = 0
	maxAllowed = len(word)
	for l in message:
		# skip spaces
		if l.isspace():
			result += " "
			continue

		m_pos = alpha.index(l)
		holder = list(word)

		# don't process digits
		try:
			if holder[count].isdigit():
				break
		except IndexError:
			break

		try:
			w_pos = alpha.index(holder[count].upper()) 
		except ValueError:
			continue
		except IndexError:
			continue

		# using the key, create the output and store in result			
		count = (count + 1) % len(holder)
		new_pos = (m_pos - w_pos) % 26
		result += alpha[new_pos]

	# calculate the frequency and Chi Statistic
	freq(result)
        if chi() < CHI:
                CHI = chi()
                KEY = key = word
                DECRYPT = result

	# clear the frequency and results lists
        for letter in alpha:
                freqList[letter] = 0

        for letter in alpha:
                resultsList[letter] = 0.0

	# did we find a Chi Statistic that is relatively low? 
	if CHI < 50.0:
		print CHI
		print KEY.upper()
		print DECRYPT
		break
