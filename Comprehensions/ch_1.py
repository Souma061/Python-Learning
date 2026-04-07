menu = [
  "spam",
  "eggs",
  "bacon",
  "Iced lemon tea",
  "Iced peach tea",
  "Iced green tea"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)


#List comprehension is used to create a new list called iced_tea that contains only the items from the menu list that have the word "Iced" in them. The comprehension iterates through each item in the menu list and checks if "Iced" is a substring of the item. If it is, the item is included in the iced_tea list. The resulting list will contain only the iced tea options from the menu.
