class parent():
    a = 10
    def displayp(self):
        print("I am parent")

class child1(parent):
    b = 20
    def displayc1(self):
        print("I am child 1")

class child2(parent):
    c = 30
    def displayc2(self):
        print("Im Child 2")

class child3(parent):
    d = 41
    def displayc3(self):
        print("Im Child 3")

e1 = child1()
e1.displayc1()


