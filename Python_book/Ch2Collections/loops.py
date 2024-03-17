#1. The loop never returns false with the condition.
# Needs an iterator for counter.
#2. 
#age = input("How old are you? ")
#print()
#print(f'You are {age} years old.')
#
#for duration in range(10, 50, 10):
#   print(f'In {duration} years, you will be {float(age) + float(duration)} years old.')
#   duration = float(duration) + 10
# 3. 
#my_list = [6, 3, 0, 11, 20, 4, 17]
#count = 0
#while count < len(my_list):
#    print(my_list[count])
#    count = count + 1
#print()
#for item in my_list:
#    print(item)
#4. 
#my_list = [6, 3, 0, 11, 20, 4, 17]
#count = 0
#while count < len(my_list):
#    if (my_list[count] % 2) == 0:
#        print(my_list[count])
#    count += 1
#print()
#for item in my_list:
#    if (item % 2) != 0:
#        print(item)
#5. 
#my_list = [
#    [1, 3, 6, 11],
#    [4, 2, 4],
#    [9, 17, 16, 0],
#]
#for item in range(0, len(my_list)):
#    list = my_list[item]
#    for number in list:
#        if number % 2 == 0:
#            print(number)
#6. 
#my_list = [
#    1, 3, 6, 11,
#    4, 2, 4, 9,
#    17, 16, 0,
#]
#odd_even = []
#for element in my_list:
#    if element % 2 == 0:
#        odd_even.append("even")
#    else:
#       odd_even.append("odd") 
#print(odd_even)
#7. 
#def find_integers(things):
#    return[element for element in things if type(element) is int]
#           
#my_tuple = (1, 'a', '1', 3, [7], 3.1415,
#            -4, None, {1, 2, 3}, False)
#
#integers = find_integers(my_tuple)
#print(integers)
#                  # [1, 3, -4]
#8.

# my_set = {
#     'Fluffy',
#     'Butterscotch',
#     'Pudding',
#     'Cheddar',
#     'Cocoa',
# }
# dictionary = {
#     str(element): len(element)
#     for element in my_set
#     if len(element) % 2 != 0
# }
# print(dictionary)
# {'Cocoa': 5, 'Pudding': 7, 'Cheddar': 7}
#9.
# def factorial(n):
#     result = 1
#     for number in range(n, 0, -1):
#         result *= number
#     return result

# print(factorial(1))   # 1
# print(factorial(2))   # 2
# print(factorial(3))   # 6
# print(factorial(4))   # 24
# print(factorial(5))   # 120
# print(factorial(6))   # 720
# print(factorial(7))   # 5040
# print(factorial(8))   # 40320
# print(factorial(25))  # 15511210043330985984000000   
# 10.
# import random

# highest = 10

# while True:
#     number = random.randrange(highest + 1)
#     print(number)
#     if number == highest:
#         break
#11.
# my_list = [
#   [1, 3, 6, 11],
#   [4, 2, 4],
#   [9, 17, 16, 0],
# ]
# number = 0
# while number < len(my_list):
#     counter = 0
#     while counter < len(my_list[number]):    
#         result = my_list[number][counter]
#         if result % 2 == 0:
#             print(result)
#         counter += 1
#     number += 1