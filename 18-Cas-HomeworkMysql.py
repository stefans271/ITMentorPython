import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='exoreus',
    db='python17'
)
#definisemo Cursor zakonekciju:
#cursor=connection.cursor()
#pravimo funkciju za novog korisnika sa novim elementima (username,password,age)
def create_user(con,  username,password,age):
    cursor = con.cursor() #samo svoja konekcija-cursor nije za globalni connection,vec samo "con"
    #VARIJABLA ZA upisivanje vrednosti u date kolone za tabelu Users:
    query="INSERT INTO users(username,password,age) VALUES (%s,%s,%s)"
    cursor.execute(query,(username,password,age))
    con.commit()
    cursor.close()
create_user(connection,"Toma","123456789",32)
create_user(connection,"Koma","abcdef",22)