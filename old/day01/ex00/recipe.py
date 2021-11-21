#! /usr/bin/python3

class Recipe:
    def __init__(self, name, lvl, time, ingredients, description = '', recipe_type = ''):
        ret = 0
        try: 
            self.name = str(name)
            if int(lvl) < 1  | int(lvl) > 5 | int(time) < 0:
                ret = 1
            self.coocking_lvl = int(lvl)
            self.coocking_time = int(time)
            self.ingredients = ingredients
            if not isinstance(ingredients, list):
                ret = 1
            self.description = str(description)
            self.recipe_type = str(recipe_type)
            if len(name) == 0 | len(ingredients) == 0 | len (recipe_type) == 0:
                ret = 1
        except:
            ret = 1
        if ret == 1:
            print("Recipe inicialization error, check params")
            exit(0)
    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ''
        txt += 'Recipe of ' + self.name + '\nCoocking_lvl: ' + str(self.coocking_lvl)
        txt += '\nCoocking time: '+ str(self.coocking_time) + ' minutes\nIngredients: '
        txt += str(self.ingredients)
        txt += '\nDescription: ' + self.description + '\nType of recipe: ' + self.recipe_type
        return txt



            
            

