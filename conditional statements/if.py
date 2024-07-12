is_tired = False
wants_to_work = False
if is_tired and wants_to_work:
  print("you should rest \nyour safety comes first")
elif wants_to_work and not is_tired:
  print("go bust your ass")
elif is_tired:
  print("get some rest")
elif not is_tired and not wants_to_work:
  print("you deserve a a day off")
else:
  print("go to work")