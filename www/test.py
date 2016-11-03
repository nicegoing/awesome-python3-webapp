class A(dict):
    def __init__(self):
        super().__iter__()

    def print(self):
        print(self.__mappings__)