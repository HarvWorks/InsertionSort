import random
import time
array = []
for i in range(0,10000):
    array.append(int(round(random.random()*1000000)))
print array

startTime = time.time()
def insertionSort(arr):
    sortNum = 2
    length = len(arr)
    if(arr[0]>arr[1]):
        temp = arr[0]
        arr[0] = arr[1]
        arr[1] = temp
    while sortNum < length:
        ind = sortNum-1
        temp = arr[sortNum]
        while (temp <= arr[ind] and ind >=0):
            arr[ind+1]=arr[ind]
            ind -= 1
        arr[ind+1] = temp
        sortNum += 1
    print arr

insertionSort(array)
endTime = time.time()

print ("Insertion Sort took: %s seconds." %(endTime - startTime)) # takes about 3.8 seconds
