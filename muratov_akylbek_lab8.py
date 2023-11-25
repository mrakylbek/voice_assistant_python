# # task 1
# import requests
# post_id = 1
# url = f"https://jsonplaceholder.typicode.com/todos/{post_id}"
# response = requests.get(url)
# print("Response Content:")
# print(response.json())
# if response.status_code >= 400:
#     print(f"Error: {response.status_code} - {response.text}")
# class ToDo:
#     def __init__(self, userId, id, title, completed):
#         self.userId = userId
#         self.id = id
#         self.title = title
#         self.completed = completed
# new_todo_object = ToDo(userId=1, id=post_id, title="Sample ToDo", completed=False)
# new_todo_payload = {
#     "userId": new_todo_object.userId,
#     "title": new_todo_object.title,
#     "completed": new_todo_object.completed
# }
# post_response = requests.post("https://jsonplaceholder.typicode.com/todos", json=new_todo_payload)
# print("\nPOST Response Content:")
# print(post_response.json())
# if post_response.status_code >= 400:
#     print(f"Error: {post_response.status_code} - {post_response.text}")
# new_todo_object.title = "Updated ToDo"
# new_todo_object.completed = True
# put_url = f"https://jsonplaceholder.typicode.com/todos/{new_todo_object.id}"
# put_payload = {
#     "userId": new_todo_object.userId,
#     "title": new_todo_object.title,
#     "completed": new_todo_object.completed
# }
# put_response = requests.put(put_url, json=put_payload)
# print("\nPUT Response Content:")
# print(put_response.json())
# if put_response.status_code >= 400:
#     print(f"Error: {put_response.status_code} - {put_response.text}")




# # task 2
# import requests
# import random
# class Episode:
#     def __init__(self, id, name, air_date, episode, character_urls):
#         self.id = id
#         self.name = name
#         self.air_date = air_date
#         self.episode = episode
#         self.character_urls = character_urls

#     def display_info(self):
#         print(f"Episode {self.episode}: {self.name}")
#         print(f"Air Date: {self.air_date}")
#         print(f"Character URLs: {', '.join(self.character_urls)}\n")

# class Character:
#     def __init__(self, id, name, status, species, gender, origin, location, episode_urls):
#         self.id = id
#         self.name = name
#         self.status = status
#         self.species = species
#         self.gender = gender
#         self.origin = origin
#         self.location = location
#         self.episode_urls = episode_urls

#     def display_info(self):
#         print(f"Character {self.id}: {self.name}")
#         print(f"Status: {self.status}")
#         print(f"Species: {self.species}")
#         print(f"Gender: {self.gender}")
#         print(f"Origin: {self.origin}")
#         print(f"Location: {self.location}")
#         print(f"Episode URLs: {', '.join(self.episode_urls)}\n")

# random_character_id = random.randint(1, 826)
# character_url = f"https://rickandmortyapi.com/api/character/{random_character_id}"
# character_response = requests.get(character_url).json()
# print("2.2 JSON Response:")
# print(character_response)
# print("\nKeys in JSON Structure:")
# print(character_response.keys())
# file_name = f"info_character_{random_character_id}.json"

# with open(file_name, "w") as file:
#     file.write(str(character_response))

# episode_urls = character_response["episode"]
# episode_ids = [url.split("/")[-1] for url in episode_urls]
# example_episode_url = "https://rickandmortyapi.com/api/episode/1"
# example_episode_response = requests.get(example_episode_url).json()
# print("\n2.5 Episode Response Structure:")
# print(example_episode_response.keys())
# all_episodes = []

# for episode_id in episode_ids:
#     episode_url = f"https://rickandmortyapi.com/api/episode/{episode_id}"
#     episode_response = requests.get(episode_url).json()
#     character_urls = episode_response["characters"]
#     characters = []
#     for character_url in character_urls:
#         character_response = requests.get(character_url).json()
#         characters.append(character_response["name"])
#     episode = Episode(
#         id=episode_response["id"],
#         name=episode_response["name"],
#         air_date=episode_response["air_date"],
#         episode=episode_response["episode"],
#         character_urls=character_urls
#     )
#     all_episodes.append(episode)

# for episode in all_episodes:
#     episode.display_info()

# print("\n2.9 Character Response Structure:")
# print(character_response.keys())
# random_character = Character(
#     id=character_response["id"],
#     name=character_response["name"],
#     status=character_response["status"],
#     species=character_response["species"],
#     gender=character_response["gender"],
#     origin=character_response["origin"]["name"],
#     location=character_response["location"]["name"],
#     episode_urls=character_response["episode"]
# )
# random_character.display_info()
# print("\nTask 2.13: Result")
# print(f"Random Character ID: {random_character_id}")
# print(f"Character File: {file_name}")
# print("Episodes:")

# for episode in all_episodes:
#     print(f"- Episode {episode.episode}: {episode.name}")
