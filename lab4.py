# # task 1.1
# user_input = input()
# tuple_result = tuple(user_input)
# print(tuple_result)

# # task 1.2
# tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
# print(*tuple, sep="")


# # task 1.3
# tuple_A = (1, 2, 3, 4, 5, 6, 7)
# tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
# half_A = tuple_A[:len(tuple_A)//2]
# half_B = tuple_B[len(tuple_B)//2:]
# result_tuple = half_A + half_B
# print(result_tuple)

# # task 1.4
# def povtorenie_count(input_tuple):
#     povtorenie = {}
#     for item in input_tuple:
#         if item in povtorenie:
#             povtorenie[item] += 1
#         else:
#             povtorenie[item] = 1
#     return [(key, value) for key, value in povtorenie.items()]

# input_tuple_1 = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)
# input_tuple_2 = ('55', '6', '777', 54, 6, 7777, 9, 777, 6)
# input_tuple_3 = ((1, 2, 3), (['A', 'B']), (1, 2, 3), (['A']))
# output_1 = povtorenie_count(input_tuple_1)
# output_2 = povtorenie_count(input_tuple_2)
# output_3 = povtorenie_count(tuple(map(tuple, input_tuple_3)))
# print(output_1)
# print(output_2)
# print(output_3)

# # task 1.5
# data_objects = (55, 6, 777, 70.0, '7', 'A')
# result_tuples = []
# int_temp_tuple = ()
# str_temp_tuple = ()
# float_temp_tuple = ()
# for item in data_objects:
#     if isinstance(item, (int)):
#         int_temp_tuple += (item,)
#     elif isinstance(item, float):
#         float_temp_tuple += (item,)
#     elif isinstance(item, str):
#         str_temp_tuple += (item,)
# result_tuples.append(int_temp_tuple)
# result_tuples.append(float_temp_tuple)
# result_tuples.append(str_temp_tuple)
# for t in result_tuples:
#     print(t)




# # task 2.1
# user_input = input()
# result_set = {char for char in user_input}
# print(result_set)

# # task 2.2
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}
# difference_set = set_A.symmetric_difference(set_B)
# print(difference_set)

# # task 2.3
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}
# print(f"{set_B - set_A}")


# # task 2.4
# set_A = {1, 2, 3, 4, 7}
# set_B = {8, 7, 9, 4, 2, 0, 10}
# set_C = {4, 0, 1}
# # 8, 7, 9, 4, 2, 0, 10, 1, 
# # for element in set_A:  
# #     if element in set_C:
# #         set_A.remove(element)
# #         set_B.add(element)
# set_D = set_A.intersection(set_C)
# set_B.update(set_D)
# print(set_B)


# # task 2.5
# import random
# A = {1, 2, 3, 4, 5, 6}
# n = 3
# m = 5
# result_list = []
# while len(result_list) < m:
#     uni_comb = set()
#     while len(uni_comb) < n:
#         element = random.choice(list(A))
#         uni_comb.add(element)
#     result_list.append(uni_comb)
# print(result_list)


# # task 3.1
# from itertools import groupby
# cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30'), ('Toyota', 'Camry 40')]
# sorted_cars_list = sorted(cars_list, key=lambda x: x[0])
# for manufacturer, group in groupby(sorted_cars_list, key=lambda x: x[0]):
#     models = [model for _, model in group]
#     print(f"{manufacturer} {len(models)}")
#     for model in models:
#         print(f"- {model}")





















# a = tuple('bat',)
# b = tuple('man',)
# print(f"\nTuple B = {b}")
# print(f'\nTuple A = {a}')

# a = set('bat')
# b = set('man')
# print(f"\nSet A = {a}"
#       f"\nSet B = {b}"
# f"\nUnion of sets A and B {a.union(b)}"
# f"\nDifference of sets A and B {a.difference(b)}"
# f"\nDifference of sets B and A {b-a}"
# f"\nIntersection of sets A and B {a.intersection(b)}"
# f"\nSymmetric difference of sets A and B {a.symmetric_difference(b)}")