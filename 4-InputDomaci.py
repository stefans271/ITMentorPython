price_bag=int(input("Dodaj cenu korpe: "))
tax_percentage=10
if price_bag<0:
    print("Pogresan unos!")
    quit()

if price_bag>=1000:
    tax=price_bag*tax_percentage/100
    print(f"Ostvarili ste 10% popusta, sto iznosi {tax} eura")
else:
    print(f"Vasa korpa iznosi {price_bag} eura")
