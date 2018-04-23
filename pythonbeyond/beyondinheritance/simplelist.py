"""
SimpleList class: Minimized version of List
"""


class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        """
        L.add(object) -> None -- append object to end
        """
        self._items.append(item)

    def __getitem__(self, index):
        """
        x.__getitem__(y) <==> x[y]
        """
        return self._items[index]

    def sort(self):
        """
        L.sort(key=None, reverse=False) -> None -- stable sort *IN PLACE*
        """
        return self._items.sort()

    def __len__(self):
        """
        Return len(self).
        """
        return len(self._items)

    def __repr__(self):
        """
        Return repr(self).
        """
        return "{}({!r})".format(self.__class__.__name__, self._items)


"""
SortedList class: Minimized version of List with inbuilt sorting mechanism
"""


class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()


"""
IntList class: Minimized version of List,allows only integers 
"""


class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items:
            self.validate(x)
        super().__init__(items)

    @staticmethod
    def validate(x):
        """
        Raises ValueError for non integers 
        """
        if not isinstance(x, (int)):
            raise ValueError("only integers are allowed")

    def add(self, item):
        self.validate(item)
        super().add(item)

class SortedIntList(IntList, SortedList):
    pass