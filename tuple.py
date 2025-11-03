'''
tuple ()
not Allow changes
allow different datatype
allow duplicate datatype
allow index and slicing

min()
max()
sum()
len()

concatenation
iteration
repetation
membership operation in not in values
identity operation is is not variable
'''

t1 = (1,1,22,33,2.5,23,55,46,55)
print(f"the value is : {t1}")

#methods
print(f"minimum of t1 is : {min(t1)}")
print(f"maximum of t1 is : {max(t1)}")
print(f"sum of t1 is : {sum(t1)}")
print(f"lenth of the tuple is : {len(t1)}")

t2 = (22,14,20.21,15,14)
#concatenation
print(f"concatenation of t1 nad t2 is : {t1+t2}")

#iteration

for i in t1:
    for j in t2:
        print(i,j)
        print(i+j)

#repetation

print(f"repetation : {t1 * 10}")

#membership operation

print(f"check 5 is present in t1 : { 5 in t1}")

print(f'check 5 not present in t1 : {5 not in t1}')

#identity operation

print(f"check t1 and t2 are same : {t1 is t2}")
print(f'checking t1 and t2 are not equal : {t1 is not t2 }')






