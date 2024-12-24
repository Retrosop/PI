class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"

class BookCollection:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration

# Пример использования
if __name__ == "__main__":
    # Создание экземпляров книг
    book1 = Book("1984", "George Orwell", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1122334455")

    # Создание коллекции книг
    collection = BookCollection()
    collection.add_book(book1)
    collection.add_book(book2)
    collection.add_book(book3)

    # Итерация по коллекции книг
    for book in collection:
        print(book)