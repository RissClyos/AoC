totalScore = 0
scores = { "X" : 1, "Y" : 2, "Z" : 3}
with open("AoC/Day2/Day2_Data.txt", "r") as datafile:
    for line in datafile:
        if line[0] == "A":
            if line[2] == "X":
                totalScore += 3
            elif line[2] == "Y":
                totalScore += 6
        elif line[0] == "B":
            if line[2] == "Y":
                totalScore += 3
            elif line[2] == "Z":
                totalScore += 6
        else:
            if line[2] == "Z":
                totalScore += 3
            elif line[2] == "X":
                totalScore += 6
        totalScore += scores[line[2]]
print("Total Score:", totalScore)