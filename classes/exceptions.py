class NotEnoughSpace(Exception):
    def __str__(self):
        return "Недостаточно места, попробуйте что то другое"


class NoSuchProduct(Exception):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"На складе нет {self.__name}"


class BadStorageName(Exception):
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return f"Нет хранилища с именем - {self.__name}"


class BadUserRequest(Exception):
    def __str__(self):
        return "Неверный ввод"


class ToManyUniqProd(Exception):
    def __str__(self):
        return "В магазине храниться более 5 уникальных товаров"
