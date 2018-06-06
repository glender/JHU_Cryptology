#! /bin/python
__author__ = "glender"
__copyright__ = "Copyright (c) 2018 glender"
__credits__ = [ "glender" ]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "glender"
__email__ = "None"
__status__ = "Production"

import collections, string, re, math, textwrap
from collections import defaultdict

alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message= "KCCPKBGUFDPHQTYAVINRRTMVGRKDNBVFDETDGILTXRGUD DKOTFMBPVGEGLTGCKQRACQCWDNAWCRXIZAKFTLEWRPTYC QKYVXCHKFTPONCQQRHJVAJUWETMCMSPKQDYHJVDAHCTRL SVSKCGCZQQDZXGSFRLSWCWSJTBHAFSIASPRJAHKJRJUMV GKMITZHFPDISPZLVLGWTFPLKKEBDPGCEBSHCTJRWXBAFS PEZQNRWXCVYCGAONWDDKACKAWBBIKFTIOVKCGGHJVLNHI FFSQESVYCLACNVRWBBIREPBBVFEXOSCDYGZWPFDTKFQIYCWHJVLNHIQIBTKHJVNPIST"

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

# This function is from the following:
# https://stackoverflow.com/questions/18715688/find-common-substring-between-two-strings
def longestSubstringFinder(string1, string2):
    answer = ""
    len1, len2 = len(string1), len(string2)
    for i in range(len1):
        match = ""
        for j in range(len2):
            if (i + j < len1 and string1[i + j] == string2[j]):
                match += string2[j]
            else:
                if (len(match) > len(answer)): answer = match
                match = ""
    return answer

# This function is from the following: 
# https://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor 

def findKey(split, m):

    # Analyze sections separately.
    for sec in xrange(len(split)):
        section = split[sec]
        section_len = len(section)

        # Count letters.
        c = dict((key, 0) for key in alphaList)
        for char in section:
            c[char] += 1

        # Compute letter dispersion.
        dispersion = dict((key, float(c[key]) / section_len) for key in c)

        # Iterate over the letters in the alphabet
        gs = []
        for g in xrange(26):
            res = 0
            letter_g = alpha[g]
            for i in xrange(26):
		# get our probability of the letter happening in English
                p_i = alphaList[alpha[i]] / 100.0
		# get our probability
                h_ig = dispersion[chr(((i + g) % 26) + 65)]
                res += p_i * h_ig
            gs.append((letter_g, res))

        # Fetch best suiting value.
        desirable = .065
        nearest_value = 999
        nearest_index = 0
        for i, g in enumerate(gs):
            difference = abs(desirable - g[1])
            if difference < nearest_value:
                nearest_value = difference
                nearest_index = i
        yield gs[nearest_index][0]

def clearList():
	# clear the frequency list and results list
	for letter in alpha:
		freqList[letter] = 0
	
	for letter in alpha:
		resultsList[letter] = 0.0

def decrypt(message, word):
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

	return result

# Find the longest substring
result = longestSubstringFinder(message, message)

# Get possible key lengths
answer = [m.start() for m in re.finditer(result, message)]
x = int(answer[0])
y = int(answer[1])
distance = int(math.sqrt( ( (x-1) - (y-1) )**2 ))
possibleKeyLengths = list(divisorGenerator(distance))

# remove the possible key lengths that are too small or too big 
possibleKeyLengths.remove(1)
possibleKeyLengths.remove(distance)

print "Possible key lengths are:"
print possibleKeyLengths

# Split message into parts
split = defaultdict(list)
for i, char in enumerate(message.upper().replace(" ", "")):
	split[i % possibleKeyLengths[0]].append(char)

# attempt to find out key
KEY = ''.join(findKey(split, possibleKeyLengths[0]))

dec = decrypt(message, KEY)
clearList()
# count frequency
freq(dec)

# is the Chi Square value too high? 
if chi() > 50.0:
	# Split message into parts
	split = defaultdict(list)
	for i, char in enumerate(message.upper().replace(" ", "")):
	        split[i % (possibleKeyLengths[0]+1)].append(char)
	# is the key length one more?
	KEY = ''.join(findKey(split, possibleKeyLengths[0]+1)) 

clearList()
dec = decrypt(message, KEY)

# count frequency
freq(dec)

# is the Chi Square value too high? 
if chi() < 50.0:
	print KEY 
	print dec
