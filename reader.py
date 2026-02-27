# reader.py
class Reader:
    """Класс, представляющий читателя библиотеки"""
    
    def __init__(self, name, reader_id):
        self.name = name
        self.reader_id = reader_id
        self.borrowed_books = []
    
    def borrow_book(self, book):
        """Читатель берет книгу"""
        if book.is_available:
            self.borrowed_books.append(book)
            book.is_available = False
            return True
        return False
    
    def return_book(self, book):
        """Читатель возвращает книгу"""
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.is_available = True
            return True
        return False
    
    def __str__(self):
        books_count = len(self.borrowed_books)
        return f"Читатель: {self.name} (ID: {self.reader_id}), книг на руках: {books_count}"