import string
x = string.ascii_letters + string.digits + string.punctuation + " "
print(x)

import string
print(string.digits)
print(string.ascii_letters)
print(string.ascii_lowercase)

import string
def find_missing_letter_in(giv_lett):
    letters = string.ascii_lowercase
    x = 0
    z = giv_lett[0]
    while letters[x] != z:
        x += 1
    xxx = 0
    while letters[x] == giv_lett[xxx]:
        xxx += 1
        x += 1
    else:
        print(f"the letter ({letters[x]}) is the missing letter")
find_missing_letter_in("abcdefgijk")
find_missing_letter_in("cdefghijklmnoqrs")