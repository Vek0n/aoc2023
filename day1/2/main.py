def replace_written_numbers_with_numbers(text):
    x = text.replace("one", "o1e")
    x = x.replace("two", "t2o")
    x = x.replace("three", "t3e")
    x = x.replace("four", "f4r")
    x = x.replace("five", "f5e")
    x = x.replace("six", "s6x")
    x = x.replace("seven", "s7n")
    x = x.replace("eight", "e8t")
    x = x.replace("nine", "n9e")
    return x


with open(r"C:\Users\Grzmociarz\Documents\AdventOfCode\day1\\1\\input.txt", 'r') as file:
    sum = 0
    for line in file:
        firstNum = ""
        lastNum = ""
        
        line = replace_written_numbers_with_numbers(line)

        for s in line:
            if s.isnumeric():
                firstNum = s
                break
        
        for s in line[::-1]:
            if s.isnumeric():
                lastNum = s
                break

        finalNum = int(firstNum + lastNum)
        sum += finalNum
    print(sum)




