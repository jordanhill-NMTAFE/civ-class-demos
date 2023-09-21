names = {"Thomas": 5, "Mary": 3}
popular_names = []
unpopular_names = []

while len(names) < 4:
    name = input("Please provide a name:")
    name = name.capitalize()

    names[name] = names.get(name, 0) + 1
    # names[name] = User(name)

print(names)

print("Popular names are:")
for key, count in names.items():
    if count > 5:
        print(key)
        popular_names.append(key)
    else:
        unpopular_names.append(key)

# Print unpopular names
print("Unpopular names are:")

for name in unpopular_names:
    print(name)