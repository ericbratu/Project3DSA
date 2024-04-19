import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeMap:
    def __init__(self):
        self._map = {}

    def add_recipe(self, recipe_name, recipe_ingredients):
        """Add a recipe to the map with the given recipe name and ingredients."""
        self._map[recipe_name] = recipe_ingredients

    def get_recipe(self, recipe_name):
        """Retrieve ingredients for a given recipe name."""
        return self._map.get(recipe_name)

    def has_recipe(self, recipe_name):
        """Check if the map contains a recipe with the given name."""
        return recipe_name in self._map

    def items(self):
        """Return an iterable of (recipe_name, recipe_ingredients) tuples."""
        return self._map.items()

    def __len__(self):
        """Return the number of recipes in the map."""
        return len(self._map)

    def __iter__(self):
        """Allow iteration over the recipe map."""
        return iter(self._map.items())

    def __repr__(self):
        """Return a string representation of the map."""
        return repr(self._map)

# Filter and sort recipes based on user input
def filter_and_sort_recipes(recipe_map, user_ingredients):
    common_ingredients_count = {}

    for recipe, recipe_ingredients in recipe_map.items():
        # See how many ingredients in common
        common_ingredients = set(recipe_ingredients) & set(user_ingredients)

        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)

    # Sort recipes by num ingredients in common with user input in descending order
    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recipes

def on_search_button_click(recipe_map, user_ingredients_entry, output_text):
    # Get user input (list of ingredients)
    user_ingredients = user_ingredients_entry.get().split(',')
    user_ingredients = [ingredient.strip() for ingredient in user_ingredients]
    
    # Filter and sort recipes based on user input
    sorted_recipes = filter_and_sort_recipes(recipe_map, user_ingredients)
    
    # Clear previous output
    output_text.delete(1.0, tk.END)
    
    # Display results in the output text area
    output_text.insert(tk.END, "Recipes sorted by most ingredients in common with your input:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50:  # Output only first 50
            common_ingredients = set(recipe_map.get_recipe(recipe)) & set(user_ingredients)
            output_text.insert(tk.END, f"\n{recipe}: {ingredient_count} ingredients in common\n")
            output_text.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            count += 1
        else:
            break

