# iz methods.py ucitaj funkciju load_file
from methods import load_file

products = load_file("data/products.json") #ucitavanje products fajla
users=load_file("data/user.json") #ucitavanje user fajla
print(products,users) #stampa oba fajla