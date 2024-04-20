import time
import tkinter as tk

class RecipeGraph:
    def __init__(self):
        self.adjacency_list = {}
        self.recipe_links = {}

    def add_vertex(self, vertex, link):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
            self.recipe_links[vertex] = link

    def add_edge(self, start_vertex, end_vertex):
        if start_vertex in self.adjacency_list and end_vertex in self.adjacency_list:
            self.adjacency_list[start_vertex].append(end_vertex)
        else:
            raise ValueError("Both vertices must be in the graph.")

    def get_neighbors(self, vertex):
        if vertex in self.adjacency_list:
            return self.adjacency_list[vertex]
        else:
            raise ValueError("Vertex not found in graph.")

    def get_recipe_link(self, recipe):
        return self.recipe_links[recipe]

    def __str__(self):
        return str(self.adjacency_list)

def recipe_sort(graph, user_inputs):
    recipe_matches = {}
    
    for recipe in graph.adjacency_list.keys():
        ingredients = graph.get_neighbors(recipe)
        

        common_ingredients = set(user_inputs) & set(ingredients)
        num_common_ingredients = len(common_ingredients)
        

        recipe_matches[recipe] = num_common_ingredients
    

    sorted_recipes = sorted(recipe_matches.items(), key=lambda x: x[1], reverse=True)
    

    return sorted_recipes

import time

def graphbutton(recipe_graph, useringredientsinput, outputtxt, elapsed_time_label):

    userinputs = useringredientsinput.get().strip()

    if not userinputs:
        return
    
    start_time = time.time()

    useringredients = userinputs.split(',')
    useringredients = [ingredient.strip() for ingredient in useringredients]
    

    outputtxt.delete(1.0, tk.END)
    

    sorted_recipes = recipe_sort(recipe_graph, useringredients)
    

    outputtxt.insert(tk.END, "Recipes sorted by most ingredients in common with your input using graph structure:\n")
    count = 0
    for recipe, ingredient_count in sorted_recipes:
        if count < 50: 
            common_ingredients = set(recipe_graph.get_neighbors(recipe)) & set(useringredients)
            outputtxt.insert(tk.END, f"\n{recipe}: ", "bold")
            outputtxt.insert(tk.END, f"{ingredient_count} ingredients in common\n")
            outputtxt.insert(tk.END, f"Common ingredients: {', '.join(common_ingredients)}\n")
            outputtxt.insert(tk.END, f"Link: {recipe_graph.get_recipe_link(recipe)}\n")
            count += 1
        else:
            break
    

    elapsed_time = time.time() - start_time
    elapsed_time_label.config(text=f"Time taken: {elapsed_time:.2f} seconds")

