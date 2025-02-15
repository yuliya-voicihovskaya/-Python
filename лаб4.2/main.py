class Vehicle:
    def __init__(self, make: str, model: str, year: int) -> None:
        """Инициализация базового класса Vehicle"""
        self.__make = make
        self.__model = model
        self.__year = year

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Vehicle"""
        return f"{self.__make} {self.__model} ({self.__year})"

    def __repr__(self) -> str:
        """Возвращает неформальное строковое представление объекта Vehicle"""
        return f"Vehicle(make={self.__make}, model={self.__model}, year={self.__year})"

    def get_make(self) -> str:
        """Метод для получения марки автомобиля"""
        return self.__make

    def get_model(self) -> str:
        """Метод для получения модели автомобиля"""
        return self.__model


class Car(Vehicle):
    def __init__(self, make: str, model: str, year: int, doors: int) -> None:
        """Инициализация дочернего класса Car, расширяет Vehicle"""
        super().__init__(make, model, year)
        self.doors = doors

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Car, улучшенное для добавления количества дверей"""
        return f"{super().__str__()} with {self.doors} doors"

    def drive(self) -> str:
        """Метод для имитации вождения автомобиля"""
        return f"The {self.get_make()} {self.get_model()} is driving."


if __name__ == "__main__":
    # Тестирование классов
    car1 = Car("Toyota", "Camry", 2022, 4)
    print(car1)  # Вывод: Toyota Camry (2022) with 4 doors
    print(repr(car1))  # Вывод: Vehicle(make=Toyota, model=Camry, year=2022)
    print(car1.drive())  # Вывод: The Toyota Camry is driving.