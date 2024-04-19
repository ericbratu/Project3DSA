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
        recipe_name = row['title']
        recipe_ingredients = eval(row['NER'])
        recipe_map.add_recipe(recipe_name, recipe_ingredients)
    
    root = tk.Tk()
    root.title("Recipe Finder")

    #ui
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10, padx=10)
    user_ingredients_entry = tk.Entry(input_frame, width=50)
    user_ingredients_entry.pack(side=tk.LEFT, padx=5)
    search_button = tk.Button(input_frame, text="Search", command=lambda: searchbutton(recipe_map, user_ingredients_entry, output_text))
    search_button.pack(side=tk.LEFT, padx=5)
    hint_label = tk.Label(input_frame, text="*Separate ingredients with a comma!", font=("Helvetica", 10, "italic"))
    hint_label.pack(side=tk.TOP, pady=5, anchor='center')
    output_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
    output_text.pack(pady=10, padx=10)


    root.mainloop()
if __name__ == "__main__":
    main()
