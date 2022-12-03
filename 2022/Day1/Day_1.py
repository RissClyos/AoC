highestElf = currentElf = 0
with open("AoC/Day_1_data.txt", "r") as datafile:
    for line in datafile:
        if line.strip() == "":
            highestElf = max([currentElf, highestElf])
            currentElf = 0
        else:
            currentElf += int(line)
print(highestElf)
