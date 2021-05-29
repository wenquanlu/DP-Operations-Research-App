import csv

def resource_allocation():

    print("Resource Allocation (AKA, Capital Budgeting)")
    print("Please upload .csv data to Upload directory")
    print("The fomrat would be 'Investment,Benefit,Benefit...'")
    print("Investment need to be sorted in increasing order down the column with equal increment from 0")

    fi = input("what is the file name (end with .csv)? ")
    maxlim = int(input("Thanks, and what is the investment limit? "))
    print("Ok, calculating the maximal solution for you...")

    try:
        with open("./upload/" + fi) as csv_file:
                csv_reader = list(csv.reader(csv_file, delimiter=','))
    except:
        print("ERROR: csv file not found")
        return

    for i in range(1, len(csv_reader)):
        for j in range(len(csv_reader[0])):
            csv_reader[i][j] = int(csv_reader[i][j])

    proj = len(csv_reader[0]) - 1
    level = len(csv_reader) - 1

    v = [[[0,0] for x in range(maxlim)] for y in range(proj + 1)]
    for i in range(1, proj + 1):
        for j in range(maxlim):
            for k in range(level):
                if j < k:
                    v[i][j][0] = max(v[i][j][0], v[i-1][j][0])
                else:
                    if v[i][j][0] < v[i-1][j - k][0] + csv_reader[k+1][i]:
                        v[i][j][0] = v[i-1][j - k][0] + csv_reader[k+1][i]
                        v[i][j][1] = k   
    print()
    show_table = input("Would you like to see DP table (unrecommended for huge tables) T/F: ")
    if show_table == "T":
        for i in range(1, proj + 1):
            for j in range(maxlim):
                print(v[i][j], " ", end="")
            print()

    rewind_start = proj
    max_value = max(v[-1][j][0] for j in range(maxlim))
    print()
    print("The max profit is {}".format(max_value))
    print("plan:")
    def find_j(v, i, target):
        for m in range(len(v[i])):
            if (v[i][m][0] == target):
                return m

    while rewind_start > 0:
        j = find_j(v, rewind_start, max_value)
        e = v[rewind_start][j]
        print("project {}: investment level: {}".format(rewind_start, e[1]))
        max_value -= csv_reader[e[1]+1][rewind_start]
        rewind_start -= 1

