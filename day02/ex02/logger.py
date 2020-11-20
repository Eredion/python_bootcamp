#! /usr/bin/python3 

import time 
from random import randint

def search_func_name(function):
    word = str(function).split()
    word = word[1]
    return word[14:].replace('_', ' ').title()


def log(func):
    def inner(*args, **kwargs):
        func_name = (search_func_name(func))
        text = "(cmaxime)Running: " + func_name + '\t\t[ exec-time = '
        text += str("{:.3f}".format(time.process_time())) + ' ms ]\n'
        file = open("machine.log", "+a")
        file.write(text)
        file.close()
        return func(*args, **kwargs)
    return inner    

class CoffeeMachine():

    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_cofee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Cofee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":

    machine = CoffeeMachine()
    for i in range(0,5):
        machine.make_cofee()

    machine.make_cofee()
    machine.add_water(70)

