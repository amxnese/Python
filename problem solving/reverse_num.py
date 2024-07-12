def num_rev(number):
    Rev = 0
    while number:
        Rev *= 10
        Rev += number%10
        number //= 10
    return(Rev)