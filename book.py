# book.py
class Book:
    """Класс, представляющий книгу в библиотеке"""
    
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn
        self.is_available = True
    
    def __str__(self):
        status = "Доступна" if self.is_available else "Выдана"
        return f"'{self.title}' - {self.author} ({self.year}) [ISBN: {self.isbn}] - {status}"
    
    def get_info(self):
        """Возвращает информацию о книге"""
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
            'available': self.is_available
        }