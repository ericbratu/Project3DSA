import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time
from map import RecipeMap, recipesort, searchbutton

def main():
    recipe_map = RecipeMap()
    
    # load from sheet
    df = pd.read_csv('veryfinal.csv')
    for index, row in df.iterrows():
        recipename = row['title']
        recipeingredient = eval(row['NER'])
        recipe_map.recipeadd(recipename, recipeingredient)
    
    root = tk.Tk()
    root.title("Recipe Finder")

    #ui
    inputbar = tk.Frame(root)
    inputbar.pack(pady=10, padx=10)
    useringredientsinput = tk.Entry(inputbar, width=50)
    useringredientsinput.pack(side=tk.LEFT, padx=5)
    searchbut = tk.Button(inputbar, text="Search", command=lambda: searchbutton(recipe_map, useringredientsinput, outputtxt))
    searchbut.pack(side=tk.LEFT, padx=5)
    disclaimer = tk.Label(inputbar, text="*Separate ingredients with a comma!", font=("Helvetica", 10, "italic"))
    disclaimer.pack(side=tk.TOP, pady=5, anchor='center')
    outputtxt = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
    outputtxt.pack(pady=10, padx=10)


    root.mainloop()
if __name__ == "__main__":
    main()
