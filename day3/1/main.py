from math import inf, nan
import re


class SchematicNumber:
    def __init__(self, number, x1, x2, x3, y):
        self.number = number
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.y = y
        

def schematic_size():
    width = 0
    height = 0
    with open(file_path, 'r') as file:
        for line in file:
            height += 1
            width = len(line)

    return width, height


def load_numbers(file_path):
    with open(file_path, 'r') as file:
        list_of_numbers = []
        x = 0
        y = 0
        for line in file:
            number = []
            insideNumber = False
            for ch in line:
                if ch.isnumeric():
                    insideNumber = True
                    number.append(ch)
                elif insideNumber == True and ch.isnumeric():
                    number.append(ch)
                elif insideNumber == True and not ch.isnumeric():
                    if number:
                        fullNumber = int(''.join(number))
                        if fullNumber >= 100:
                            list_of_numbers.append(SchematicNumber(
                                number=fullNumber, 
                                x1=x-3,
                                x2=x-2,
                                x3=x-1,
                                y=y))
                        elif fullNumber<=99:
                                list_of_numbers.append(SchematicNumber(
                                number=fullNumber, 
                                x1=nan,
                                x2=x-2,
                                x3=x-1,
                                y=y))
                        elif fullNumber <=9:
                                list_of_numbers.append(SchematicNumber(
                                number=fullNumber, 
                                x1=nan,
                                x2=nan,
                                x3=x-1,
                                y=y))
                        number = []
                x+=1
            y+=1
            x=0
        
        return list_of_numbers


def get_adjacent_numbers(x, y, numbers):
    foundNumbers = []
    for n in reversed(numbers):
        if y == n.y:
            if x-1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
            elif x+1 == n.x1 or x+1 == n.x2 or x+1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
        elif y-1 == n.y:
            if x-1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
            elif x+1 == n.x1 or x+1 == n.x2 or x+1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
            elif x == n.x1 or x == n.x2 or x == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
        elif y+1 == n.y:
            if x-1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
            elif x+1 == n.x1 or x+1 == n.x2 or x+1 == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
            elif x == n.x1 or x == n.x2 or x == n.x3:
                foundNumbers.append(n.number)
                numbers.remove(n)
    
    if len(foundNumbers) == 2:
        return foundNumbers[0] * foundNumbers[1]
    else:
        return 0


def check_schematic(file_path):
    numbers = load_numbers(file_path)
    sum = 0
    with open(file_path, 'r') as file:
        x = 0
        y = 0
        for line in file:
            for ch in line:
                if ch == '*':
                    sum += get_adjacent_numbers(x,y,numbers=numbers)
                x+=1
            y+=1
            x=0
    print(sum)

file_path = r"C:\Users\Grzmociarz\Documents\AdventOfCode\day3\\1\\input.txt"
width, height = schematic_size()
check_schematic(file_path=file_path)


