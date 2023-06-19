class Book:
    def __init__(self, book_id, book_name, author_name):
        self.book_id = book_id
        self.book_name = book_name
        self.author_name = author_name
        pass
    pass

class Library:
    def __init__(self, book_list, library_addr):
        self.book_list = book_list
        self.library_addr = library_addr
        pass
    def get_author_book_count(self):
        author_book_count = dict(zip([i.author_name.upper() for i in self.book_list],[0 for i in self.book_list] ))
        for book in self.book_list:
            author_book_count[book.author_name.upper()] += 1
            pass
        return author_book_count
    def get_books(self):
        books = {}
        for book in self.book_list:
            books[book.book_id] = book.book_name
            pass
        return [i[1] for i in sorted(books.items(), reverse=True)]
    pass

def list_of_books_by_city(city_name, library_list):
    list_of_books = []
    k = 0
    for lib in library_list:
        if city_name.lower() == lib.library_addr['city'].lower():
            k = 1
            for k in lib.get_books():
                list_of_books.append(k)
                pass
            pass
        pass
    if k == 0:
        return None
    return list_of_books
    
if __name__=='__main__':
    lib_list = []
    for i in range(int(input())):
        book_list = []
        x = int(input())
        for j in range(x):
            book_list.append(Book(input(), input(), input()))
            pass
        library_addr = {'street': input(), 'area':input(),'city': input(), 'state': input(), 'zip': input()}
        lib_list.append(Library(book_list, library_addr))
        pass
    city_name = input()
    author_count = lib_list[0].get_author_book_count()
    book_list_by_city = list_of_books_by_city(city_name, lib_list)
    if len(author_count) > 0:
        for i in  author_count.items():
            print(i[0], i[1])
            pass
        pass
    if book_list_by_city == None:
        print("No Book Found")
        pass
    else:
        print(book_list_by_city)
        pass
    pass
