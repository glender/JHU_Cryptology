from chi import chi
import random, string

chi = chi()
str = "This is a 123string that is definitely english WOAH"
chi.freq(str)
x = chi.chi()

print x
value = x
chi.clear()

for i in range(0,10):
    test = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(10))
    chi.freq(test)
    testValue = chi.chi()
    chi.clear()
    # we want the lowest possible chi-squared value
    if testValue <= value:
        value = testValue
        str = test

print value
print str
