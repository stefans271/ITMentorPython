
import json
import os

def load_file(file_name): #pozovemo load_file
    with open(file_name, "r") as file: #otvoriti file_name
        products=json.load(file) #pretvorice json podatke u dictionary
        return products #vraca podatke

def save_file(file_name,data):
    with open(file_name, "w") as file: #otvori fajl i upisi u njega
        json.dump(data,file,indent=4)

def delete_file(file_name):#pozvati funkciju delete_file zabrisanje fajla
    os.remove(file_name) #uradi remove fajla

def empty_file(file_name): #pozvati funkciju Epmty file
    save_file(file_name,"") #u funkciju Save file smo sacuvali prazan string-ispraznili sacuvano


