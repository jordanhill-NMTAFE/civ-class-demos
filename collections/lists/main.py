print("Hi, I am a python file")

animals = []

print(animals)
animals.append("Dog")
animals.append("Cat")
animals.append("Mouse")

print(animals)

for i in range(0, 5):
    animals.append("Mouse")

print(animals)

mice = []

for animal in animals:
    if animal == "Mouse":
        mice.append(animal)

print(mice, len(mice))

is_list = True if type(mice) == list else False

print(is_list)

new_list = [animal for animal in animals if animal == "Cat"]

print("new_list:", new_list)


