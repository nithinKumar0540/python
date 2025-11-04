#Multi level Inehritance
class grandparent():
    a = 10
    def displaygp(self):
        print("Im Grand Parent")

class parent(grandparent):
    b = 20
    def displayp(self):
        print("Im Parent")

class child(parent):
    c = 30
    def displayc(self):
        print("Im Child")

c1 = child()
c1.displayc()
c1.displayp()
c1.displaygp()
