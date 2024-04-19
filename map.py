import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeMap:
    def __init__(self):
        self._map = {}

    def recipeadd(self, recipename, recipeingredient):
        self._map[recipename] = recipeingredient

    def get_recipe(self, recipename):
        return self._map.get(recipename)

    def has_recipe(self, recipename):
        return recipename in self._map

    def items(self):
        return self._map.items()

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        return iter(self._map.items())


def recipesort(recipe_map, useringredients):
    common_ingredients_count = {}

    for recipe, recipeingredient in recipe_map.items():
        # common ingredients w/ user
        common_ingredients = set(recipeingredient) & set(useringredients)

        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)

    # sort from most to least in common
    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recipes

def searchbutton(recipe_map, useringredientsinput, outputtxt):
    useringredients = useringredientsinput.get().split(',')
    useringredients = [ingredient.strip() for ingredient in useringredients]
    
    sorted_recipes = recipesort(recipe_map, useringredients)
    
    # Clear previous output
    outputtxt.delete(1.0, tk.END)
    
    #recipe display
    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50:  # output only first 50
            common_ingredients = set(recipe_map.get_recipe(recipe)) & set(useringredients)
            outputtxt.insert(tk.END, f"\n{recipe}: {ingredient_count} ingredients in common\n")
            outputtxt.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            count += 1
        else:
            break

