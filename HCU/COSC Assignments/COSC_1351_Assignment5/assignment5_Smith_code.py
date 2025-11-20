#Lincoln Smith, COSC 1351 Dr. Mardini
#This program will define functions in order to generate a random list, sort the list, and test and compare sorting algorithms on said list
import random
#Function to generate random list
def randList(l,a,b):
    myList = []#create empty list
    for i in range(l):#fill list with random values up to desired length
        myList.append(random.randint(a,b))
    return myList#return randomized list

#linear search function, will search down the list until value is found
def linSearch(myList,val):
    for i in range(len(myList)):#search thru list's index for val
        if myList[i]==val:#check if list contains val at said index
            return i+1#if so, give user the index of the match
    return len(myList)#if not found, return i is it is no. of comparisons

#selection sort function, will swap values until list is sorted
def selectSort(myList):
    for i in range(len(myList)-1):#main loop for sort
        minPosition=i#set value to be swapped
        
        for j in range(minPosition, len(myList)):#search for min value
            if myList[j]<myList[minPosition]:
                minPosition = j#if smaller value is found, minPos is set to said value
        
        temp = myList[i]#store number
        myList[i] = myList[minPosition]#replace with small
        myList[minPosition] = temp#finish the swap
    
    return myList#return sorted list

#binary search function, will split list continuously until val is found (or not), and will return no. of comparisons
def binarySearch(myList,val):
    count = 0 # no. of comparisons
    first = 0; last = len(myList)-1 # set up pos variables
    while first<=last: #until list is 1 value
        mid = (first+last)//2 #set middle marker
        if val>myList[mid]: #greater half
            count+=1
            first=mid+1 #value on 'right hand' side
        elif val<myList[mid]:
            count+=1
            last = mid-1 #value on 'left hand' side
        else:
            count+=1
            return count #return once found
    return count #still return if not found

#comparison function, will create a table that tests the above searching algorithms and compares theie no. of passes, before noting observations
def search_comparison():
    sizes = [1000, 10000, 100000] #list of sizes to test. note: program could not progress past 100000, limited size. 
    print("List size         Linear Comparisons       Binary Comparisons") #format chart
    print("-------------------------------------------------------------")
    for size in sizes: #test algorithm for each size in list
        testList = randList(size,1,size) #generate random list of size, range will be size in order to avoid too many duplicates
        testList = selectSort(testList) #sort generated list
        linearComp = linSearch(testList, -1) #test for linear comparisons
        binComp = binarySearch(testList, -1) #test for binary comparisons
        print(f"{size}\t\t  {linearComp}\t\t           {binComp}") #print results in chart
    print("Observations:")
    print("With each increase, it seems that the no. of comparisons for the linear search function increases at a steady, linear rate, equal to the increase in size of each list.\n However, the binary search comparisons increase at a much slower rate, as its overall operation is much quicker and extremely efficient compared to the linear algorithm.")
search_comparison() #run test