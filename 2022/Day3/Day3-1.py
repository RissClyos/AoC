total = 0
with open("AoC/Day3/Day3Data.txt", "r") as datafile:
    for line in datafile:
        first = line[0:int((len(line)/2))]
        second = line[int((len(line)/2)):]
        for x in first:
            if x in second:
                total += (ord(x)-96) if x.islower() else (ord(x)-38)
                break
print(total)
    