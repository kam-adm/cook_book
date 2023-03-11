from pprint import pprint
with open('recipes.txt', 'rt') as file:
    cook_book = {}
    s = cook_book
    for line in file:
        dish_name = line.strip()
        quantity_ingredients = int(file.readline())
        list_ingredients = []
        print(dish_name)
        for _ in range(quantity_ingredients):
            ingredient_name, quantity, measure = file.readline().strip().split(' | ')
            list_ingredients.append({
             'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure
            })
        file.readline()
        cook_book[dish_name] = list_ingredients
        print(list_ingredients)
    #pprint(cook_book)
