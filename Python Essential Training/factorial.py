# Calculate factorial of a number

def factorial(num):

    if type(num) != int:
        print("Number is not an integer")
        return 0
    if num == 0:
        return 1
    if num < 0:
        print("Number cannot be negative")
        return 0

    result = 1
    while num >0:
        result = result * num
        num = num - 1
    return result


number = 2
result = factorial(number)
print("Result: ", result)

number = 0
result = factorial(number)
print("Result: ", result)

number = 1.5
result = factorial(number)
print("Result: ", result)

number = 5
result = factorial(number)
print("Result: ", result)

number = 10
result = factorial(number)
print("Result: ", result)