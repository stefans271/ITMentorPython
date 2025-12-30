import re
#proveriti preko RegEx da li je string email
email="toma@gmail.com"
#prvo proveriti teks sa \w, pa onda simbole \.- ,pa @, potom opet \w\.-,pa provera tacke \.,i potom reci \w
pattern=r"^[\w\-.]+@[\w\-.]+\.\w+$"
if re.match(pattern,email):
    print("Email address is valid")
else:
    print("Email address is invalid")
