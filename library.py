# library.py
from book import Book
from reader import Reader

class Library:
    """Класс, управляющий библиотекой"""
    
    def __init__(self, name):
        self.name = name
        self.books = []
        self.readers = []
    
    def add_book(self, book):
        """Добавление книги в библиотеку"""
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку")
    
    def register_reader(self, reader):
        """Регистрация нового читателя"""
        self.readers.append(reader)
        print(f"Читатель {reader.name} зарегистрирован")
    
    def find_book(self, title):
        """Поиск книги по названию"""
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None
    
    def list_available_books(self):
        """Список доступных книг"""
        available = [book for book in self.books if book.is_available]
        return available
    
    def __str__(self):
        return f"Библиотека '{self.name}': {len(self.books)} книг, {len(self.readers)} читателей"