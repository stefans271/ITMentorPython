
books=[]
def add_book(book_name,book_author):
    books.append({"name":book_name,"author":book_author})

def find_book_by_name(name):
    for book in books:
        if book["name"] == name:
            return book

add_book("Harry Potter","J.K.Rowling")
add_book("Lord of the Rings","J.R.R.Talkin")
print(books)

book=find_book_by_name("Harry Potter")
print(book)
book=find_book_by_name("Harry Potte")
if book is None:
    print("Book not found")

def delete_book_by_name(book_name):
    book_found=find_book_by_name(book_name)
    if book_found is None:
        print("Book not deleted")
    else:
        books.remove(book_found)
        print("Book is deleted")

delete_book_by_name("Harry Potter")
delete_book_by_name("Harry Potte")