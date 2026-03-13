# main.py
from book import Book
from reader import Reader
from library import Library

def main():
    # Создаем библиотеку
    library = Library("Городская библиотека №1")
    
    # Создаем книги
    book1 = Book("Война и мир", "Лев Толстой", 1869, "978-5-699-12045-7")
    book2 = Book("Преступление и наказание", "Федор Достоевский", 1866, "978-5-17-123456-7")
    book3 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, "978-5-389-09876-5")
    
    # Добавляем книги в библиотеку
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Регистрируем читателя
    reader = Reader("Иван Петров", "R001")
    library.register_reader(reader)
    
    # Демонстрация работы
    print("\n" + "="*50)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ БИБЛИОТЕКИ")
    print("="*50)
    
    print(f"\n{library}")
    
    print("\nДоступные книги:")
    for book in library.list_available_books():
        print(f"  - {book}")
    
    # Читатель берет книгу
    print(f"\n{reader.name} берет книгу '{book1.title}'")
    reader.borrow_book(book1)
    
    print("\nДоступные книги после выдачи:")
    for book in library.list_available_books():
        print(f"  - {book}")
    
    # Читатель возвращает книгу
    print(f"\n{reader.name} возвращает книгу")
    reader.return_book(book1)
    
    print("\nДоступные книги после возврата:")
    for book in library.list_available_books():
        print(f"  - {book}")

if __name__ == "__main__":
    main()