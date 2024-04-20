import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeGraph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []

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

    def __str__(self):
        return str(self.adjacency_list)


def recipe_sort(graph, user_inputs):
    # map to keep track of recipe matches
    recipe_matches = {}
    
    # iterate through each recipe in the graph
    for recipe in graph.adjacency_list.keys():
        # get the ingredients associated with the recipe
        ingredients = graph.get_neighbors(recipe)
        
        # matching count
        common_ingredients = set(user_inputs) & set(ingredients)
        num_common_ingredients = len(common_ingredients)
        
        # add the recipe and the number of matches to the dictionary
        recipe_matches[recipe] = num_common_ingredients
    
    # sort recipes by the number of matches in descending order
    sorted_recipes = sorted(recipe_matches.items(), key=lambda x: x[1], reverse=True)
    
    # print the sorted recipes with their common ingredients w/ 50 cap
    num_outputs = min(50, len(sorted_recipes))
    for i in range(num_outputs):
        recipe, num_common_ingredients = sorted_recipes[i]
        common_ingredients = set(user_inputs) & set(graph.get_neighbors(recipe))
        print(f"Recipe title: {recipe}, {num_common_ingredients} ingredients in common. Common ingredients: {', '.join(common_ingredients)}")

# def main():
#     recipe_map = RecipeGraph()
    
#     df = pd.read_csv('veryfinal.csv')
#     for index, row in df.iterrows():
#         recipename = row['title']
#         recipeingredients = eval(row['NER'])
#         recipe_map.add_vertex(recipename)
        
#         for ingredient in recipeingredients:
#             recipe_map.add_vertex(ingredient)
#             recipe_map.add_edge(recipename, ingredient)

#     user_input = input("Enter ingredients separated by commas: ")
#     user_inputs = [ingredient.strip() for ingredient in user_input.split(',')]
    
#     recipe_sort(recipe_map, user_inputs)

# if __name__ == "__main__":
#     main()
