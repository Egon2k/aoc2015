def part1(data):
    up = data.count('(')
    down = data.count(')')
    return up - down

def part2(data):
    for i in range(len(data)):
        if part1(data[:i]) == -1:
            return i

if __name__ == "__main__":
    data = []

    with open('day1/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data[0]))
    print(part2(data[0]))
