from abc import ABC, abstractmethod

from classes.exceptions import NotEnoughSpace, NoSuchProduct


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


class BaseStorage(Storage):

    def __init__(self, items, capacity):
        self._items = items
        self._capacity = capacity

    def add(self, name, amount):
        """

        """
        if self.get_free_space() < amount:
            raise NotEnoughSpace

        if name in self._items:
            self._items[name] += amount

        else:
            self._items[name] = amount

    def remove(self, name, amount):
        """

        """
        if name not in self._items:
            raise NoSuchProduct(name)
        if self._items[name] < amount:
            raise NotEnoughSpace

        self._items[name] -= amount

        if self._items[name] == 0:
            self._items.pop(name)

    def get_free_space(self):
        """
        Считает свободное место
        """
        return self._capacity - sum(self._items.values())

    def get_items(self):
        """

        """
        items = [f"{item} - {amount}" for item, amount in self._items.items()]
        return items

    def get_unique_items_count(self):
        """

        """
        return len(self._items)
