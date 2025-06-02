print("Example 1")
a = False
print("The value of A is:", a)
if a:
    print("A is true! \n")
else:
    print("A is false! \n")

print("Example 2")
a = True
b = True
c = True
print("A: ",a,"B: ",b,"C: ",c)
if a:
    print("A is True")
    if b:
        print("B is true")
        if c:
            print("C is true")
else:
    print("One of the values is false")
print("\n")

print("Example 3:Iterating and printing through a list \n")
test_list = [1,2,3,4,5]
for item in test_list:
    print(item)
print("Is the value 4 in the list?", 4 in test_list)

print("Example 4: While loops \n")
iterate = 0
while iterate <= 5:
    print(iterate)
    iterate += 1