# ***********************************
# if _name_ == '__main__'
# ***********************************

#why tho?
# 1. Module can be run as a standalone program
#    or
# 2. Module can be imported and used by other modules

#  Python interpreter sets "special variables", one of which is _name_
#  Python will assign the _name_ variable a value of '__main__' if it's
#  the initial module being run

import module_two

def main():
    print("Hello!")

print(__name__) #the current module
print(module_two.__name__) #the module we are importing

if __name__ == '__main__':
    main()

# ***********************************
