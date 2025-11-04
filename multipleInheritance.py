"""
multiple Inheritance
"""
class parent1():
    a = 10
    def displayp1(self):
        print("Im Parent 1")

class parent2():
    b = 20.2
    def displayp2(self):
        print("Im Parent 2")

class parent3():
    c = 30.2
    def displayp3(self):
        print("Im Parent 3")

class child(parent1,parent2,parent3):
    d = 41
    def displayc(self):
        print("Im Child")
c1 = child()
c1.displayc()
c1.displayp1()
c1.displayp2()
c1.displayp3()


