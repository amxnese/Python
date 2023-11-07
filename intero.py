''' l'intero '''
num = 0
while num < 2:
    num = int(input("enter a number:  "))
cmt = 2
somme = 3
produit = 1
while cmt <= num:
    produit *= somme
    somme += num
    cmt += 1
print(f"la valeur de E est:   {produit}")