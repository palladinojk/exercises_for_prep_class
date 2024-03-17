# 1. Error. It is outside scope.
# 2. Prints bar the global variable since shadowed.
#3. 
#def mult(a, b):
#   number = a * b
#   return number 

#def get_number(prompt):
#    entry = input(prompt)
#    return float(entry)

#first = get_number('Enter the first number:')
#second = get_number('Enter the second number:')
#amount = mult(first, second)
#print(f'{first} * {second} = {amount}')
# 4. Got mostly right with couple additions. Watched video too.
#5. Yipeee!!!! Actually, it does not print it.
#6. Nothing - Return value stops function
#7 Raise an error. It is expecting another argument for qux
#8. Raise an error.
#9. The three arguments rather than default values
# 10. 42, 3.141592, 2
#11 42, 3, 2
#12 error - expect first argument at least.
#13 error because default value needed after other one. 
# All subsequent parameters need default values.
#14 multiply, left, right, get_num, prompt, 
# first_number, product, multiply, second_number,
# float, input, print
#15 I got that one right.
#16  multiply (1,9), left (1), right (1)
#   get_num (4, 7, 8), prompt (4,5)
#   built-in functions float/input (5), print(10)
#17 function names are say. method names = .upper, .lower
#  built-in are max, print, input
#18. 
# def remainders_3(numbers):
#    return [number % 3 for number in numbers] 
# numbers_1 = [0, 1, 2, 3, 4, 5, 6]
# numbers_2 = [1, 2, 4, 5]
# numbers_3 = [0, 3, 6]
# numbers_4 = []
# print(any(remainders_3(numbers_1)))
# print(any(remainders_3(numbers_2)))
# print(any(remainders_3(numbers_3)))
# print(any(remainders_3(numbers_4)))
# 19. 
def remainders_5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))