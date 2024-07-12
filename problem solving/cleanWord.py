def CleanWord(word):
    if len(word) == 1:
        return word
    if word[0] == word[1]:
        print(f"before return ==>  {word}")
        return CleanWord(word[1:])
    print(f"after return ==>  {word}")
    return word[0] + CleanWord(word[1:])
print(CleanWord("ppppyyyyyytttttthhhhhhooooooooonnnnnnnnnnn"))