import time
import tkinter as tk

class PriorityQueue:
    def __init__(self):
        self.dict = {}
        self.queue = []
        
    def dict_insert(self, recipename, recipeingredientlist, recipelink):
        if recipename not in self.dict:
            self.dict[recipename] = (recipeingredientlist, recipelink, 0)

    def pq_insert(self, recipename, recipeingredientlist, recipelink):
        if recipename in self.dict:
            recipe_data = self.dict[recipename]
            self.queue.append((recipename, recipe_data[0], recipe_data[1], recipe_data[2]))

    def pop(self):
        if not self.queue:
            return None
        max_priority = max(self.queue, key=lambda x: x[3])
        self.queue.remove(max_priority)
        return max_priority

def recipesort(recipe_pq, useringredients):
    sorted_recipes = []

    for recipename, recipe_data in recipe_pq.dict.items():
        recipeingredientlist, recipelink, priority = recipe_data
        similar_ingredients = set(recipeingredientlist) & set(useringredients)
        if similar_ingredients:
            recipe_pq.dict[recipename] = (recipeingredientlist, recipelink, len(similar_ingredients))
            recipe_pq.pq_insert(recipename, recipeingredientlist, recipelink)

    while recipe_pq.queue:
        sorted_recipes.append(recipe_pq.pop())

    return sorted_recipes

def pqbutton(recipe_pq, useringredientsinput, outputtxt, elapsed_time_label):
    userinputs = useringredientsinput.get().strip()

    if not userinputs:
        return
    
    start_time = time.time()

    useringredients = userinputs.split(',')
    useringredients = [ingredient.strip() for ingredient in useringredients]
    
    outputtxt.delete(1.0, tk.END)

    sorted_recipes = recipesort(recipe_pq, useringredients)
    if not sorted_recipes:
        outputtxt.insert(tk.END, "No recipes found with the input ingredients.")
        return

    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input using priority queue structure:\n")
    count = 0
    for recipe_data in sorted_recipes:
        if count < 50:
            recipename, recipeingredientlist, recipelink, priority = recipe_data
            common_ingredients = set(useringredients) & set(recipeingredientlist)
            outputtxt.insert(tk.END, f"\n{recipename}: ", "bold")
            outputtxt.insert(tk.END, f"{priority} ingredients in common\n")
            outputtxt.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            outputtxt.insert(tk.END, f"Link: {recipelink}\n")
            count += 1
        else:
            break
    
    elapsed_time = time.time() - start_time
    elapsed_time_label.config(text=f"Time taken: {elapsed_time:.2f} seconds")
