import pandas as pd
import tkinter as tk
from tkinter import scrolledtext
import time
from map import RecipeMap, filter_and_sort_recipes, on_search_button_click

def main():
    # Create recipe map
    recipe_map = RecipeMap()
    
    # Load data from CSV
    df = pd.read_csv('veryfinal.csv')
    for index, row in df.iterrows():
        recipe_name = row['title']
        recipe_ingredients = eval(row['NER'])
        recipe_map.add_recipe(recipe_name, recipe_ingredients)
    
    # Create the main application window
    root = tk.Tk()
    root.title("Recipe Finder")

    # Create a frame for the input and button
    input_frame = tk.Frame(root)
    input_frame.pack(pady=10, padx=10)

    # Create an entry widget for user input
    user_ingredients_entry = tk.Entry(input_frame, width=50)
    user_ingredients_entry.pack(side=tk.LEFT, padx=5)

    # Create a search button
    search_button = tk.Button(input_frame, text="Search", command=lambda: on_search_button_click(recipe_map, user_ingredients_entry, output_text))
    search_button.pack(side=tk.LEFT, padx=5)

    # Create a label centered underneath the entry widget and search button
    hint_label = tk.Label(input_frame, text="*Separate ingredients with a comma!", font=("Helvetica", 10, "italic"))
    hint_label.pack(side=tk.TOP, pady=5, anchor='center')

    # Create a scrolled text widget for output
    output_text = scrolledtext.ScrolledText(root, width=80, height=20, wrap=tk.WORD)
    output_text.pack(pady=10, padx=10)

    # Run the main loop
    root.mainloop()

if __name__ == "__main__":
    main()
