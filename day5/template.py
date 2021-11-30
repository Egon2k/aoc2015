import hashlib

def checkVovels(line):
    count = 0
    for vovel in ['a','e','i','o','u']:
        if vovel in line:
            count = count + 1
    return (count >= 3)

def checkDoubles(line):
    for i, char in enumerate(line[:-1]):
        if line[i] == line[i+1]:
            return True
    return False

def checkBadStrings(line):
    return "ab" in line or "cd" in line or "pq" in line or "xy" in line

def part1(data):
    count = 0
    for i in data:
        if checkVovels(i) and checkDoubles(i) and not(checkBadStrings(i)):
            count = count + 1
        
    return count
        

def part2(data):
    pass
        
if __name__ == "__main__":
    data = []

    with open('day5/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    #print(part2(data))
