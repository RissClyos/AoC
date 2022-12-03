currentElf, elfList = 0, []
with open("AoC/Day_1_data.txt", "r") as datafile:
    for line in datafile:
        if line.strip() == "":
            elfList.append(currentElf)
            currentElf = 0
        else:
            currentElf += int(line)
print(sum(sorted(elfList, reverse = True)[0:3]))
