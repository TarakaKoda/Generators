import random


first_name = ["srinu", "pavan", "kurama", "naruto","sasuke"]
last_name = ["uzumaki", "uchiha", "koda", "nara", "senju"]

def people_list(num_people):
    profile = []
    for (id ,num) in enumerate(num_people):
        dict = {
            "id": id+1,
            "fist_name": random.choice(first_name),
            "last_name": random.choice(last_name)
        }
        profile.append(dict)
    return profile

# details = people_list(range(5))
# print(details)

def people_generator(num_people):
    for (id, num) in enumerate(num_people):
        dect = {
            "id": id+1,
            "first_name": random.choice(first_name),
            "last_name": random.choice(last_name)
        }
        yield dect

result = people_generator(range(5))
print(list(result))