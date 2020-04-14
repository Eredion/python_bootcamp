def delete_recipe(name, dic):
    aux = dict(dic)
    del aux[name]
    return aux

def print_recipe(name, dic):
    print("Recipe for", name, end = ":\n")
    print("Ingredients list:", dic[name]['ingredients'])
    print("To be eaten for", dic[name]['meal'])
    print("Takes", dic[name]['prep_time'], "minutes of coocking")

coockbook = {'sandwich': {'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],\
                        'meal' : 'lunch', 'prep_time' : 10},\
            'cake': {'ingredients' : ['flour', 'sugar', 'eggs'],\
                        'meal' : 'dessert', 'prep_time' : 60},
            'salad': {'ingredients': ['avocado', 'arugula', 'tomatoes'],\
                'meal' : 'starter', 'prep_time' : 15}
            }

print_recipe('sandwich', coockbook)

coockbook = delete_recipe('sandwich', coockbook)
print(coockbook)
