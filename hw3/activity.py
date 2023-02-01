#activity selection is modified from an algorithm that is found on 
#geeksforgeeks.org
#https://www.geeksforgeeks.org/activity-selection-problem-greedy-algo-1/
def activitySelection(array):
    #sort list by finishing time
    array.sort(key = lambda x: x[1])

    #get length of list
    n = len(array)

    selected = []
    print ("The following activities are selected")
 
    # starting with last activity in list
    i = n - 1

    #append the last activity by default because that is where the algorithm is starting
    selected.append(array[i][0])

    #loop through the list in reversed order 
    for index, j in reversed(list(enumerate(array))):
        #compare the current activity's finish time to the previous activity's start time
        #if it's less than the start time then the activity number is pushed to the selected array
        if j[2] <= array[i][1]:
            selected.append(j[0])
            i = index
    #return the selected array but reverse it first to match the sample solution
    return list(reversed(selected))
 
def main():
    f = open('act.txt', 'r')
    selected = []
    set = 1
    for line in f:
        #removing the '\n' from end of each line and converting to integer
        line = line.rstrip()

        #check if has reached the line where there are no leading white space and the length of the selected array is greater than 0
        #then the program has reached a new set of data and should evaluate the current data set that has been collected
        #else, handle the selected of the data into array list that's stored in the selected array
        if ' ' not in line and len(selected) > 0:
            print("Set: " + str(set))

            #test the first result of the array
            #the first loop will always append the number of activities, so we need to pass in an array that skips over the bad data
            if(len(selected[0]) > 1):
                result = activitySelection(selected[0:])
            else:
                result = activitySelection(selected[1:])
            print("Number of activities selected = " + str(len(result)))
            print("Activities: " + str(result) + '\n')
            set += 1
            selected = []
        else:
            selected.append([int(i) for i in line.split()])

    #a final pass that evaluates the rest of the data from the selected array
    if len(selected) > 0:
        print("Set: " + str(set))
        result = activitySelection(selected)
        print("Number of activities selected = " + str(len(result)))
        print("Activities: " + str(result))
    f.close()

if __name__=="__main__":
    main()