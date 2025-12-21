products={
    "hleb":{
        "cena":100,
        "kolicina":50
    },
    "pivo":{
        "cena":150,
        "kolicina":220
    }
}
question=None
while question not in ["obrisi","dodaj"]:
    question = input("sta zelite da uradite? obrisi/dodaj: ").lower()
if question=="obrisi":
    delete = None
    delete=input("koji proizvod zelite da obrisete? ").lower()
    while delete not in products: #dokle god se ne unese tacan naziv prozivoda iz dictionary
        delete=input("koji proizvod zelite da obrisete? ").lower() #ponavljamo upit korisniku
    del products[delete] #del-koristimo zabrisanje elemenata iz dictionary ili Array

elif question=="dodaj":
    add = None
    while add in products or add==None:
        add = input("Unesite ime proizvoda koje ne postoji: ").lower()
    price=input("upisati cenu: ")
    quantity=input("upisati kolicinu: ")
    products[add]={}
    products[add]["cena"]=price
    products[add]["kolicina"]=quantity
print(products)




