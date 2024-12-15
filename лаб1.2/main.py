# TODO Написать 3 класса с документацией и аннотацией типов

class Book:
    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Заголовок книги (должен быть строкой).
        :param author: Автор книги (должен быть строкой).
        :param pages: Количество страниц в книге (должен быть > 0).

        :raises ValueError: Если pages <= 0.

        >>> book = Book('1984', 'Джордж Оруэлл', 328)
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")

        self.title = title
        self.author = author
        self.pages = pages

    def get_info(self) -> str:
        """
        Получение информации о книге.

        :return: Строка с заголовком и автором.

        >>> book = Book('1984', 'Джордж Оруэлл', 328)
        >>> book.get_info()
        '1984, автор: Джордж Оруэлл'
        """
        return f"{self.title}, автор: {self.author}"


class Laptop:
    def __init__(self, brand: str, model: str, ram: int):
        """
        Инициализация ноутбука.

        :param brand: Бренд ноутбука (должен быть строкой).
        :param model: Модель ноутбука (должен быть строкой).
        :param ram: Объем оперативной памяти в гигабайтах (должен быть > 0).

        :raises ValueError: Если ram <= 0.

        >>> laptop = Laptop('Dell', 'XPS 13', 16)
        """
        if ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть больше 0.")

        self.brand = brand
        self.model = model
        self.ram = ram

    def get_specs(self) -> str:
        """
        Получение характеристик ноутбука.

        :return: Строка с брендом, моделью и объемом RAM.

        >>> laptop = Laptop('Dell', 'XPS 13', 16)
        >>> laptop.get_specs()
        'Dell XPS 13, RAM: 16 GB'
        """
        return f"{self.brand} {self.model}, RAM: {self.ram} GB"


class Phone:
    def __init__(self, brand: str, model: str, storage: int):
        """
        Инициализация телефона.

        :param brand: Бренд телефона (должен быть строкой).
        :param model: Модель телефона (должен быть строкой).
        :param storage: Объем памяти в гигабайтах (должен быть > 0).

        :raises ValueError: Если storage <= 0.

        >>> phone = Phone('Apple', 'iPhone 13', 128)
        """
        if storage <= 0:
            raise ValueError("Объем памяти должен быть больше 0.")

        self.brand = brand
        self.model = model
        self.storage = storage

    def make_call(self, number: str) -> None:
        """
        Совершение звонка на указанный номер.

        :param number: Номер для звонка (должен быть строкой).

        >>> phone = Phone('Apple', 'iPhone 13', 128)
        >>> phone.make_call('+1234567890')
        """
        print(f"Звонок на номер {number}")

    def get_storage(self) -> int:
        """
        Получение объема памяти телефона.

        :return: Объем памяти в гигабайтах.

        >>> phone = Phone('Apple', 'iPhone 13', 128)
        >>> phone.get_storage()
        128
        """
        return self.storage


if __name__ == "__main__":
# TODO работоспособность экземпляров класса проверить с помощью doctest
    import doctest
    doctest.testmod()

