#! /usr/bin/python3

coockbook = {'sandwitch' : {'ingredients' : ['ham','bread','cheese','tomatoes'],\
                            'meal' : 'lunch', 'prep_time': 10},\
             'cake' : {'ingredients' : ['flour', 'sugar', 'eggs'],\
                       'meal':'dessert', 'prep_time':60},\
             'salad' : {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],\
                        'meal':'lunch', 'prep_time':15}}

#print(coockbook.keys())

#print(coockbook.values())

#print(coockbook.items())

def print_recipe(name):
    if name in coockbook:
        print('Recipe for ' + name)
        print('Ingredients list: ', end='')
        print(coockbook[name]['ingredients'])
        print('To be eaten for ' + coockbook[name]['meal'] + '.')
        print('Takes ' + str(coockbook[name]['prep_time']) + ' minutes of coocking.\n')
        
    else:
        print("This recipe is not in the coockbook")
    return

def delete_recipe(name):
    if name in coockbook:
        coockbook.pop(name)
    else:
        print("This recipe is not in the coockbook")

def add_recipe(name = '', ingredients = [], meal = '', prep = 0):
    if not name in coockbook:
        coockbook[name] = {'ingredients':ingredients, 'meal':meal, 'prep_time':prep}
    else:
        print("This recipe is already in the coockbook")

def print_all():
    for recipe in coockbook:
        print_recipe(recipe)
    return


while 42:
    print("\nPlease select an option typing the corresponding number:")
    print("1: Add a recipe\n2: Delete recipe\n3: Print a recipe")
    print("4: Print the coockbook\n5: Quit")
    command = input()
    if command == '1':
        print("\nIntroduce a new recipe name: ")
        name = input()
        print("Introduce the ingredients:")
        ingredients = input()
        print("Introduce meal type:")
        meal = input()
        print("Introduce preparation time in minutes:")
        time = int(input())
        add_recipe(name, ingredients, meal, time)
    elif command == '2':
        print("\nIntroduce the recipe you want to remove:")
        name = input()
        delete_recipe(name)
    elif command == '3':
        print('\nIntroduce the recipe you want to print:')
        name = input()
        print_recipe(name)
    elif command == '4':
        print_all()
    elif command == '5':
        exit()
    else:
        print('\nThis is not a valid option, please type a valid number\nTo exit, press 5.')

