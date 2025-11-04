class display():
    def __init__(self, a, b):
        self.__a = a
        self._b = b
        print(self.__a)

class demo(display):
    def outout(self):
        print(self._b)

c = demo(15,23)
c.outout()

