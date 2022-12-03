total = 0
with open("AoC/Day3/Day3Data.txt", "r") as datafile:
    elves = [line.rstrip('\n') for line in datafile]
    groups = [elves[x:x + 3] for x in range(0, len(elves), 3)]
    for group in groups:
        for elf in group[:1]:
            for item in elf:
                if (item in str(group[1:2])) and (item in str(group[2:])) :
                    total += (ord(item)-96) if item.islower() else (ord(item)-38)   
                    break
print(total)
    