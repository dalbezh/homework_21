from abc import ABC, abstractmethod

from items import store_items, shop_items


class Storage(ABC):
    @abstractmethod
    def add(self, name: str, number: int):
        pass

    @abstractmethod
    def remove(self, name: str, number: int):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    """
    Склад
    """
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):
        if self.get_free_space() < amount:
            raise NotEnouthSpace

        if name in self._items:
            self._items[name] += amount

        else:
            self._items[name] = amount


    def remove(self, name, amount):
        if name not in self._items or self._items[name] < amount: # вот это надо разобрать !!!
            raise NotEnouthSpace

        self._items[name] -= amount

        if self._items[name] == 0:
            self._items.pop(name)


    def get_free_space(self):
        """
        Считает свободное место
        """
        return self._capacity - sum(self._items.values())

    def get_items(self):
        items = [f"{item} - {amount}" for item, amount in self._items.items()]
        return items

    def get_unique_items_count(self):
        return len(self._items)


class Shop(Storage):
    """
    Магазин
    """
    def __init__(self, items, capacity=100):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):
        if self.get_unique_items_count() >= 5: # проверка, что в магазине храниться меньше 5 уникальных товаров.
            raise ToManyDiffProd

        if self.get_free_space() < amount:
            raise NotEnouthSpace

        if name in self._items:
            self._items[name] += amount

        else:
            self._items[name] = amount


    def remove(self, name, amount):
        if name not in self._items or self._items[name] < amount: # вот это надо разобрать !!!
            raise NotEnouthSpace

        self._items[name] -= amount

        if self._items[name] == 0:
            self._items.pop(name)


    def get_free_space(self):
        """
        Считает свободное место
        """
        return self._capacity - sum(self._items.values())

    def get_items(self):
        items = [f"{item} - {amount}" for item, amount in self._items.items()]
        return items

    def get_unique_items_count(self):
        return len(self._items)


class Request:
    def __init__(self, request: str, storages):
        """
        Обработка запроса пользоватля, который должeн выглядеть так:
        Доставить 3 печеньки из склад в магазин
        """
        user_request = request.lower().split(" ")
        if len(user_request) != 7 and "доставить" not in user_request:
            raise BadRequest

        self.amount = int(user_request[1])
        self.product = user_request[2]
        self.from_ = user_request[4]
        self.to = user_request[6]

        if self.from_ not in storages or self.to not in storages: # а оно тебе надо браток
            raise BadStorageName




def main():
    store = Store(store_items)
    shop = Shop(shop_items)

    storages = {
        "склад": store,
        "магазин": shop
    }


    for _ in range(1): 
        for storage_name in storages:
            print(f"В {storage_name} храниться:\n")
            for item in storages[storage_name].get_items(): 
                print(item)
            print("\n")

        user_input = input("Ваш запрос: ")

        request = Request(request=user_input, storages=storages)
        # Доставить 3 печеньки из склад в магазин


if __name__ == '__main__':
    main()
