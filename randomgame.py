import csv

with open ('RoboGameLibrary.csv', newline='', encoding="utf8") as csvfile:
    gamereader = csv.reader(csvfile, delimiter=',')
    # for row in gamereader:
    #     # print(','.join(row))
    #     games = list(row[i] for i in cols)
    #     print games
    for lines in gamereader:
        print(lines[1])