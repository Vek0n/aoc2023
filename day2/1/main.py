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
maxRed = 12
maxBlue = 14
maxGreen = 13


for game_id, subsets in enumerate(games_data, start=1):

    possible = True

    for subset in subsets:
        if subset['blue'] > maxBlue or subset['red'] > maxRed or subset['green'] > maxGreen:
            possible = False

    if possible == True:
        sum += game_id

print(sum)