from collections import Counter
ll = []
word = "abbcccddddeeeeeffffffggggggghhhhhhhiiiiiiiijjjjjjjjjkkkkkkkkkk"
for i in word:
    ll.append((Counter(word)[i]))
for n in ((dict.fromkeys(ll))):
    print(n,end=",")