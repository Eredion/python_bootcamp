#! /usr/bin/python3

import sys
import time
import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        try:
            self.name = str(name)
        except:
            print("ERROR, invalid book name")
            sys.exit(0)
        self.creation_time = datetime.now()
        self.last_update = self.creation_time
        self.recipe_list = {'starter': [], 'lunch' : [], 'dessert' : []}
    
    def get_recipe_by_name(self, name):
        "Print a recipe with the name `name` and return the instance"
        for type in self.recipe_list.values():
            for rec in type:
                if rec.name == name:
                    print(rec)
                    return(rec)
        print("ERROR: this recipe is not in the cookbook")
        pass

    def get_recipes_by_tines(self, recipe_type)
        "Get all recipe names for a given recipe_type"
        for type in self.recipe_list.keys():
            if type == recipe_type:

        pass

    def add_recipe(self, recipe)
        if not isinstance(recipe, Recipe):
            print("ERROR: only Recipe class can be added to the book")
            exit(0)
        else:
            self.recipe_list[recipe.recipe_type].append(recipe)
            self.last_update = datetime.now()
        pass

        

