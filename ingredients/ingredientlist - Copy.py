import csv
from collections import Counter
import ast

# Function to extract ingredients from a row and update the counter
def update_counter(row, counter):
    ingredients = ast.literal_eval(row['NER'])  # Convert string representation of list to actual list
    counter.update(ingredients)

# Read the CSV file
input_file = 'withoutstrangeingredients20000.csv'
output_file = 'ingredientlist.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Initialize a counter to store ingredient occurrences
    ingredient_counter = Counter()
    
    # Iterate over each row in the CSV file
    for row in reader:
        update_counter(row, ingredient_counter)

# Write the ingredient occurrences to a new CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Ingredient', 'Occurrences']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    
    # Write each ingredient and its occurrence count
    for ingredient, count in ingredient_counter.items():
        writer.writerow({'Ingredient': ingredient, 'Occurrences': count})

print("done")
