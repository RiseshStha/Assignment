# 1
# list1 = [22,2,3,3,111]
# print(min(list1))

#2
# empty_list = []
# def is_empty(my_list):
#     if len(my_list) == 0:
#         return "Empty"
#     else:
#         return "Not empty"
# print(is_empty(empty_list))

#3,4
# print(random.choice(list1))
# list2 = list1.copy()

#5
# second_Largest = [2,3,4,5,6,9,8,8,5]
# second_Largest.sort()
# print(max(second_Largest) -1)

#6
# def my_list(l):
#     a = []
#     x = [l[3]]
#     for i in l:
#         if i not in x:
#             a.append(i)
#         return a
# print(my_list([1,2,3,4,'putting',5,7]))

#7
# seriesOfNUmber = [1,2,3,4,5,5,6,7,8,9,10]
# even_count = 0
# odd_count = 0
# for i in seriesOfNUmber:
#     if i % 2 == 0:
#         even_count += 1
#     else:
#         odd_count += 1
# print(even_count)
# print(odd_count)

#8
# tuple_1 = (1,2,3,4,5,)
# converted_tuple = list(tuple_1)
# converted_tuple.append(33)
# tuple_2 = tuple(converted_tuple)
# print(tuple_2)

#9
# tuple_1 = (1,2,3)
# string2 = str(tuple_1)
# print(string2)
# print(type(string2))

#10
# a = [3,4,6,7,8]
# b = tuple(a)
# print(type(b))
# print(b)

#11
# a = [('Hari','Ram'),("age",42)]
# b = dict(a)
# print(b)

#12
# dict_1 = {1:1, 2:2,3:3}
# dict_2 = {11:11,22:22}
# dict_3 = {33:3,44:4}
# dict_1.update(dict_2)
# dict_1.update(dict_3)
# print(dict_1)

#13,14
# key_check_dict = {
#     'name': 'Risesh',
#     'age':19  
# }

#15
# if 'name' in key_check_dict:
#     print('Yes it is my name')
# else:
#     print('No it is my name')

#16
# square_dict = {}
# for i in range(1,17):
#     square_dict[i] = i**2

#17   
# first_dict = [1,2]
# second_dict = [3,4]
# first_dict.extend(second_dict)

#18
# third_largest_list = [1,3,5,3,89,9,7]
# third_largest_list.sort()
# print(third_largest_list[-3])

#19,20,21
# set_1 = {'a','b','c','d','e','f','g','h','i'}
# for j in set_1: # iterate mean loop
#     print(j)
# set_1.add("l")
# set_1.remove("a")
# set_1.discard('e')
# set_1.discard(set_1)
# print(set_1)

#22
# set_1 = {1,2,3,4,5}
# set_2 = {3,5,4,6,9}
# b = set_1.intersection(set_2)
# print(b)

# 23
# dict_1 = {'a':"B",'b':"B"}
# def key_present(x):
#     if x in dict_1:
#         print("key is present")
        
#     else:
#         print("Key not present")
# key_present('a')

# 26
# a = {1:11,2:22,3:33,4:44}
# if 44 in a.values():
#     print("present")
# else:
#     print("Not present")





    
    




