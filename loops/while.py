MyFavoriteWebsites = []
MaximumWebs = 5
while MaximumWebs > 0:
    web = input("enter the website name without https://:     ")
    MyFavoriteWebsites.append(f"https://{web.lower().strip()}")
    print(MyFavoriteWebsites)
    MaximumWebs -= 1
    print(f"website added\n{MaximumWebs} places left")
else:
    print("bookmark is full, can't add more")
if len(MyFavoriteWebsites) > 0:
    MyFavoriteWebsites.sort()
    index = 0
    print("printing the list of websites in your bookmark")
    while index < len(MyFavoriteWebsites):
        print(MyFavoriteWebsites[index])
        index += 1