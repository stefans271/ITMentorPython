# 1)budzet
# 2)dodavanje troskova
# 3)brisanje troskova
# 4)logovanje troskova-napraviti tekstualni fajl "expense_log.txt"
#Upisati svaki trosak u formatu:Amount:Cifra, User:ID, DateTime,Budget: Trenutni, Preostali budget:
#prvo pravimo .json file i ovde dodajemo varijablu koja ce ucitati sta imamo u .json fajlu
#definisemo max.budget:ako korisnik ima vise od max.budgeta ili manje-jednako nuli-ispisati gresku
#dodajemo import sys , i nakon provere budgeta funkciju sys.exit() kako bi stopirali kod
#pravimo varijablu za trosak i while petlju sa upitom korisnika o troskovima(unos u minus znaku)
#u petlji dodajemo i uslov da varijabla za trosak ne sme biti veca od budzeta korisnika
#dodajemo novu varijablu za user_budzet, koja sadrzi zbir budzeta i kredita user-a

import json
import sys
from datetime import datetime

user=None
with open("data/user.json", "r")as file:
    user=json.load(file)
print(user)
max_budget=500000
user_budget=user["budget"]+user["credit"]

if user_budget>=max_budget or user_budget<=0:
    print("Neispravan iznos budgeta")
    sys.exit()
print(f"Vas budzet iznosi: {user_budget}")
expense=0
total_expense=0
while expense<=0 or expense>=user_budget:
    expense=int(input("Unesite trosak: "))
    total_expense+=expense
    if total_expense>user_budget:
        print("Nemate dovoljno novca!")
        break
    with open("logs/expense_log.txt", "a")as file:
        remainings=user_budget-total_expense
        message=(f"\nAmount:{expense}, "
             f" User:{user['id']}, "
             f" Budget:{user_budget}, "
             f" Preostali budzet:{remainings}, "
             f" DateTime:{datetime.now()}")
        file.write(message)
        expense=0








