# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 13:11:24 2023

@author: ryanw
"""

import os
import numpy as np

def choose_dishes(recipes, number):
    if len(recipes) < number:
        number = len(recipes)
        print("Not enough recipes to populate the list. Opting for minimal number instead.")
    return np.random.choice(recipes, number, replace=False)

def main():
    directory = os.path.dirname(os.path.realpath(__file__))
    recipe_dir = directory + "\\Recipes\\"
    
    dishes = []
    for recipe in os.listdir(recipe_dir):
        dishes.append(recipe[:-4])  # assumes the files have the .txt extension
    
    if not os.path.exists(directory + "\\Last Week.txt"):
        with open(directory + "\\Last Week.txt", "w") as w:
            pass
    
    valid_recipes = [x for x in dishes]
    with open(directory + "\\Last Week.txt", "r") as previous:
        for line in previous:
            valid_recipes.remove(str(line[:-1]))
    
    loop = "n"
    while loop == "n":
        meals = int(input("Please enter how many dishes are desired: "))
        options = choose_dishes(valid_recipes, meals)
        print(f"The randomly chosen options are {options}.")
        loop = input("Are you happy with this result? Enter y/n: ")
    
    os.remove(directory + "\\Last Week.txt")
    with open(directory + "\\Last Week.txt", "w") as previous:
        for option in options:
            print(option)
            previous.write(option + "\n")
    
    
if __name__ == "__main__":
    main()