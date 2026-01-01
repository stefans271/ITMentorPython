# pitati korisnika da doda proizvod, nakon unosa se proizvod dodaje u kasu,
#korisnik mora uneti total 3 proizvoda

cash_register=list()
#dok je broj unetih proizvoda u kasi manji od 3, pitati korisnika da unese novi proizvod
#kada korisnik unese roizvod, dodati ga u kasu.
while len(cash_register)<3:
    product=input("Enter the product name: ")
    cash_register.append(product)
    print(cash_register)

