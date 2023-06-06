#lambda function->function written in 1 line using lamba keyword accepts any number
#of arguements, but only has one express (think of it as a shotcut) (useful if needed for a short period of time throw away)
#labda parameters: expression

double = lambda x: x * 2
mutiplty = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first, last: f"My fullname is {first} {last}"
age_check = lambda age: True if age >= 18 else False

print(age_check(18))
print(full_name("fridah","watetu"))
print(double(8))
print(mutiplty(5,5))
print(add(10,20,12))