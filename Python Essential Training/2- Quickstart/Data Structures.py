# Create a list and print length
my_list = [1,2,3,4]
print("Length of my_list:",(len(my_list)))
# Create a list of lists and print the length of the list
list_of_lists = [[],[],[],[]]
print("Length of list_of_lists:",len(list_of_lists))
# Create a set, read type, print
my_set = {1,2,3,4,5,6,7,8,9,10}
print("Type of my_set: ",type(my_set))
print("Length of my_set:",len(my_set))
print("my_set:",my_set)
# Equality testing
# These values are equal
print([1,2] == [1,2])
# These values are not equal
print([1,2] == [2,1])
# Create a tuple and print the length
my_tuple = [1,2,3]
print("Tuple length",len(my_tuple))
# Append to the list and print the completed list
my_list.append(6)
print(my_list)
# Create a dictionary
my_dictionary = {
        "apple":"A red fruit",
        "bear":"A scary animal"
    }
# Print the definition of the item called
print("Def of apple:",my_dictionary['apple'])
