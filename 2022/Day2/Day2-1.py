totalScore = 0
with open("AoC/Day2/Day2_Data.txt", "r") as datafile:
    for line in datafile:
        if line[0] == "A":
            if line[2] == "X":
                totalScore += 3
            elif line[2] == "Y":
                totalScore += 4
            else:
                totalScore += 8
        elif line[0] == "B":
            if line[2] == "X":
                totalScore += 1
            elif line[2] == "Y":
                totalScore += 5
            else:
                totalScore += 9
        else:
            if line[2] == "X":
                totalScore += 2
            elif line[2] == "Y":
                totalScore += 6
            else:
                totalScore += 7
print("Total Score:", totalScore)
