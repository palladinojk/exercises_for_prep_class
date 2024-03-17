# Exercises
#1.
# this_range = range(0, 25, 3)
# print(this_range[6])
#2.
# text = 'Launch School'
# print(text[4:10])
#3.
# text = (1, 2, 3, 4, 5)
# text_back = list(reversed(text))
# print(tuple(text_back[1:len(text_back)-1]))
# looks like they wanted me to mutate the list 
# I thought they wanted a new list/object
#4. Dictionary
#pets = {
#  'Cat':  'Meow',
#  'Dog':  'Bark',
#    'Bird': 'Tweet',
#}
#print(pets['Dog'])
#Lizard = pets.keys()
#if 'Lizard' in Lizard:
#    print(pets['Lizard'])
#else:
#    print('None')
#    print('<silence>')
#print(pets.get('Lizard', 'None and <silence'))      # 100
# 5. The mutable items don't work as keys.
# the list, the dict, and the set are mutable.
# 6. False, false, false, false, false, true, true,
# false, false, false, false
#7. 
#info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
#list_info = list(info)
#for char in range(0, len(list_info)):
#   if list_info[char] == ":":
#        list_info[char] = '+'
#   else:
#        continue
#my_string = ''.join(list_info)
#print(my_string)
#info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
#result = info.replace(':', '+')
#print(result)
# 8. The first is finding f in the shortened string
# The second is using is using the method on the full string
# 9. 
# stuff = [
#    ['hello', 'world'],
#    ['example', 'mem', None, 6, 88],
#    [4, 8, 12],
#]
# stuff[1][3] = 606
# print(stuff)
# 10. print(cats['Pete']['Cocoa']['enjoys'])
#11. false, true, true, false, true, false, false,
# true, false, true
#numbers1 = [1, 3, 5, 7, 9, 11]
#numbers2 = []
#numbers3 = [2, 4, 6, 8]
#numbers4 = ['1', '3', '5']
#numbers5 = ['1', 3.0, '5']
#print(3 in numbers1)
#print(3 in numbers2)
#print(3 in numbers3)
#print(3 in numbers4)   
#print(3 in numbers5)
#13. the tuple, true, false, true, false
# 14. 
#my_str = 'abc'
#my_list = ['Alpha', 'Bravo', 'Charlie']
#my_tuple = (None, True, False)
#my_range = range(10, 60, 10)
#whole = zip(my_str, my_list, my_tuple, my_range)
#print(list(whole))
# 15. dict_keys(['Cat', 'Bird', 'Snake'])