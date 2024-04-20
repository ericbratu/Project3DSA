import pandas as pd
import tkinter as tk
from tkinter import scrolledtext, Label
import time
from map import RecipeMap, recipesort, mapbutton
from graph import RecipeGraph, recipe_sort, graphbutton

def main():

    recipe_map = RecipeMap()
    recipe_graph = RecipeGraph()

    df = pd.read_csv('veryfinal.csv')
    for index, row in df.iterrows():
        recipename = row['title']
        recipeingredient = eval(row['NER'])
        recipe_map.recipeadd(recipename, recipeingredient)
        

        recipe_graph.add_vertex(recipename)
        for ingredient in recipeingredient:
            recipe_graph.add_vertex(ingredient)
            recipe_graph.add_edge(recipename, ingredient)


    root = tk.Tk()
    root.title("Recipe Finder")


    inputbar = tk.Frame(root)
    inputbar.pack(pady=10, padx=10)
    useringredientsinput = tk.Entry(inputbar, width=50)
    useringredientsinput.pack(side=tk.LEFT, padx=5)


    disclaimer = tk.Label(inputbar, text="*Separate ingredients with a comma!", font=("Helvetica", 10, "italic"))
    disclaimer.pack(side=tk.TOP, pady=5, anchor='center')
    

    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)


    map_but = tk.Button(button_frame, text="Map", command=lambda: mapbutton(recipe_map, useringredientsinput, outputtxt, elapsed_time_label))
    map_but.pack(side=tk.LEFT, padx=5)
    

    graph_but = tk.Button(button_frame, text="Graph", command=lambda: graphbutton(recipe_graph, useringredientsinput, outputtxt, elapsed_time_label))
    graph_but.pack(side=tk.LEFT, padx=5)

    elapsed_time_label = tk.Label(button_frame, text="Time taken: ")
    elapsed_time_label.pack(side=tk.LEFT, padx=5)


    outputtxt = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
    outputtxt.pack(pady=10, padx=10)

    root.mainloop()

if __name__ == "__main__":
    main()
