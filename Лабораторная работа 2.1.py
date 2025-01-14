import doctest
class Computer:
    def __init__(self, brand: str, ram: int, storage: int):
        """
        Создание объекта "Компьютер"

        :param brand: Бренд компьютера
        :param ram: Объем оперативной памяти в ГБ
        :param storage: Объем встроенной памяти в ГБ

        Примеры:
        >>> pc = Computer("Dell", 16, 512)
        """
        if not isinstance(brand, str):
            raise TypeError("Бренд должен быть строкой")
        if not isinstance(ram, int) or ram <= 0:
            raise ValueError("Объем оперативной памяти должен быть положительным целым числом")
        if not isinstance(storage, int) or storage <= 0:
            raise ValueError("Объем встроенной памяти должен быть положительным целым числом")

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def turn_on(self) -> None:
        """
        Включение компьютера.

        Примеры:
        >>> pc = Computer("Dell", 16, 512)
        >>> pc.turn_on()
        """
        ...
    def turn_off(self) -> None:
        """
        Выключение компьютера.

        Примеры:
        >>> pc = Computer("Dell", 16, 512)
        >>> pc.turn_off()
        """
        ...


class Fruit:
    def __init__(self, name: str, color: str, weight: float):
        """
        Создание объекта "Фрукт"

        :param name: Название фрукта
        :param color: Цвет фрукта
        :param weight: Вес фрукта в граммах

        Примеры:
        >>> apple = Fruit("Яблоко", "Красное", 150)
        """
        if not isinstance(name, str):
            raise TypeError("Название должно быть строкой")
        if not isinstance(color, str):
            raise TypeError("Цвет должен быть строкой")
        if not isinstance(weight, (int, float)) or weight <= 0:
            raise ValueError("Вес фрукта должен быть положительным числом")

        self.name = name
        self.color = color
        self.weight = weight


    def get_taste(self) -> str:
        """
        Получение вкуса фрукта.

        :return: Вкус фрукта

        Примеры:
        >>> apple = Fruit("Яблоко", "Красное", 150)
        >>> apple.get_taste()
        """
        ...
    def peel(self) -> None:
        """
        Очистка фрукта.

        Примеры:
        >>> apple = Fruit("Яблоко", "Красное", 150)
        >>> apple.peel()
        """
        ...


class Square:
    def __init__(self, side_length: float):
        """
        Создание объекта "Квадрат"

        :param side_length: Длина стороны квадрата

        Примеры:
        >>> square = Square(5)
        """
        if not isinstance(side_length, (int, float)) or side_length <= 0:
            raise ValueError("Длина стороны должна быть положительным числом")

        self.side_length = side_length

    def calculate_area(self) -> float:
        """
        Вычисление площади квадрата.

        :return: Площадь квадрата

        Примеры:
        >>> square = Square(4)
        >>> square.calculate_area()
        """
        ...
    def calculate_perimeter(self) -> float:
        """
        Вычисление периметра квадрата.

        :return: Периметр квадрата

        Примеры:
        >>> square = Square(4)
        >>> square.calculate_perimeter()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации