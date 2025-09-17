num_input = input("Give me a number : ")
num_float = float(num_input)
if num_float.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")