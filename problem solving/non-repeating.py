def first_non_repeating_letter(string):
    for letter in string:
        x = letter.lower()
        z = string.lower()
        if z.count(x) == 1:
            return letter
    return ''