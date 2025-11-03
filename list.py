"""
list []
allow changable data
allow to different datatype
allow to  duplicates
allow indexing and slicing

list methods:

append()
extend()
remove()
pop()
index()
count()
insert()

"""
a = [1,1,2,32.5, True, "Hello" ]
# print entire list
print(a)
# print what datatype
print(type(a))
# print 5 index value in list
print(a[5])
# print total list
print(a[::])
#print reverse index
print(a[::-1])
#print certain index eg from 0 to  5 last (n-1)
print(a[0:6:])
#print negative -1 to -5 and you also say the direction forword 1 or backword -1
print(a[-1:-5:-1])

#append #add one element
b = [1,1,2,2.5,True, "Hello", "Hi"]
b.append("Nithin")
b.append(23)
print(b)

#extend #add bulk element at a time
b.extend([14,46,"Siddhiksha","varansh","shivansh",46.9])
print(b)

#remove a element by value of list
b.remove(1)
b.remove(2.5)
print(b)

#pop remove element by index value
b.pop(7)
print(b)

#count
b.count("Hello")
print(b.count(1))
print(f" @@@@@@@@@ tha Value of a is : {a+b}")
print(f"the value of b is : {b}")


#index
print(b.index(23))

#insert()

b.insert(3,"Hiiiiiii")
print(f"aaaaaa : {b}")
