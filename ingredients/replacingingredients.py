import csv

# Function to perform replacements in the 'NER' column of a row
def perform_replacements(row):
    # Convert 'NER' column string to list
    ner_list = eval(row['NER'])
    
    # Perform replacements
    for i in range(len(ner_list)):
        if ner_list[i] == 'all-purpose':
            ner_list[i] = 'all-purpose flour'

        elif ner_list[i] == 'egg':
            ner_list[i] = 'eggs'

        elif ner_list[i] == 'ground nutmeg':
            ner_list[i] = 'nutmeg'

        elif ner_list[i] == 'extra virgin olive oil':
            ner_list[i] = 'olive oil'
        elif ner_list[i] == 'extra-virgin olive oil':
            ner_list[i] = 'olive oil'

        elif ner_list[i] == 'freshly ground black pepper':
            ner_list[i] = 'black pepper'
        elif ner_list[i] == 'ground black pepper':
            ner_list[i] = 'black pepper'

        elif ner_list[i] == 'red bell pepper':
            ner_list[i] = 'bell pepper'

        elif ner_list[i] == 'green pepper':
            ner_list[i] = 'bell pepper'

        elif ner_list[i] == 'carrot':
            ner_list[i] = 'carrots'

        elif ner_list[i] == 'tomato':
            ner_list[i] = 'tomatoes'

        elif ner_list[i] == 'clove garlic':
            ner_list[i] = 'garlic'

        elif ner_list[i] == 'canola oil':
            ner_list[i] = 'cooking oil'

        elif ner_list[i] == 'vegetable oil':
            ner_list[i] = 'cooking oil'

        elif ner_list[i] == 'oleo':
            ner_list[i] = 'margarine'

    
    
    # Convert list back to string and update 'NER' column in row
    row['NER'] = str(ner_list)

# Read the CSV file and perform replacements
input_file = 'withoutstrangeingredients20000.csv'
output_file = 'modified_withoutstrangeingredients.csv'

with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    
    # Write header to output file
    writer.writeheader()
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Perform replacements in 'NER' column
        perform_replacements(row)
        
        # Write modified row to output file
        writer.writerow(row)

print("Replacement completed. Modified file saved as:", output_file)
