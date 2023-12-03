from math import inf
import re

def load_games_list(file_path):
    games = []

    with open(file_path, 'r') as file:
        for line in file:
            game_data = line.split(':', 1)[1].strip()
            subset_strings = [s.strip() for s in game_data.split(';') if s.strip()]
            subsets = []

            for subset in subset_strings:
                subset_dict = {'blue': 0, 'red': 0, 'green': 0}
                color_counts = re.findall(r'(\d+)\s+(blue|red|green)', subset)
                for count, color in color_counts:
                    subset_dict[color] = int(count)
                subsets.append(subset_dict)

            games.append(subsets)
    return games

file_path = r"C:\Users\Grzmociarz\Documents\AdventOfCode\day2\\1\\input.txt"
games_data = load_games_list(file_path)


sum = 0
for game_id, subsets in enumerate(games_data, start=1):
    highestRed = 0
    highestBlue = 0
    highestGreen = 0
    
    for subset in subsets:
        if subset['red'] > highestRed:
            highestRed = subset['red']
        
        if subset['blue'] > highestBlue:
            highestBlue = subset['blue']
        
        if subset['green'] > highestGreen:
            highestGreen = subset['green']
    
    sum += highestRed*highestBlue*highestGreen

print(sum)