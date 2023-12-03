with open(r"C:\Users\Grzmociarz\Documents\AdventOfCode\day1\\1\\input.txt", 'r') as file:
    sum = 0
    for line in file:
        firstNum = ""
        lastNum = ""
        
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




