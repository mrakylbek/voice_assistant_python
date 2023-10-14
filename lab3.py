# # 1
# n = int(input())
# num = 2
# while num <= n:
#     print(num)
#     num += 2

# # 2
# n = int(input())
# fact = 1
# while n > 0:
#     fact *= n
#     n -= 1
# print(fact)

# # 3
# while True:
#     number = int(input())
#     if number == 42:
#         print()
#         break

# # 4
# input_string = input()
# count = 0
# for char in input_string:
#     if char == 'a' or char == 'A':
#         count += 1
# print(count)


# # 5
# num = int(input())
# sum_final = 0
# while num > 0:
#     digit = num % 10  
#     sum_final += digit
#     num //= 10 
# print(sum_final)

# # 6
# n = int(input())
# a = 0
# b = 1
# count = 0
# while count < n:
#     print(a)
#     c = a
#     a = b
#     b = c + b
#     count += 1

# # 7
# input_string = input()
# reversed_string = ""
# index = len(input_string) - 1 
# while index >= 0:
#     reversed_string += input_string[index]
#     index -= 1
# print(reversed_string)

# # 8
# sum_odd = 0
# while True:
#     num = int(input())
#     if num == 0:
#         break
#     if num % 2 == 0:
#         continue
#     sum_odd += num
# print(sum_odd)

# # 9
# import random
# target = random.randint(1, 100)
# while True:
#     guess = int(input())
#     if guess < target:
#         print("Too small")
#     elif guess > target:
#         print("Too large")
#     else:
#         print("Congratulations, you guessed it!")
#         break

# # 10
# input_string = input()
# is_palindrome = True
# left = 0
# right = len(input_string) - 1
# while left < right:
#     if input_string[left] != input_string[right]:
#         is_palindrome = False
#         break
#     left += 1
#     right -= 1
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# # 11
# X = float(input())
# Y = int(input())
# result = 1
# while Y > 0:
#     result *= X
#     Y -= 1
# print(result)

# # 12
# N = int(input())
# num = 2  
# while num <= N:
#     is_prime = True  
#     div = 2  
#     while div * div <= num:
#         if num % div == 0:
#             is_prime = False 
#             break
#         div += 1
#     if is_prime:
#         print(num)
#     num += 1

# # 13
# input_string = input()
# reversed_string = ""
# index = len(input_string) - 1 
# while index >= 0:
#     reversed_string += input_string[index]
#     index -= 1
# print(reversed_string)

# # 14
# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# num = int(input())
# while True:
#     if is_prime(num):
#         print(num)
#         break
#     else:
#         # print(num)
#         num += 1

# # 15
# def caesar_cipher(text, number):
#     enc_text = ""
#     for char in text:
#         if char.isalpha():
#             is_upper = char.isupper()
#             char_code = ord(char)
#             char_code = (char_code - 65 + number) % 26 + 65 if is_upper else (char_code - 97 + number) % 26 + 97
#             enc_text += chr(char_code)
#         else:
#             enc_text += char
#     return enc_text
# text = input("string: ")
# number = int(input("number: "))
# enc_text = caesar_cipher(text, number)
# print(enc_text)






















# # task 1.1
# user_input = input()
# tuple_result = tuple(user_input)
# print(tuple_result)

# # task 1.2
# input_tuple = ('T', 'h', 'e', 'B', 'i', 'g', 'B', 'e', 'n')
# result_string = ''.join(input_tuple)
# print("The tuple is:", input_tuple)
# print("The string is:", result_string)


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
# output_3 = povtorenie_count(input_tuple_3)
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
# result_set = set_A - set_B
# print(result_set)

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


# task 3.1
from itertools import groupby
cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]
sorted_cars_list = sorted(cars_list, key=lambda x: x[0])
for manufacturer, group in groupby(sorted_cars_list, key=lambda x: x[0]):
    models = [model for _, model in group]
    print(f"{manufacturer} {len(models)}")
    for model in models:
        print(f"- {model}")





















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