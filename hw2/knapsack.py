from random import randint
import sys, os, time, random

#The algorithms used in this program were modeled off
#of the geekforgeeks algorithm to solve the knapsack
#problem, with some changes for the assignment. Their 
#solutiom can be found here: 
#https://www.geeksforgeeks.org/printing-items-01-knapsack/

#fill array with random values
def randomizeArray(array, sizeOfArray, maxRandInt):
    for i in range(0, sizeOfArray):
        array.append(randint(0,maxRandInt))


#recursive knapsack function
def knapsackREC(val, weight, n, W):
    #base case
    if (n < 0 or W == 0):
        return 0

    # If weight of the nth item is
    # more than Knapsack of capacity W,
    # then this item cannot be included
    # in the optimal solution
    if (weight[n] > W):
        return knapsackREC(val, weight, n - 1, W)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        maxValue = max(val[n] + knapsackREC(val, weight, n - 1, W - weight[n]), knapsackREC(val, weight, n - 1, W))
        return maxValue

#dynamic programming solution to knapsack problem
def knapsackDP(val, weight, n, W):
    
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):

            #If in the first row or column of the table
            #set it to 0. It is not used
            if i == 0 or w == 0:
                table[i][w] = 0

            #If the item can be fit in the knapsack,
            #Check if it's better to include it or not
            elif weight[i - 1] <= w:
                table[i][w] = max(val[i - 1] + table[i - 1][w - weight[i - 1]], table[i - 1][w])

            #The item doesn't fit, so don't include it
            else:
                table[i][w] = table[i - 1][w]

    return table[n][W]

#driver code
def run (n, W, dp, naive):
    
    #Set the number of items and max weight here!
    n = 20
    W = 200

    #Set max random integer
    maxRandInt = 20

    #Create and fill arrays with random values
    val = [random.randint(0, 50) for x in range (0, n)]
    weight = [0 for x in range(0, n)]

    while sum(weight) < W:
        weight[random.randint(0, len(weight)-1)] += 1

    #Time the recursive function
    recStartTime = time.time()
    recResult = knapsackREC(val, weight, n - 1, W)
    recTime = time.time() - recStartTime

    #Time the dynamic function
    dpStartTime = time.time()
    dynResult = knapsackDP(val, weight, n, W)
    dpTime = time.time() - dpStartTime

    print(
        "Completed: N =", n, 
        " W =", W, 
        " Rec Time: ", (recTime), 
        " DP Time: ", (dpTime), 
        " Rec Result: ", recResult, 
        " DP Result: ", dynResult, )

def printarray (a):
    for e in a:
        print(e)
    print()

if __name__ == "__main__":

	count = [x for x in range (5)]

	for r in range (1):
		dp = []
		naive = []
		print("==== RUN ", r, " ====")
		for x in count:
			run(x, 100, dp, naive)