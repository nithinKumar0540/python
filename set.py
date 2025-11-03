'''
set {}

allow changes
allow differenr datatypes
Not allow duplicates
not allow indexing and slicing

set methods:
add()
update()
remove()
pop()

set operation
union()
intersection()
difference()
issubset()
issuperset()

'''
a = {1,1,2.3,True,'Hello',77}
print(a)
print(f'value of a is: {a}')

#add
a.add('Nithin')
print(a)
#remove
a.remove(77)
print(a)
#update()
a.update({12,14,15})
print(a)
#pop()
a.pop() # remove element randomely or first  element
print(a)

b = {1,2,3,4,5,6}
c = {4,5,6,7,8,9}
print(a | b)
print(a.intersection(b))
print(a & b)
print(a - b)
print(b-a)
print(a<=b)
print(a>=b)

