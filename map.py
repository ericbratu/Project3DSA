import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeMap:
    def __init__(self):
        self._map = {}

    def add_recipe(self, recipe_name, recipe_ingredients):
        self._map[recipe_name] = recipe_ingredients

    def get_recipe(self, recipe_name):
        return self._map.get(recipe_name)

    def has_recipe(self, recipe_name):
        return recipe_name in self._map

    def items(self):
        return self._map.items()

    def __len__(self):
        return len(self._map)

    def __iter__(self):
        return iter(self._map.items())


def recipesort(recipe_map, user_ingredients):
    common_ingredients_count = {}

    for recipe, recipe_ingredients in recipe_map.items():
        # common ingredients w/ user
        common_ingredients = set(recipe_ingredients) & set(user_ingredients)

        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)

    # sort from most to least in common
    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recipes

def searchbutton(recipe_map, user_ingredients_entry, output_text):
    user_ingredients = user_ingredients_entry.get().split(',')
    user_ingredients = [ingredient.strip() for ingredient in user_ingredients]
    
    sorted_recipes = recipesort(recipe_map, user_ingredients)
    
    # Clear previous output
    output_text.delete(1.0, tk.END)
    
    #recipe display
    output_text.insert(tk.END, "Recipes sorted by most ingredients in common with your input:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50:  # output only first 50
            common_ingredients = set(recipe_map.get_recipe(recipe)) & set(user_ingredients)
            output_text.insert(tk.END, f"\n{recipe}: {ingredient_count} ingredients in common\n")
            output_text.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            count += 1
        else:
            break

