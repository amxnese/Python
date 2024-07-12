# ord() Function, takes a character as an argument and returns its Unicode.
# char() Function, takes an integer representing a Unicode and returns the corresponding character.
alphabets = []
for i in range(ord('A'), ord('Z')+1):
  alphabets.append(chr(i))
print(alphabets) # prints out a list of the Uppercase alphatets