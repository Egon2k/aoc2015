def checkPart1Rule1(line):
    count = 0
    for vovel in ['a','e','i','o','u']:
        count = count + line.count(vovel)
    return (count >= 3)

def checkPart1Rule2(line):
    for i, char in enumerate(line[:-1]):
        if line[i] == line[i+1]:
            return True
    return False

def checkPart1Rule3(line):
    return not("ab" in line or "cd" in line or "pq" in line or "xy" in line)


def checkPart2Rule1(line):
    for i, char in enumerate(line[:-2]):
        if line[i:i+2] in line[i+2:]:
            return True
    return False

def checkPart2Rule2(line):
    for i, char in enumerate(line[:-2]):
        if line[i] == line[i+2]:
            return True
    return False

def checkNicePart1(line):
    return checkPart1Rule1(line) and checkPart1Rule2(line) and checkPart1Rule3(line)

def checkNicePart2(line):
    return checkPart2Rule1(line) and checkPart2Rule2(line)

def part1(data):
    count = 0
    for i in data:
        if checkNicePart1(i):
            count = count + 1
    return count

def part2(data):
    count = 0
    for i in data:
        if checkNicePart2(i):
            count = count + 1
    return count

if __name__ == "__main__":
    data = []

    with open('day05/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
