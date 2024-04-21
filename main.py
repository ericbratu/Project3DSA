import pandas as pd
import tkinter as tk
import tkinter.font as tkfont
from tkinter import scrolledtext
import time
from pq import PriorityQueue, pqbutton
from graph import RecipeGraph, graphbutton
from dict import allRecipes

def main():
    recipe_graph = RecipeGraph()
    recipe_pq = PriorityQueue()

    df = pd.read_csv('veryfinal.csv')
    for index, row in df.iterrows():
        recipename = row['title']
        recipeingredient = eval(row['NER'])
        recipelink = row['link']

        # insert all recipes into priority queue
        recipe_pq.dict_insert(recipename, recipeingredient, recipelink)

        # insert all recipes into graph
        recipe_graph.add_vertex(recipename, recipelink)
        for ingredient in recipeingredient:
            recipe_graph.add_vertex(ingredient, None)
            recipe_graph.add_edge(recipename, ingredient)

    # main window
    root = tk.Tk()
    root.title("Recipe Finder")

    # input frame and user input
    inputbar = tk.Frame(root)
    inputbar.pack(pady=10, padx=10)
    useringredientsinput = tk.Entry(inputbar, width=50)
    useringredientsinput.pack(side=tk.LEFT, padx=5)

    # instructions
    disclaimer = tk.Label(inputbar, text="*Separate ingredients with a comma!", font=("Times New Roman", 10, "italic"))
    disclaimer.pack(side=tk.TOP, pady=5, anchor='center')
    
    # buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=5)

    # priority queue button
    pq_but = tk.Button(button_frame, text="Search using priority queue", command=lambda: pqbutton(recipe_pq, useringredientsinput, outputtxt, elapsed_time_label))
    pq_but.pack(side=tk.LEFT, padx=5)
    
    # graph buttons
    graph_but = tk.Button(button_frame, text="Search using graph", command=lambda: graphbutton(recipe_graph, useringredientsinput, outputtxt, elapsed_time_label))
    graph_but.pack(side=tk.LEFT, padx=5)

    # elapsed time
    elapsed_time_label = tk.Label(button_frame, text="Time taken: ")
    elapsed_time_label.pack(side=tk.LEFT, padx=5)

    # output text
    outputtxt = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD, font=("Times New Roman", 10), spacing2=2)
    outputtxt.pack(pady=10, padx=10)

    # bold font configuration
    bold_font = tkfont.Font(outputtxt, outputtxt.cget("font"))
    bold_font.configure(weight="bold")

    outputtxt.tag_configure("bold", font=bold_font)

    root.mainloop()

def new_func(useringredientsinput):
    new_var = useringredientsinput
    return new_var

if __name__ == "__main__":
    main()
