#reduce() = apply a function to an iterable and reduce it to a single cumulative value
#performs function on first two elements and repeats process until 1 value remains

#reduce(function, iterable)
import functools

#EXAMPLE ONE

numbers = [20, 45, 12, 45, 78, 45]
addition = lambda data,sum: sum + data
result = functools.reduce(addition, numbers)
print(result)

#EXAMPLE TWO

letters = ["H", "E", "L", "L", "0"]
join_letters = lambda word, letter: word + letter
full_word = functools.reduce(join_letters, letters)
print(full_word)

#EXAMPLE THREE
factorial = [5, 4, 3, 2, 1]
result =functools.reduce(lambda x, y: x * y, factorial)
print(result)