import csv

def knapsack(S, W, max_weight):
    B = [[None for x in range(max_weight)] for y in range(len(W) + 1)]
    for i in range(max_weight):
        B[0][i] = 0
    for row in range(1, len(W) + 1):
        for w in range(max_weight):
            k = row - 1
            if W[k] > w:
                B[row][w] = B[row - 1][w]
            else:
                B[row][w] = max(B[row - 1][w], B[row-1][w - W[k]] + S[k])
    bit_result = [0 for x in range(len(W))]
    start_col = max_weight - 1
    start_row = len(W)
    max_profit = B[start_row][start_col]
    print()
    show_table = input("Would you like to see DP table (unrecommended for huge tables) T/F: ")
    print()
    if show_table == "T":
        for i in range(len(B)):
            for j in range(len(B[0])):
                print("{} ".format(B[i][j]), end="")
            print()    
    print()    
    print("The max benefit is {}".format(max_profit))
    print()
    while start_row != 0:
        if (B[start_row - 1][start_col] != B[start_row][start_col]):
            bit_result[start_row -1] =1
            max_profit -= S[start_row - 1]
            start_row -= 1
            for i in range(max_weight):
                if (B[start_row][i] == max_profit):
                    start_col = i
        else:
            start_row -= 1
    return bit_result

def knapsack_problem():
    print("Knapsack Solver")
    print("Please upload .csv data to Upload directory")
    print("The fomrat would be first row: weights, second row: benefits (no headers)")
    
    fi = input("what is the file name (end with .csv)? ")
    maxlim = int(input("Thanks, and what is the weight limit? "))
    print("Ok, calculating the maximal solution for you...")

    try:
        with open("./upload/" + fi) as csv_file:
                csv_reader = list(csv.reader(csv_file, delimiter=','))
    except:
        print("ERROR: csv file not found")
        return
    S = csv_reader[1]
    W = csv_reader[0]
    for i in range(len(S)):
        S[i] = int(S[i])
        W[i] = int(W[i])
    result = knapsack(S, W, maxlim)
    for i in range(len(result)):
        if result[i] == 0:
            print("item {}: not included".format(i))
        else:
            print("item {}: included".format(i))
        