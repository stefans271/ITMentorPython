import random
from datetime import date
from db import connection
from faker import Faker
faker = Faker()

genres=["Mystery","Adventure","Fantasy","Horror"]
adjectives=["Forgotten","Uncovered"]
nouns=["Secret","Castle","Isle"]

def generate_random_dob():
    return faker.date_between(start_date=date(1950,1,1), end_date=date(2000,1,1))

def generate_random_genre():
    return random.choice(genres)

def get_random_author():
    return faker.name()

def book_title(book_genre,book_author):
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    return f"{adjective} {noun}: A {book_genre} by {book_author}"

#insert_user, insert_book
def insert_user(con,name,birth_date):
    cursor = con.cursor()
    cursor.execute("INSERT INTO users (name,dob) VALUES (%s, %s)",(name,birth_date))
    con.commit()
    cursor.close()

def insert_book(con,name,book_genre,book_author):
    cursor = con.cursor()
    cursor.execute("INSERT INTO books (name,category,author) VALUES (%s, %s, %s)",(name,book_genre,book_author))
    con.commit()
    cursor.close()

dob=generate_random_dob()
genre=generate_random_genre()
author=get_random_author()
book=book_title(genre,author)
insert_user(connection,author,dob)
insert_book(connection,book,genre,author)
print(dob,genre,author,book)


