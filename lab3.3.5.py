class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if self.head is None:
            self.head = self.tail = obj
        obj.set_prev(self.tail)
        self.tail.set_next(obj)
        self.tail = obj

    def remove_obj(self, indx):
        pass

    def __len__(self):
        return 0 if not self.tail.get_id() else self.tail.get_id() + 1

    def __call__(self, indx):
        n = self.head
        while n.get_id() != indx:
            n = n.get_next()
        return n.get_data()


class ObjList:
    ID = 0

    def __init__(self, data):
        self.__id = ObjList.ID
        self.__data = data
        self.__prev = None
        self.__next = None
        ObjList.ID += 1

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def get_data(self):
        return self.__data

    def get_id(self):
        return self.__id