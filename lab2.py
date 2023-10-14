# # 1. Ratio
# num = int(input("Enter a four-digit number: "))
# digit_1 = num // 1000
# digit_2 = (num // 100) % 10
# digit_3 = (num // 10) % 10
# digit_4 = num % 10
# if digit_1 + digit_4 == abs(digit_2 - digit_3):
#     print("YES")
# else:
#     print("NO")


# # 2. Roskomnadzor
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("Access allowed")
# else:
#     print("Access denied")

# # 3. Arithmetic progression
# a = int(input())
# b = int(input())
# c = int(input())
# if b - a == c - b:
#     print("YES")
# else:
#     print("NO")

# # 4. Rook Move
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# if x1 == x2 or y1 == y2:
#     print("YES")
# else:
#     print("NO")

# # 5. King's Move🌶 ️
# x1 = int(input())
# y1 = int(input())
# x2 = int(input())
# y2 = int(input())
# dx = abs(x2 - x1)
# dy = abs(y2 - y1)
# if dx <= 1 and dy <= 1:
#     print("YES")
# else:
#     print("NO")

# # 6. Average number
# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# largest = max(num1, num2, num3)
# sum_of_largest_two = num1 + num2 + num3 - largest
# average = sum_of_largest_two / 2
# print(int(average))

# # 7. Number of days
# month = int(input())
# days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# print(days_in_month[month])

# # 8. Weigh-in ceremony
# weight = int(input())
# if weight <= 60:
#     category = "Light weight"
# elif weight <= 64:
#     category = "First welterweight"
# elif weight <= 69:
#     category = "Welterweight"
# else:
#     category = "Unknown category"
# print(category)

# # 9. Password
# password = input()
# confirmation = input()
# if password == confirmation:
#     print("Password accepted")
# else:
#     print("Password not accepted")

# # 10. Even or odd?
# number = int(input())
# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # 11. The smallest of two numbers
# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     smallest = num1
# else:
#     smallest = num2
# print(smallest)

# # 12. Age Group
# age = int(input())
# if age <= 13:
#     age_group = "childhood"
# elif 14 <= age <= 24:
#     age_group = "youth"
# elif 25 <= age <= 59:
#     age_group = "maturity"
# else:
#     age_group = "old age"
# print(age_group)

# # 13. Triangle view
# a = int(input())
# b = int(input())
# c = int(input())
# if a == b == c:
#     triangle_type = "Equilateral"
# elif a == b or b == c or a == c:
#     triangle_type = "Isosceles"
# else:
#     triangle_type = "Versatile"
# print(triangle_type)
