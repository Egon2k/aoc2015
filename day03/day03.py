def walk(currPos, dir):
    if dir == ">":
        currPos[0] = currPos[0] + 1
    elif dir == "<":
        currPos[0] = currPos[0] - 1
    elif dir == "^":
        currPos[1] = currPos[1] + 1
    elif dir == "v":
        currPos[1] = currPos[1] - 1
    return currPos

def part1(data):
    currPos = [0,0]
    posList = list()
    posList.append(tuple(currPos))
    for i in data:
        currPos = walk(currPos, i)

        if tuple(currPos) not in posList:
            posList.append(tuple(currPos))
    return posList
        

def part2(data):
    santa = [dir for x,dir in enumerate(data) if x%2 == 0]
    robo = [dir for x,dir in enumerate(data) if x%2 == 1]
    posListSanta = part1(santa)
    posListRobo = part1(robo)
    return list(set(posListSanta) | set(posListRobo))
        
if __name__ == "__main__":
    data = []

    with open('day03/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(len(part1(data[0])))
    print(len(part2(data[0])))
