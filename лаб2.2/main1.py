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


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]

    for book in list_books:
        print(book)  # проверяем метод str

    print(list_books)  # проверяем метод repr
