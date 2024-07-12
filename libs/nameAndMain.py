''' in Normal Cases, __name__ == __main__ , but when the module is imported
__name__ == the name of the module, "nameAndMain" in this case '''
if __name__ == "nameAndMain":
    print(r"You Imported The 'one' Module") # this get executed whenever this file is imported
print(__name__) # __main__