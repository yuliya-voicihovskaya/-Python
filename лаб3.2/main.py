class Book:
    """ Базовый класс для книг. """

    def __init__(self, name: str, author: str):
        """
        Инициализация книги.

        :param name: Название книги
        :param author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self):
        """ Получить название книги. """
        return self._name

    @property
    def author(self):
        """ Получить автора книги. """
        return self._author

    def __str__(self):
        """ Возвращает строковое представление книги. """
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        """ Возвращает формальное строковое представление книги. """
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """ Класс для бумажных книг. """

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация бумажной книги.

        :param name: Название книги
        :param author: Автор книги
        :param pages: Количество страниц в книге
        """
        super().__init__(name, author)
        self.pages = pages  # Вызов сеттера

    @property
    def pages(self):
        """ Получить количество страниц книги. """
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """
        Установить количество страниц книги.

        :param value: Количество страниц (положительное целое число)
        :raises ValueError: Если количество страниц не положительное или не целое
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество страниц должно быть положительным целым числом")
        self._pages = value

    def __str__(self):
        """ Возвращает строковое представление бумажной книги. """
        return f"Бумажная книга {self.name}. Автор {self.author}. Страниц: {self.pages}"


class AudioBook(Book):
    """ Класс для аудиокниг. """

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация аудиокниги.

        :param name: Название книги
        :param author: Автор книги
        :param duration: Длительность аудиокниги (в часах)
        """
        super().__init__(name, author)
        self.duration = duration  # Вызов сеттера

    @property
    def duration(self):
        """ Получить длительность аудиокниги. """
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Установить длительность аудиокниги.

        :param value: Длительность (положительное число)
        :raises ValueError: Если длительность не положительная
        """
        if not isinstance(value, (float)) or value <= 0:
            raise ValueError("Продолжительность должна быть положительным числом")
        self._duration = float(value)

    def __str__(self):
        """ Возвращает строковое представление аудиокниги. """
        return f"Аудиокнига {self.name}. Автор {self.author}. Длительность: {self.duration:.2f} часов"

# Пример использования
paper_book = PaperBook("1984", "Джордж Оруэлл", 328)
audio_book = AudioBook("Человек в высоком замке", "Филип К. Дик", 12.5)

print(paper_book)  # Бумажная книга 1984. Автор Джордж Оруэлл. Страниц: 328
print(audio_book)  # Аудиокнига Человек в высоком замке. Автор Филип К. Дик. Длительность: 12.50 часов