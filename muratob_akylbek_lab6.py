# # task 1
# fav_m = ["Irina Kairatovna", "Jah Khalib", "Raim", "Banapart"]
# for m in fav_m:
#     print(m)

# # task 2
# info = {
#     "height": "185 cm",
#     "fav color": "blue",
#     "fav actor": "Leonardo DiCaprio",
#     "fav sport": "basketball",
# }
# for key, value in info.items():
#     print(f"{key}: {value}")

# # task 3
# info = {
#     "height": "185 cm",
#     "fav color": "blue",
#     "fav actor": "Leonardo DiCaprio",
#     "fav sport": "basketball",
# }
# your_info = {}
# for key, value in info.items():
#     user_input = input(f"Enter your {key}: ")
#     your_info[key] = user_input
# print("Your information:")
# for key, value in your_info.items():
#     print(f"{key.capitalize()}: {value}")

# # task 4
# fav_songs = {
#     "Irina Kairatovna": ["Adjare Gudju", "5K", "Чина"],
#     "Jah Khalib": ["Stand Up", "Medina"],
#     "Beyoncé": ["Where are you", "Jol", "Жди звонка"],
# }

# # task 5
# def scrabble(word):
#     scores = {
#         'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#         'D': 2, 'G': 2,
#         'B': 3, 'C': 3, 'M': 3, 'P': 3,
#         'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#         'K': 5, 'J': 8, 'X': 8, 'Q': 10, 'Z': 10,
#         'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#         'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#         'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#         'Й': 4, 'Ы': 4,
#         'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#         'Ш': 8, 'Э': 8, 'Ю': 8,
#         'Ф': 10, 'Щ': 10, 'Ъ': 10
#     }
#     total_score = 0
#     for letter in word.upper():
#         total_score += scores[letter]
#     return total_score
# user_word = input("Enter word: ")
# score = scrabble(user_word)
# print(score)

# # task 6
# inventory = {
#     1: {"название": "книга", "цена": 1000, "количество": 100},
#     2: {"название": "ручка", "цена": 150, "количество": 200},
#     3: {"название": "бумага", "цена": 83, "количество": 50},
# }
# print(inventory)

# # task 7
# inventory = {
#     1: {"название": "книга", "цена": 1000, "количество": 100},
#     2: {"название": "ручка", "цена": 150, "количество": 200},
#     3: {"название": "бумага", "цена": 83, "количество": 50},
# }
# def update_inventory(inventory, item_id, quantity):
#     if item_id in inventory:
#         inventory[item_id]["количество"] += quantity
#         print(f"Количество товара с идентификатором {item_id} обновлено на {quantity}.")
#     else:
#         print(f"Товар с идентификатором {item_id} отсутствует в инвентаре.")
# update_inventory(inventory, 2, 50)
# print(inventory)  

# # task 8
# inventory = {
#     1: {"название": "книга", "цена": 1000, "количество": 100},
#     2: {"название": "ручка", "цена": 150, "количество": 200},
#     3: {"название": "бумага", "цена": 83, "количество": 50},
# }
# def total_inventory_value(inventory):
#     total_value = 0
#     for item_id, item_info in inventory.items():
#         price = item_info["цена"]
#         quantity = item_info["количество"]
#         total_value += price * quantity
#     return total_value
# total_value = total_inventory_value(inventory)
# print(f"Общая стоимость товаров на складе: {total_value} денежной единицы.")

# # task 9
# inventory = {
#     1: {"название": "книга", "цена": 1000, "количество": 100},
#     2: {"название": "ручка", "цена": 150, "количество": 200},
#     3: {"название": "бумага", "цена": 83, "количество": 50},
#     4: {"название": "книга", "цена": 1000, "количество": 100},
# }
# def find_item_by_name(inventory, name):
#     matching_ids = []
#     for item_id, item_info in inventory.items():
#         if item_info.get("название") == name:
#             matching_ids.append(item_id)
#     return matching_ids
# item_name = "книга"
# matching_items = find_item_by_name(inventory, item_name)
# if matching_items:
#     print(f"Товары с названием '{item_name}' имеют идентификаторы: {matching_items}")
# else:
#     print(f"Товары с названием '{item_name}' не найдены.")

# # task 10
# inventory = {
#     1: {"название": "книга", "цена": 1000, "количество": 100},
#     2: {"название": "ручка", "цена": 150, "количество": 200},
#     3: {"название": "бумага", "цена": 83, "количество": 50},
# }
# sales = {
#     1: 30,
#     2: 20,
#     3: 10
# }
# for item_id, sold_quantity in sales.items():
#     if item_id in inventory:
#         inventory[item_id]["количество"] -= sold_quantity
# for item_id, item_info in inventory.items():
#     print(f"Товар с идентификатором {item_id}: {item_info['название']} - Остаток: {item_info['количество']}")

# # task 11
# def get_result(input_list, n):
#     counts = {}
#     for el in input_list:
#         if el in counts:
#             counts[el] += 1
#         else:
#             counts[el] = 1
    
#     top_n = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True)[:n])
#     return top_n
# my_list = [1, 2, 2, 3, 3, 3, 'apple', 'apple', 'banana', 'banana', 'banana', 'cherry']
# N = 3
# result = get_result(my_list, N)
# print(result)

# # task for 100
# nested_dict = {
#     'y': 1,
#     'z': {
#         'f': 2,
#         'k': {
#             'l': 3
#         }
#     }
# }
# def flatten_dictionary(nested_dict, parent_key='', sep='_'):
#     items = []
#     for key, value in nested_dict.items():
#         new_key = parent_key + sep + key if parent_key else key
#         if isinstance(value, dict):
#             items.extend(flatten_dictionary(value, new_key, sep=sep).items())
#         else:
#             items.append((new_key, value))
#     return dict(items)
# flattened_dict = flatten_dictionary(nested_dict)
# print(flattened_dict)
