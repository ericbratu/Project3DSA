import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeMap:
    def __init__(self):
        self._map = {}

    def recipeadd(self, recipename, recipeingredient, recipelink):
        if recipename not in self._map:
            self._map[recipename] = recipeingredient
            self._map[recipename].append(recipelink)


    def get_recipe(self, recipename):
        return self._map.get(recipename)

    def has_recipe(self, recipename):
        return recipename in self._map

    def items(self):
        return self._map.items()


    def __iter__(self):
        return iter(self._map.items())


def recipesort(recipe_map, useringredients):
    common_ingredients_count = {}

    for recipe, recipeingredient in recipe_map.items():

        common_ingredients = set(recipeingredient) & set(useringredients)

        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)

    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recipes

def mapbutton(recipe_map, useringredientsinput, outputtxt, elapsed_time_label):

    userinputs = useringredientsinput.get().strip()
    
    if not userinputs:
        return
    
    start_time = time.time()
    

    useringredients = userinputs.split(',')
    useringredients = [ingredient.strip() for ingredient in useringredients]
    outputtxt.delete(1.0, tk.END)
    
    sorted_recipes = recipesort(recipe_map, useringredients)
        
    # if there are no recipes with input ingredients
    if sorted_recipes == []:
        outputtxt.insert(tk.END, "No recipes found with the input ingredients.")
        return
    
    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input using map structure:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50:
            common_ingredients = set(recipe_map.get_recipe(recipe)) & set(useringredients)
            outputtxt.insert(tk.END, f"\n{recipe}: ", "bold")
            outputtxt.insert(tk.END, f"{ingredient_count} ingredients in common\n")
            outputtxt.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")                
            outputtxt.insert(tk.END, f"Link: {recipe_map.get_recipe(recipe)[-1]}\n")  
            count += 1
        else:
            break
    

    elapsed_time = time.time() - start_time
    elapsed_time_label.config(text=f"Time taken: {elapsed_time:.3f} seconds")
    