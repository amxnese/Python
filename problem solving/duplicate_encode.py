def duplicate_encode(word):
    first_list = []
    final_result = []
    z = word.lower()
    for i in z:
        first_list.append(i)
    for n in x:
        if n in first_list:
            first_list.remove(n)
    for a in z:
        if a in first_list:
            final_result.append(")")
        else:
            final_result.append("(")
    return "".join(final_result)

def duplicate_encode(word):
    return "".join(["(" if word.lower().count(c) == 1 else ")" for c in word.lower()])

from collections import Counter
def duplicate_encode(word):
    return "".join(("(" if Counter(word)[i] == 1 else ")") for i in word.lower())
print(duplicate_encode("amiine"))