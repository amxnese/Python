def binary_search(num,lst_of_nums):
    mid = len(lst_of_nums)//2
    if lst_of_nums[mid] == num:
      return mid
    elif lst_of_nums[mid] > num:
      return mid-2 + binary_search(num,lst_of_nums[:mid])
    else:
      return  binary_search(num,lst_of_nums[mid:])
nums = [-4,-3,-2,-1,1,3,4,6,7,8,9,12,32,122,299]
print(binary_search(32,nums))