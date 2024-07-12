def find_binary(num,string):
    if num == 0:
      return string
    string = str(num%2) + string
    return find_binary(num//2,string)
for i in range(20):
    print(find_binary(i,''))