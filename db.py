import pymysql
connection = pymysql.connect(host='localhost',user='root',password='exoreus',db='library',port=3306)
if connection.open:
    print("Connection established")