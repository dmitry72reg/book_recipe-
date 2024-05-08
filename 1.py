cook_book = {}
with open('1.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            if line.isdigit():
                dish = []
                cook_book[dish_name] = dish
            else:
                if '|' in line:
                    ingredient, quantity, measure = line.split('|')
                    dish.append({'ingredient_name': ingredient.strip(), 'quantity': int(quantity.strip()), 'measure': measure.strip()})
                else:
                    dish_name = line


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                if ingredient['ingredient_name'] not in shop_list:
                    shop_list[ingredient['ingredient_name']] = {
                        'quantity': ingredient['quantity'] * person_count,
                        'measure': ingredient['measure']
                    }
                else:
                    shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    return shop_list