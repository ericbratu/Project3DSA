import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeMap:
    def __init__(self, size=100):
        self.size = size
        self._map = [[] for _ in range(size)]


    def customhash(self, key):
        hash_value = sum(ord(char) for char in key) % self.size
        return hash_value


    def recipeadd(self, recipename, recipeingredient, recipelink):
        if not isinstance(recipename, str):
            raise TypeError("Recipe name must be a string")

        hash_value = self.customhash(recipename)

    # check if recipe exists in hash
        for i, (name, ingredients, link) in enumerate(self._map[hash_value]):
            if name == recipename:

                self._map[hash_value][i] = (recipename, recipeingredient, recipelink)
                return
        self._map[hash_value].append((recipename, recipeingredient, recipelink))


    def get_recipe(self, recipename):
        # custom hash func
        hash_value = self.customhash(recipename)
        
        for name, ingredients, link in self._map[hash_value]:
            if name == recipename:
                return ingredients, link
        return None


    def has_recipe(self, recipename):
        hash_value = self.customhash(recipename)
        
        for name, ingredients, link in self._map[hash_value]:
            if name == recipename:
                return True
        return False


    def items(self):
        for hash_value in range(self.size):
            for name, ingredients, link in self._map[hash_value]:
                yield name, ingredients, link


    def __iter__(self):
        return self.items()


def recipesort(recipe_map, useringredients):
    common_ingredients_count = {}

    for recipe, recipeingredient, recipelink in recipe_map.items():
        # compare ingredients
        common_ingredients = set(recipeingredient) & set(useringredients)

        #count common ingredients
        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)

    # sort by # of common ingredients in descending order
    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    return sorted_recipes


def mapbutton(recipe_map, useringredientsinput, outputtxt, elapsed_time_label):
    userinputs = useringredientsinput.get().strip()
    
    if not userinputs:
        return
    
    start_time = time.time()
    
    #input parsing
    useringredients = userinputs.split(',')
    useringredients = [ingredient.strip() for ingredient in useringredients]
    
    outputtxt.delete(1.0, tk.END)

    sorted_recipes = recipesort(recipe_map, useringredients)
        
    # no recipes
    if not sorted_recipes:
        outputtxt.insert(tk.END, "No recipes found with the input ingredients.")
        return
    
    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input using map structure:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50:
            recipe_info = recipe_map.get_recipe(recipe)
            if recipe_info:
                ingredients, link = recipe_info
            
            # find common ingredients
            common_ingredients = set(ingredients) & set(useringredients)
            
            outputtxt.insert(tk.END, f"\n{recipe}: ", "bold")
            outputtxt.insert(tk.END, f"{ingredient_count} ingredients in common\n")
            outputtxt.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            outputtxt.insert(tk.END, f"Link: {link}\n")
            
            count += 1
        else:
            break
    
            #finalise time taken
    elapsed_time = time.time() - start_time
    elapsed_time_label.config(text=f"Time taken: {elapsed_time:.3f} seconds")