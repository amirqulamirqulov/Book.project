from models import Book_name, Book_type, Book
from windows.Book_name import*

# for book in Book_type.objects():
#     print(str(book.id))
#     print(str(book))

# rg = Book_type("86")
# rg.save()
# Book_type.delete(13)
# Book_type.print()

# rg.delete()

# Book_name("assalom", 56).save()
# # Book_name.print()

# for item in Book_name.objects():
#     print(item)

# Book_name.delete(16)
# Book_type.get_by_id(1)
# Book_name.delete(25)
# Book_name.delete(26)
# Book_name.delete(22)
# print(Book_type.get_by_id(1) is not None)

for item in Book.objects():
    print(item.Bookid)