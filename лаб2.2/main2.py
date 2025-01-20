BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]

# TODO написать класс Book
class Book:
    """
    Класс, представляющий книгу.

    Атрибуты:
        id (int): Уникальный идентификатор книги.
        name (str): Название книги.
        pages (int): Количество страниц в книге.
    """

    def __init__(self, id_, name, pages):
        """
        Инициализация экземпляра книги.

        Параметры:
            id_ (int): Уникальный идентификатор книги.
            name (str): Название книги.
            pages (int): Количество страниц в книге.
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self):
        """
        Возвращает строковое представление книги для вывода.

        Возвращает:
            str: Строка, содержащая название книги.
        """
        return f'Книга "{self.name}"'

    def __repr__(self):
        """
        Возвращает неформальное представление книги для отладки.

        Возвращает:
            str: Строка с полями книги.
        """
        return f'Book(id_={self.id}, name={self.name!r}, pages={self.pages})'


# TODO написать класс Library
class Library:
    """
    Класс, представляющий библиотеку.

    Атрибуты:
        books (list): Список книг в библиотеке.
    """

    def __init__(self, books=None):
        """
        Инициализация экземпляра библиотеки.

        Параметры:
            books (list, optional): Список книг для инициализации библиотеки.
                По умолчанию - пустой список.
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self):
        """
        Возвращает следующий доступный идентификатор для новой книги.

        Возвращает:
            int: Следующий доступный идентификатор.
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, id_):
        """
        Возвращает индекс книги в списке по её идентификатору.

        Параметры:
            id_ (int): Идентификатор книги.

        Возвращает:
            int: Индекс книги в списке.

        Исключения:
            ValueError: Если книги с запрашиваемым идентификатором не существует.
        """
        for index, book in enumerate(self.books):
            if book.id == id_:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # проверяем индекс книги с id = 1
