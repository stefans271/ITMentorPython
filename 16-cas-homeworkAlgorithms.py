#mali algoritam za proveru samo duplih cifara u nekoj listi:
numbers = [3,5,12,2,0,15,7,2,9,5,0]
checked = []  # novi niz za vec pregledane brojeve
duplicate = [] # lista sa dupliranim ciframa iz i-iteracije sa checked listom
for i in numbers:
    if i in checked:
        duplicate.append(i) #dodajemo nadjenu duplu cifru u duplicate listu
    else:
        checked.append(i) #ako cifra nije pronadjena tj nije dupla, onda je dodajemo u checked listu
print(f"Duplicates found:{duplicate}")