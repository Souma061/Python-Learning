#set comprehension

favourite_languages = [
  "Js",
  "Python",
  "C++",
  "Java",
  "Js",
  "C++"
]

unique_lans = {langs for langs in favourite_languages if len(langs) > 2}
print(unique_lans)


recipes = {
  "Pancakes": ["flour", "milk", "eggs"],
  "Omelette": ["eggs", "milk", "cheese"],
  "Salad": ["lettuce", "tomatoes", "cucumbers"]
}

unique_ingredients = {spices for ingredients in recipes.values() for spices in ingredients}
print(unique_ingredients)

#set comprehension is used to create a set of unique ingredients from the recipes dictionary. It iterates through the values of the recipes dictionary (which are lists of ingredients) and then through each ingredient in those lists, adding them to the set. The resulting set will contain only unique ingredients, eliminating any duplicates.
