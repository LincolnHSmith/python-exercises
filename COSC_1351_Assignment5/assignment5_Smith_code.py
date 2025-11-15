#Lincoln Smith, COSC 1351 Dr. Mardini
import random
#Function to generate random list
def randList(l,a,b):
    myList = []#create empty list
    for i in range(l):#fill list with random values up to desired length
        myList.append(random.randint(a,b))
    return myList#return randomized list

#linear search function
def linSearch(myList,val):
    for i in range(len(myList)):#search thru list's index for val
        if myList[i]==val:#check if list contains val at said index
            return i+1#if so, give user the index of the match
    return len(myList)#if not found, return i is it is no. of comparisons

#selection sort function
def selectSort(myList):
    for i in range(len(myList)-1):#main loop for sort
        minPosition=i#set value to be swapped
        
        for j in range(minPosition, len(myList)):#search for min value
            if myList[j]<myList[minPosition]:
                minPosition = j#if smaller value is found, minPos is set to said value
        
        temp = myList[i]#store number
        myList[i] = myList[minPosition]#replace with sma
        myList[minPosition] = temp#finish the swap
    
    return myList#return sorted list

#binary search function
def binarySearch(myList,val):
    