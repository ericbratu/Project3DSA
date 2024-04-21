import pandas as pd
import tkinter as tk
import tkinter.font as tkfont
from tkinter import scrolledtext, Label
import time
from map import RecipeMap, recipesort, mapbutton
from graph import RecipeGraph, recipe_sort, graphbutton

def main():
    recipe_map = RecipeMap()
    recipe_graph = RecipeGraph()

    # Read the CSV file
    df = pd.read_csv('veryfinal.csv')

    # Iterate through each row in the dataframe
    for index, row in df.iterrows():
        # Preprocess the recipe name, ingredients, and link
        recipename = str(row['title'])  # typecast to string
        recipeingredient = eval(row['NER'])
        recipelink = str(row['link'])  # typecast to string
        
        # Add the recipe to the RecipeMap
        recipe_map.recipeadd(recipename, recipeingredient, recipelink)

        # Graph implementation
        recipe_graph.add_vertex(recipename, recipelink)
        for ingredient in recipeingredient:
            recipe_graph.add_vertex(ingredient, None)
            recipe_graph.add_edge(recipename, ingredient)

    # Initialize the main window
    root = tk.Tk()
    root.title("Recipe Finder")

    # User Input
    inputbar = tk.Frame(root)
    inputbar.pack(pady=10, padx=10)
    useringredientsinput = tk.Entry(inputbar, width=50)
    useringredientsinput.pack(side=tk.LEFT, padx=5)

    # Disclaimer/instructions
    disclaimer = tk.Label(inputbar, text="*Separate ingredients with a comma!", font=("Times New Roman", 10, "italic"))
    disclaimer.pack(side=tk.TOP, pady=5, anchor='center')

    # Button frame
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    # Map search button
    map_but = tk.Button(button_frame, text="Search using map", command=lambda: mapbutton(recipe_map, useringredientsinput, outputtxt, elapsed_time_label))
    map_but.pack(side=tk.LEFT, padx=5)

    # Graph search button
    graph_but = tk.Button(button_frame, text="Search using graph", command=lambda: graphbutton(recipe_graph, useringredientsinput, outputtxt, elapsed_time_label))
    graph_but.pack(side=tk.LEFT, padx=5)

    # Elapsed time label
    elapsed_time_label = tk.Label(button_frame, text="Time taken: ")
    elapsed_time_label.pack(side=tk.LEFT, padx=5)

    # Output
    outputtxt = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, font=("Times New Roman", 10), spacing2=2)
    outputtxt.pack(pady=10, padx=10)

    # Bold font configuration
    bold_font = tkfont.Font(outputtxt, outputtxt.cget("font"))
    bold_font.configure(weight="bold")

    outputtxt.tag_configure("bold", font=bold_font)

    root.mainloop()

if __name__ == "__main__":
    main()
