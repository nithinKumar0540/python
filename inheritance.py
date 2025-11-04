'''
Inheritance allow us to define a class that inherits all the method  and properties from another class

parent class is the class inherited  from are also called Base Class

1) Single Inheritance
2) Multiple Inheritance
3) Multi Level Inheritance
4) Hierarchical Inheritance

'''
#Single Inheritance
class parent():
    a = 10
    def displayp(self):
        print("Im Parent")

class child1(parent):
    b = 20
    def displayc1(self):
        print("Im Child")

c = child1()
c.displayc1()
c.displayp()


