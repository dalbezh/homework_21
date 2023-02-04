from classes.base import BaseStorage
from classes.exceptions import BadUserRequest, BadStorageName, ToManyUniqProd
from items import store_items, shop_items


class Store(BaseStorage):
    """
    Склад
    """
    name_storage = "склад"

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)


class Shop(BaseStorage):
    """
    Магазин
    """
    name_storage = "магазин"

    def __init__(self, items, capacity=100):
        super().__init__(items, capacity)

    def add(self, name: str, amount: int):
        """
        Добавлена проверка,
        что в магазине храниться меньше 5 уникальных товаров.
        """
        if self.get_unique_items_count() >= 5:
            raise ToManyUniqProd
        super().add(name, amount)


class Request:
    def __init__(self, request: str, storages):
        """
        Обработка запроса пользователя, который выглядит так:
        Доставить 3 шоколад из склад в магазин
        """
        user_request = request.lower().split(" ")
        if len(user_request) != 7 and "доставить" not in user_request:
            raise BadUserRequest

        self.amount = int(user_request[1])
        self.product = user_request[2]
        self.from_ = user_request[4]
        self.to = user_request[6]

        if self.from_ not in storages:
            raise BadStorageName(self.from_)
        elif self.to not in storages:
            raise BadStorageName(self.to)


def enum_quantity(storages):
    """
    Функция выводит содержимое склада и магазина
    (что-где находится)
    """
    for storage_name in storages:
        print(f"  В {storage_name} храниться:\n")
        for item in storages[storage_name].get_items():
            print(item)
        print("\n")


def main():
    store = Store(store_items)
    shop = Shop(shop_items)

    storages = dict(склад=store, магазин=shop)

    # для теста цикл реализован через for (количество итерация можно менять в range)
    for _ in range(3):
        user_input = input("Ваш запрос: ")
        request = Request(request=user_input, storages=storages)
        if request.from_ == "склад" and store.get_free_space() != 0:
            print("Нужное количество есть на складе")
            store.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} со {request.from_}")
            print(f"Курьер везёт {request.amount} {request.product} со {request.from_} в {request.to}")
            shop.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
            enum_quantity(storages)
        elif request.from_ == "магазин" and shop.get_free_space() != 0:
            print("Нужное количество есть в магазине")
            shop.remove(request.product, request.amount)
            print(f"Курьер забрал {request.amount} {request.product} со {request.from_}")
            print(f"Курьер везёт {request.amount} {request.product} со {request.from_} в {request.to}")
            store.add(request.product, request.amount)
            print(f"Курьер доставил {request.amount} {request.product} в {request.to}")
            enum_quantity(storages)


if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        print(ex)
