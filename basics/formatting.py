for i in range(1,11):
    print(f"{i:02}")
from math import pi
num = pi
print(f"{num:.4f}")
def series_resistance(lst):
	total = sum(lst)
	return '{} ohm{}'.format(total, 's' * (total > 1))

def stutter(word):
    if len(word) >= 2:
        two = word[:2]
        return "{}... {}... {}?".format(two,two,word)
print(stutter("incredible"))