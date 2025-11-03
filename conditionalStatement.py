'''
if condition:           (*) # in if condition true then print
    statement
elif condition:
    statement
elif condition:
    statement
else:
    statement
-------------------------------------
Nested if:
---------
if condition:           True it also check nested if
    statement
    if condition:       (*) in nested if condition is true
        statement
    else:
        statement
else:
    statement

----------------------------------------
#nested if
if True:
    print("Im Outer If")
    if True:
        print("Im Inner If")
    else:
        print("Im Inner else")
else:
    print("Outer If")

--------------------------------------

'''

age = int(input("Enter your age : "))
if age  > 58:
    print("you will get pension")

elif age == 58:
    print("You are elgible to get pension")

else:
    print("Wait till your age is 58")


