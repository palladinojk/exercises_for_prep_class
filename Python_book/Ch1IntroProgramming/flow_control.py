#Exercises
# 1. False, True, 3, 3, False, True, False, False, False, True
#2.
#def even_or_odd(number):
#    if number % 2 == 0:
#        print('even')
#    else:
 #       print('odd')

# even_or_odd(5)
#3. Product 2 and Product not found!
#4. 
#if foo():
#    return 'bar'
#else:
#    return qux()
# 5. Empty
#6. 
# def string_function(word):
#    if len(word) > 10:
#        return word.upper()
#    else:
#        return(word)
    
# print(string_function('goodbye'))
# print(string_function('hello world'))
# 7. 

def amount(integer):
    if (integer >= 0) and (integer <= 50):
        print(f'{integer} is between 0 and 50.')
    elif (integer >= 51) and (integer <= 100):
        print(f'{integer} is between 51 and 100')
    elif integer > 100:
        print(f'{integer} is greater than 100.')
    else:
        print('The value is less than 0.')
amount(0)     # 0 is between 0 and 50
amount(25)    # 25 is between 0 and 50
amount(50)    # 50 is between 0 and 50
amount(75)    # 75 is between 51 and 100
amount(100)   # 100 is between 51 and 100
amount(101)   # 101 is greater than 100
amount(-1)    # -1 is less than 0
