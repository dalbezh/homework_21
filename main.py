from abc import ABC, abstractmethod


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

    def add(self, name, number):
        pass

    def remove(self, name, number):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Shop(Storage):
    """
    Магазин
    """
    def __init__(self, items, capacity=20):
        self._items = items
        self._capacity = capacity

    def add(self, name, number):
        pass

    def remove(self, name, number):
        pass

    def get_free_space(self):
        pass

    def get_items(self):
        pass

    def get_unique_items_count(self):
        pass


class Request:
    from_ = ""
    to = ""
    amount = 3
    product = "печеньки"

    @classmethod
    def set_from(cls, from_: str):
        cls.from_ = from_
        return cls.from_

    @classmethod
    def set_to(cls, to: str):
        cls.to = to
        return cls.to

    @classmethod
    def set_amount(cls, amount: int):
        cls.amount = amount
        return cls.amount

    @classmethod
    def set_product(cls, product: str):
        cls.product = product
        return cls.product



def main():
    store = Store('test')
    print(store)

    test_from = Request.set_from("склад")
    test_to = Request.set_to("магазин")

    print(f"{Request.to}, {Request.from_}, {Request.amount}, {Request.product}")


if __name__ == '__main__':
    main()
    