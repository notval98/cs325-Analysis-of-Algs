def dynamic(val, weight, n, W):

    #Create and initialize the table
    table = [[0 for x in range(W + 1)] for x in range(n + 1)]

    #Iterate through the entire table
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

    #Save result to total variable
    total = table[n][W]

    #Create list for when function returns and
    #append the total to the start
    returnList = []
    returnList.append(total)

    #Create a list to hold the items used
    totalItemsList = []

    #Iterate through the table to find items used
    w = W
    for i in range(n, 0, -1):

        #Create list to hold items
        itemsList = []

        #If total is <= 0, no items were used
        if total <= 0:
            break

        #If we find total, that item column corresponds
        #to the item used
        if total == table[i - 1][w]:
            continue

        #So add the item number and reduce the value and weight totals
        else:
            itemsList.append(i)
            total = total - val[i - 1]
            w = w - weight[i - 1]

        #Add the entire list to the original list
        totalItemsList.append(itemsList)

    #Append items list to returnList and return
    returnList.append(totalItemsList)
    return returnList

def readFile():

    #Open shopping.txt for reading
    f = open("shopping.txt", "r")

    #Get the number of cases
    numCases = f.readline()

    #Create arrays to hold all data from file
    itemPrice = []
    itemWeight = []
    peopleMaxWeight = []
    casesList = []

    #Iterate through file the number of cases there are present
    i = 0
    while (i < int(numCases)):

        #Create lists that will case data
        caseValues = []
        casePrices = []
        caseWeight = []
        casePeopleWeight = []

        #Determine the number of items and add to caseValues
        numItems = f.readline()
        caseValues.append(int(numItems))

        #Read and place item price and weight in
        #appropriate list
        for j in range(int(numItems)):
            itemLine = f.readline().split()
            casePrices.append(int(itemLine[0]))
            caseWeight.append(int(itemLine[1]))

        #Determine the number of people and add to caseValues
        numPeople = f.readline()
        caseValues.append(int(numPeople))

        #Read the max weight for each person and put
        #into list
        for k in range(int(numPeople)):
            itemLine = f.readline()
            casePeopleWeight.append(int(itemLine))

        #Append each case list to the total list
        itemPrice.append(casePrices)
        itemWeight.append(caseWeight)
        peopleMaxWeight.append(casePeopleWeight)
        casesList.append(caseValues)

        #Increment the case counter
        i = i + 1

    #Return all the lists
    return itemPrice, itemWeight, peopleMaxWeight, casesList

def printResult(listToWrite, caseNum):
    #Determine how many people to account for
    numPeople = len(listToWrite)

    #Open file for writing and write the case number
    print("Test Case {0}\n".format(caseNum + 1))

    #Add the first value of each list in listToWrite
    #to get total value and write it to file
    value = 0
    for i in range(numPeople):
        value += listToWrite[i][0]

    print("Total Price {0}\n".format(value))

    #For each family memeber
    for i in range(numPeople):
        #Write the member numer
        print("{0}: ".format((i + 1)))

        #And write each item number in the list
        for j in range(len(listToWrite[i][1])):
            print("{0} ".format((listToWrite[i][1][j][0])))

        
def shopping(itemsPrice, itemsWeight, maxWeights):

    #Get number of people and items
    numPeople = len(maxWeights)
    numItems = len(itemsPrice)

    #For each person, call dynamic and append result to peopleTotals
    peopleTotals = []
    for i in range(numPeople):
        peopleTotals.append(dynamic(itemsPrice, itemsWeight, numItems, maxWeights[i]))

    #Return list with totals of every case
    return peopleTotals

if __name__ == '__main__':

    #Initialize lists to hold input data
    itemsPrice = []
    itemsWeight = []
    maxWeights = []
    caseDetails = []

    #Get input data from file
    itemsPrice, itemsWeight, maxWeights, caseDetails = readFile()

    #Get the number of cases  in file
    numCases = len(caseDetails)

    #For each case, call shopping and print results to file
    for i in range(numCases):
        results = shopping(itemsPrice[i], itemsWeight[i], maxWeights[i])
        printResult(results, i)