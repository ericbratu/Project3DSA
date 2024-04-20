# Recipe Finder

Our group, Kitchen Nightmares, created a recipe finder where users are able to input ingredients they have lying around in their fridge and search from a dataset of ~100,000 recipes in order to see what recipes have the most ingredients in common with their input. 

## Usefulness
This solves the problem of food buildup and eventual spoiling from not knowing what to cook with your ingredients!

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tkinter & pandas in your terminal of choice. We used and reccomend VS code's built-in terminal.

```bash
pip install tk
```

```bash
pip install pandas
```


## Usage

To use, run the main file and wait for the pop-up to open. Once open, input ingredients separated by a comma into the search bar (just a comma, not comma and space) and press either the "Search with map" button or "Search with graph" button depending on which data structure you would like to use. From there, it will output the first 50 recipes with the most ingredients in common with the user input in descending order.

## Disclaimer

If multiple recipes have the same number of ingredients in common, they might appear in a different order depending on which data structure you use, but rest assured, they are all still there :P.

## Where Users can Get Help

If users have any issues, they can email group members Eric Bratu, Grace Donath, and Xiaoguo Jia at [eric.bratu@ufl.edu](mailto:eric.bratu@ufl.edu), [gracedonath@ufl.edu](mailto:gracedonath@ufl.edu), and [xiaoguojia@ufl.edu](mailto:xiaoguojia@ufl.edu), respectively


## License

[MIT](https://choosealicense.com/licenses/mit/)