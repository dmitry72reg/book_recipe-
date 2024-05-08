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