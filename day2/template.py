def part1(data):
    ret = 0
    for i in data:
        sizes = [int(e) for e in i.split('x')]
        ret = ret + sizes[0] * sizes[1] * 2
        ret = ret + sizes[0] * sizes[2] * 2
        ret = ret + sizes[1] * sizes[2] * 2
        ret = ret + min(sizes[0] * sizes[1], \
                        sizes[0] * sizes[2], \
                        sizes[1] * sizes[2])
    return ret
        

def part2(data):
    ret = 0
    for i in data:
        sizes = [int(e) for e in i.split('x')]
        sizes.sort()
        ret = ret + 2*sizes[0] + 2*sizes[1]
        ret = ret + (sizes[0] * sizes[1] * sizes[2])
    return ret 
        
if __name__ == "__main__":
    data = []

    with open('day2/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data))
    print(part2(data))
