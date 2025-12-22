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
history=[]
allowed=["obrisi","dodaj", "izlistaj", "stop","istorijat","obrisi sve",
         "prikazi najskuplji proizvod"]
question=None
while question not in allowed:
    question = input(f"sta zelite da uradite? {"/".join(allowed)}:\n").lower()
    if question=="obrisi":
        delete=input("koji proizvod zelite da obrisete?\n").lower()
        while delete not in products: #dokle god se ne unese tacan naziv prozivoda iz dictionary
            delete=input("koji proizvod zelite da obrisete?\n").lower() #ponavljamo upit korisniku
        del products[delete] #del-koristimo zabrisanje elemenata iz dictionary ili Array
        question = None
        msg=f"Obrisali ste proizvod: {delete}\n"
        print(msg)
        history.append(msg)
    elif question=="dodaj":
        add = None
        while add in products or add is None:
            add = input("Unesite ime proizvoda koje ne postoji:\n").lower()
        price=None
        while price is None or price<=0:
            price = int(input("upisati cenu:\n"))
        quant = None
        while quant is None or quant<0:
            quant=int(input("upisati kolicinu:\n"))
            products[add]={
                "cena":price,
                "kolicina":quant
            }
        question = None
        msg=f"Dodali ste novi proizvod: {add}\n"
        print(msg)
        history.append(msg)
    elif question=="izlistaj":
        print(products)
        question = None
    elif question=="istorijat":
        print(history)
        question = None
    elif question=="obrisi sve":
        products={}
        question = None
    elif question=="prikazi najskuplji proizvod" or "pnp":
        most_expensive_price=0 #najskuplja cena proizvoda kroz petlju iz Products dictionary
        most_expensive_item=None #najskuplji proizvod kroz petlju iz Products dictionary
        for items in products:
            if most_expensive_price<products[items]["cena"]:
                #ako je cena manja od cena item-a iz Products dictionary
                most_expensive_price=products[items]["cena"] #onda cena iz dict. postaje maks.cena
                most_expensive_item=items
        print(most_expensive_item,products[most_expensive_item]["cena"])
print(products)