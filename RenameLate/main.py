# Loops

items = ["Bob", "Ted", "Liu"]
for index, item in enumerate(items):
    print(index, item)

# items = [1, 2, 3, 4]
# for item in items:
#     print(item)


# count = 0
# while count < 10:
#     print("The condition is true")
#     count += 1

# print("After loop")


# Nested function

# def count():
#     count = 0

#     def increment():
#         nonlocal count
#         count += 1
#         print(count)

#     increment()


# count()


# def talk(phrase):
#     def say(word):
#         print(word)

#     words = phrase.split(' ')
#     for word in words:
#         say(word)


# talk('I am going to buy the milk')


# Sets - Unordered, unchangeable, and un-indexed, no duplicates

# set1 = {"Roger", "Syd", "Thomas", "Luke"}

# set2 = {"Roger"}

# set3 = {"Thomas"}

# intersect = set1 & set2
# print(intersect)  # prints where the 2 sets intersect

# mod = set1 | set2
# print(mod)  # prints items in both sets

# mod2 = set1 - set3
# print(mod2)


# ------------------------------------------------------------------------------------------

# Dictionaries - ordered and mutable, does not allow duplicates
# dog = {"name": "Roger", "age": 8, "Color": "green"}

# dog["name"] = "Syd"
# print(dog["name"])

# print(dog.popitem())  # Removes and prints the last item in dictionary
# print(dog)
# print(list(dog.keys()))  # prints dict keys in list
# print(list(dog.values()))  # prints dict values in list
# print(list(dog.items()))  # prints dict items in list

# dog["favorite food"] = "Meat" #Adds new key-value pair in dict
# print(dog)

# ------------------------------------------------------------------------------------------
# Tuples are ordered, and immutable
# names = ("Roger", "Syd")
# print(names)
# ------------------------------------------------------------------------------------------

# List - ordered, changeable, and allow duplicates
# items = ["Roger", "bob", "Beau", "Syd", "Quincy"]


# print(sorted(items, key=str.lower)) # Makes a different copy of items list and sorts it
# print(items)
# ------------------------------------------------------------------------------------------


# Copy original list
# items = ["Roger", "bob", "Beau", "Syd", "Quincy"]

# items_copy = items[:]
# items.sort(key=str.lower)

# print(items)
# print(items_copy)
# ------------------------------------------------------------------------------------------


# Sort function orders upper-cased letters first, and then lower-case letters
# items = ["Roger", "bob", "Beau", "Syd", "Quincy"]
# items.sort(key=str.lower)
# print(items)
# ------------------------------------------------------------------------------------------

# items = ["Roger", 1, "Syd", True, "Quincy", 7]
# items[1:1] = ["Test1", "Test2"]
# print(items)
# items.insert(2, "Test")
# print(items)
# ------------------------------------------------------------------------------------------


# from enum import Enum

# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1
# print(list(State))
# ------------------------------------------------------------------------------------------
