from pprint import pprint


with open('recipes.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        quantity_ingredients = int(file.readline())
        list_ingredients = []
        for _ in range(quantity_ingredients):
            ingredient_name, measure, quantity = file.readline().strip().split(' | ')
            list_ingredients.append({
                'ingredient_name': ingredient_name,
                'measure': int(measure),
                'quantity': quantity
                 })
        file.readline()
        cook_book[dish_name] = list_ingredients



    def get_shop_list_by_dishes(dishes, person_count):
        ingredient_list_by_dishes = {}
        for i in cook_book:
            for m in dishes:
                if i == m:
                    for n in cook_book[i]:
                        if n['ingredient_name'] not in ingredient_list_by_dishes:
                            ingredient_list_by_dishes.setdefault(n['ingredient_name'], []).append(n['measure'] * person_count)
                            ingredient_list_by_dishes.setdefault(n['ingredient_name'], []).append(n['quantity'])
                        else:
                            g = int(n['measure'])
                            ingredient_list_by_dishes[ingredient_name][0] += g

        pprint(ingredient_list_by_dishes)

    get_shop_list_by_dishes(['Омлет', 'Запеченный картофель', 'Фахитос'], 2)


