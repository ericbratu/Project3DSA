import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('final.csv')

# Check for duplicate titles
duplicate_titles = df[df.duplicated(subset=['title'], keep=False)]

if not duplicate_titles.empty:
    print("Duplicate Titles Found:")
    print(duplicate_titles)
else:
    print("No Duplicate Titles Found.")



# df = pd.read_csv('veryfinal.csv')

# # Print the first row
# print("First Row:")
# print(df.head(1))

# # Print the last row
# print("\nLast Row:")
# print(df.tail(1))

# # # print the number of rows and columns
# # print(df.shape)

# # map
# recipe_map = {}

# for index, row in df.iterrows():
#     recipeName = row['title']
#     recipeIngredients = eval(row['NER']) 
    
#     recipe_map[recipeName] = recipeIngredients

# # Get the first entry of the recipe map
# first_entry = next(iter(recipe_map.items()))
# print("\nFirst Entry:")
# print("Recipe:", first_entry[0])
# print("Ingredients:", first_entry[1])

# # Get the last entry of the recipe map
# last_entry = list(recipe_map.items())[-1]
# print("\nLast Entry:")
# print("Recipe:", last_entry[0])
# print("Ingredients:", last_entry[1])

# print(len(recipe_map))
