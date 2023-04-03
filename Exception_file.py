# Exception is a base class for all errors, It is a predefined class
a, b, c = 0, 0, 0
try:
    # "120.50" eval() converts the string input to float value
    # "120.50" will be converted to float 120.50 by eval()
    a = eval(input("Enter a number:\t"))
    b = eval(input("Enter another number:\t"))
    c = a/b
except Exception as ex:
    print("ZeroDivisionError:\t", ex)
except ValueError as ex:
    print("ValueError:\t", ex)
finally:
    print("Finally........")

print(f"{a}/{b}={c}")
