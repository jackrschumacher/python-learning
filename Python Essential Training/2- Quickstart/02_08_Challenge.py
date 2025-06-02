# Python code​​​​​​‌‌​‌​‌‌‌​​​‌​​‌​​‌‌‌‌‌​‌‌ below



def factorial(number):
    i = 0
    total_value = number
    # Your code goes here.
    # Need to check if the variable that is being passed in is a integer
    if type(number) == int and number >=0:
        # print("The value ",number," is an integer")
        if(number) == 0:
            return 1
        # There are 1 less factorials than the value of the number (ex. 5 has 4 factorials)
        else:
            while i < (number -1) :
                i +=1
                total_value = total_value * i
            return total_value

    else:
        print("The value ", number, " is not an integer. Please run the program and try again")
    pass
