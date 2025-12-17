#list - varijabla slicna array-u
#  index     [0]               [1]
books=["Harry Poter 1", "LOTR Collection"]
#zamena prvog elementa iz liste
books[0] = "Orange"
print(f"Modified list: {books}")
#brisanje poslednje stavke iz liste
books.remove("LOTR Collection")
print(f"Modifikovana lista: {books}")