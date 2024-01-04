lst = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
for i in range(len(lst)):
  print(f"\033[{31+i}mThis is {lst[i]} text\033[0m")
print("Back To Normal")