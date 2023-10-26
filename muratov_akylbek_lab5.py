# # task 1.1
# user_input = input()
# user_input = user_input.lower()
# symbol_list = list(user_input)
# print(symbol_list)


# # task 1.2 
# symbol_list = ['a', 's', 'd', 'g', ' ', 'd', 's', 'j', 'h', 'd', 's', ' ', 'd', 's', 'j', 'f', 'h']
# symbol_counts = [(symbol, symbol_list.count(symbol)) for symbol in set(symbol_list)]
# print(symbol_counts)

# # task 1.3
# symbol_counts = [('h', 2), (' ', 2), ('g', 1), ('a', 1), ('s', 4), ('d', 4), ('j', 2), ('f', 1)]
# vowels = ['a', 'e', 'i', 'o', 'u']
# list_vow = [(symbol, count) for symbol, count in symbol_counts if symbol in vowels]
# list_cons = [(symbol, count) for symbol, count in symbol_counts if symbol.isalpha() and symbol not in vowels]
# list_sym = [(symbol, count) for symbol, count in symbol_counts if not symbol.isalnum()]
# print("list_vow =", list_vow)
# print("list_cons =", list_cons)
# print("list_sym =", list_sym)

# # task 1.4
# import math
# list_A = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
# list_A.sort()
# n = len(list_A)
# q1 = list_A[:n // 4]
# q2 = list_A[n // 4:n // 2]
# q3 = list_A[n // 2:3 * (n // 4)]
# q4 = list_A[3 * (n // 4):]
# if n % 4 != 0:
#     q1.extend([0] * (4 - n % 4))
# print("q1 =", q1)
# print("q2 =", q2)
# print("q3 =", q3)
# print("q4 =", q4)

# # task 2.1
# student_name = "Adam"
# assignment_scores = [82, 56, 44, 30]
# lab_scores = [78.20, 77.20]
# test_scores = [78, 77]
# student = {
#     'name': student_name,
#     'assignment': assignment_scores,
#     'test': test_scores,
#     'lab': lab_scores
# }
# print(student)

# # task 2.2
# student = {
#     'name': 'Adam',
#     'assignment': [82, 56, 44, 30],
#     'test': [78, 77],
#     'lab': [78.2, 77.2]
# }
# submitted_activities = len(student.get('assignment', [])) + len(student.get('lab', [])) + len(student.get('test', []))
# submission_check = {student['name']: submitted_activities}
# print(submission_check)

# # task 2.3
# student1 = {
#     'name': 'Adam',
#     'assignment': [82, 56, 44, 30],
#     'test': [78, 77],
#     'lab': [78.2, 77.2]
# }
# submission_rate = {'Adam': 8}
# if submission_rate.get(student1['name'], 0) >= 4:
#     final_grade = (
#         0.3 * sum(student1['assignment']) / len(student1['assignment']) +
#         0.5 * sum(student1['lab']) / len(student1['lab']) +
#         0.2 * sum(student1['test']) / len(student1['test'])
#     )
#     student1['final_grade'] = round(final_grade, 2)
# else:
#     student1['final_grade'] = 0
# print(student1)

# student2 = {
#     'name': 'Kevin',
#     'assignment': [82, 30],
#     'test': [],
#     'lab': [78.2]
# }
# submission_rate = {'Kevin': 3}
# if submission_rate.get(student2['name'], 0) >= 4:
#     final_grade = (
#         0.3 * sum(student2['assignment']) / len(student2['assignment']) +
#         0.5 * sum(student2['lab']) / len(student2['lab']) +
#         0.2 * sum(student2['test']) / len(student2['test'])
#     )
#     student2['final_grade'] = round(final_grade, 2)
# else:
#     student2['final_grade'] = 0
# print(student2)

# # task 2.4
# student1 = {
#     'name': 'Adam',
#     'assignment': [82, 56, 44, 30],
#     'test': [78, 77],
#     'lab': [78.2, 77.2],
#     'final_grade': 70.25
# }
# student2 = {
#     'name': 'Kevin',
#     'assignment': [82, 30],
#     'test': [],
#     'lab': [78.2],
#     'final_grade': 0
# }
# students = {student['name']: {k: v for k, v in student.items() if k != 'name'} for student in [student1, student2]}
# print(students)

# # task 3
# transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]
# stats = {}
# for user_id, transaction_type in transactions:
#     if user_id not in stats:
#         stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
#     stats[user_id][transaction_type] += 1
#     if stats[user_id]['mft'] is None or stats[user_id][transaction_type] > stats[user_id][stats[user_id]['mft']]:
#         stats[user_id]['mft'] = transaction_type
#     if (
#         stats[user_id]['lft'] is None or
#         (stats[user_id][transaction_type] < stats[user_id][stats[user_id]['lft']] or
#         (stats[user_id][transaction_type] == stats[user_id][stats[user_id]['lft']] and transactions.index((user_id, transaction_type)) < transactions.index((user_id, stats[user_id]['lft']))))
#     ):
#         stats[user_id]['lft'] = transaction_type
# print(stats)
