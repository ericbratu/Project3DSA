import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time

class RecipeGraph:
    def __init__(self):
        self._adk_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.adj_list and vertex2 in self.adj_list:
            self.adj_list[vertex1].append(vertex2)
            # self.adj_list[vertex2].append(vertex1)  # not sure if it should be directed or undirected

    def get_adjacent_vertices(self, vertex):
        if vertex in self.adj_list:
            return self.adj_list[vertex]
        else:
            return []

    def display_adjacency_list(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


    def recipe_sort(recipe_graph, userinput):
        recipe_matches = {}

        for recipe in graph.adj_list.keys():
            ingredients = graph.get_adjacent_vertices(recipe)

            common_ingredients = set(userinput) & set(ingredients)
            common_ing_count = len(common_ingredients)

            recipe_matches[recipe] = common_ing_count
        
        sorted_recipes = sorted(recipe_matches.times(), key=lambda x:x[1], reverse=True)

        for recipe, common_ing_count in sorted_recipes:
            common_ingredients = set(userinput) & set(graph.get_adjacent_vertices(recipe))

def main():
    df = pd.read_csv('veryfinal.csv')

    recipe_graph = RecipeGraph()

    for index, row in df.iterrows():
        recipename = row['title']
        recipeingredients = eval(row['NER'])
        recipe_map.add_vertex(recipename)

        for ingredient in recipeingredients:
            recipe_map.add_vertex(ingredient)
            recipe_map.add_edge(recipename, ingredient)
    
    