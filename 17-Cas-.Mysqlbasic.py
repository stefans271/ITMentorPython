#install package PyMysql

import pymysql
connection=pymysql.connect(
    host='localhost',
    user='root',
    password='exoreus',
    db='python17'
)
if connection.open:
    print("Connected")
else:
    print("Connection failed")

#veza izmedju Pythona i Database
cursor=connection.cursor()
#dodaj 3 kolone u tabeli users preko Python konekcije "Cursor"
cursor.execute("INSERT INTO users(username,password,age) VALUES ('Admin','najbolji',18)")
connection.commit()
