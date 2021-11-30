import hashlib

def part1(data):
    for i in range(9999999):
        string = data + str(i)
        res = hashlib.md5(string.encode('utf-8')).hexdigest()
        if res.startswith("00000"):
            return i
        

def part2(data):
    for i in range(9999999):
        string = data + str(i)
        res = hashlib.md5(string.encode('utf-8')).hexdigest()
        if res.startswith("000000"):
            return i
        
if __name__ == "__main__":
    data = []

    with open('day04/data.txt') as f:
        for line in f:
            data.append(line.strip())

    print(part1(data[0]))
    print(part2(data[0]))
