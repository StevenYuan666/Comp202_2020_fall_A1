# this is the program called even_and_positive in the instruction
# but for clearly show the number of the question, I use the name Q3 instead

# create a variable to store the value the user put in

input_value = int(input("please enter a number:"))

#evaluate the condition

is_even = (input_value % 2 == 0)
is_positive = input_value > 0

# display the info the input value

print(str(input_value) + ' is an even number :' + str(is_even))
print(str(input_value) + ' is a positive number :' + str(is_positive))
print(str(input_value) + ' is a positive number :' + str((is_even and is_positive)))
