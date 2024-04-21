import time
import tkinter as tk

class PriorityQueue:
    def __init__(self):
        self.dict = {}
        self.queue = []
        
    def dict_insert(self, recipename, recipeingredientlist, recipelink, priority):
        if recipename not in self.dict:
            self.dict[recipename] = (recipeingredientlist, recipelink, priority)
    
    def pq_insert(self, recipename, recipeingredientlist, recipelink, priority):
        self.queue.append((recipename, recipeingredientlist, recipelink, priority))
        self._heapify_up(len(self.queue) - 1)
    
    def pop(self):
        if not self.queue:
            return None
        max_item = self.queue[0]
        last_item = self.queue.pop()
        if self.queue:
            self.queue[0] = last_item
            self._heapify_down(0)
        return max_item
    
    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.queue[index][3] > self.queue[parent_index][3]:
                self.queue[index], self.queue[parent_index] = self.queue[parent_index], self.queue[index]
                index = parent_index
            else:
                break
    
    def _heapify_down(self, index):
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            largest_index = index
            
            if left_child_index < len(self.queue) and self.queue[left_child_index][3] > self.queue[largest_index][3]:
                largest_index = left_child_index
            if right_child_index < len(self.queue) and self.queue[right_child_index][3] > self.queue[largest_index][3]:
                largest_index = right_child_index
            
            if largest_index != index:
                self.queue[index], self.queue[largest_index] = self.queue[largest_index], self.queue[index]
                index = largest_index
            else:
                break


def recipesort(recipe_pq, useringredients):
    sorted_recipes = {}

    for recipename, recipe_data in recipe_pq.dict.items():
        recipeingredientlist, recipelink, initialpriority = recipe_data
        
        similar_ingredients = set(recipeingredientlist) & set(useringredients)
        
        if similar_ingredients:
            recipe_pq.pq_insert(recipename, recipeingredientlist, recipelink, len(similar_ingredients))

    while recipe_pq.queue:
        recipename, recipeingredientlist, recipelink, priority = recipe_pq.pop()
        sorted_recipes[recipename] = (recipeingredientlist, recipelink, priority)

    print(sorted_recipes)
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
    
    if sorted_recipes == []:
        outputtxt.insert(tk.END, "No recipes found with the input ingredients.")
        return

    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input using priority queue structure:\n")
    count = 0
    
    for recipename, recipe_data in sorted_recipes.items():
        if count < 50:
            recipeingredientlist, recipelink, priority = recipe_data  
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
