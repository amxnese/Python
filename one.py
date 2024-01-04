''' in Normal Cases, __name__ == __main__ , but when the module is imported
__name__ == the name of the module, "one" in this case '''
if __name__ == "one":
    print(r"You Imported The 'one' Module") # this get executed whenever one.py is imported
print(__name__) # __main__