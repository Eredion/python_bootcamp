#! /usr/bin/python3

coockbook = {'sandwitch' : {'ingredients' : ['ham','bread','cheese','tomatoes'],\
                            'meal' : 'lunch', 'prep_time': 10},\
             'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'],\
                       'meal':'dessert', 'prep_time':60},\
             'salad' : {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],\
                        'meal':'lunch', 'prep_time':15}}

print(coockbook.keys())

print(coockbook.values())

print(coockbook.items())

def print_recipe(name):
    print(coockbook[name])
    return

print_recipe('cake')
