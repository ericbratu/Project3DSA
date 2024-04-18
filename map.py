import pandas as pd

df = pd.read_csv('veryfinal.csv')

print(df.shape)

# map
recipe_map = {}

for index, row in df.iterrows():
     recipeName = row['title']
     recipeIngredients = eval(row['NER']) 
    
     recipe_map[recipeName] = recipeIngredients

print(len(recipe_map))
