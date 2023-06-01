# exceptions = events detected during execution that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("You cannt divide by zero")
    print(e)
except ValueError as e:
    print("You can only divide using numbers")
    print(e)
except Exception as e:
    print("something went wrong")
    print(e)
else:
    print(result)
finally:
    # everything in the finally block always executes
    # whether there is an error or not
    print("The finnaly cause")
