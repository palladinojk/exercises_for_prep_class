#1. The first is about whether the values they hold are
# the same. The second is whether they are the same
# object or not.
#2. yes. I believe it will. It will reflect the
# changes since they both point to the same location.
#3. This looks like the other example, but the dict constructor creates a 
# new object which means it does not change. It prints the original 
# content of 'The Life of Brian'
#4. dict() creates a shallow copy. Since these are
# mutable types, dict2 will reflect the change and 
# should be [1, 42, 3]
# 5. 
# import copy

# dict1 = {
#     'a': [[7, 1], ['aa', 'aaa']],
#     'b': ([3, 2], ['bb', 'bbb']),
# }

# dict2 = copy.deepcopy(dict1)

# # All of these should print False
# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])

# # All of these should print True

# print(dict1['a'][0][0] is dict2['a'][0][0])
# print(dict1['a'][0][1] is dict2['a'][0][1])
# print(dict1['a'][1][0] is dict2['a'][1][0])
# print(dict1['a'][1][1] is dict2['a'][1][1])
# print(dict1['b'][0][0] is dict2['b'][0][0])
# print(dict1['b'][0][1] is dict2['b'][0][1])
# print(dict1['b'][1][0] is dict2['b'][1][0])
# print(dict1['b'][1][1] is dict2['b'][1][1])
# 6. 
# dict1 = {
#     'a': [{7, 1}, ['aa', 'aaa']],
#     'b': ({3, 2}, ['bb', 'bbb']),
# }

# dict2 = dict(dict1)

# print(dict1         is dict2)
# print(dict1['a']    is dict2['a'])
# print(dict1['a'][0] is dict2['a'][0])
# print(dict1['a'][1] is dict2['a'][1])
# print(dict1['b']    is dict2['b'])
# print(dict1['b'][0] is dict2['b'][0])
# print(dict1['b'][1] is dict2['b'][1])