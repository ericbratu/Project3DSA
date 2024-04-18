import pandas as pd

df = pd.read_csv('veryfinal.csv')

print(df.shape)

# map
recipe_map = {}

for index, row in df.iterrows():
     recipeName = row['title']
     recipeIngredients = eval(row['NER']) 
    
     recipe_map[recipeName] = recipeIngredients

#print(len(recipe_map))
return recipe_map



def filter_and_sort_recipes(recipe_map, user_ingredients):
    common_ingredients_count = {}
    
    # Filters and calculates the count of common ingredients
    for recipe, recipeIngredients in recipe_map.items():
        # Calculate the intersection of user's input ingredients and recipe ingredients
        common_ingredients = set(recipeIngredients) & set(user_ingredients)
        
        # If common ingredients, store the count
        if common_ingredients:
            common_ingredients_count[recipe] = len(common_ingredients)
    
    # Sort recipes by the num ingredients in common with user input, in descending order
    sorted_recipes = sorted(common_ingredients_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_recipes


def main():
    file_path = 'veryfinal.csv'
    
    #xiaoguo
    
    # Get user input (list of ingredients)
    user_ingredients = input("Enter ingredients (comma separated): ").split(',')
    
    # Filter and sort recipes based on user input
    sorted_recipes = filter_and_sort_recipes(recipe_map, user_ingredients)
    
    # Display sorted recipes
    print("Recipes sorted by most ingredients in common with your input:")
    for recipe, count in sorted_recipes:
        print(f"{recipe}: {count} ingredients in common")

if __name__ == "__main__":
    main()
