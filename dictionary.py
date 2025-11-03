'''
dict {k:v,k:v}

allow changes
allow different datatype
not allow duplicates keys and values are duplicates
not allow indexing and slicing

dict methods:
get()
update()
keys()
values()
items()
'''
a = {'p':123, "abc":123, 456:456, True:789}

#get()
print(a.get('p'))

#keys()
print(a.keys())

#values
print(a.values())

#items
print(a.items())

#update()
a.update({'star':"god","energy":"transfor"})
print(a)

for i in a:
    print(i)

print("----------")

for i, j in a.items():
    print(i,j)

print("----------")


