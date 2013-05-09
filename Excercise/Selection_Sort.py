import random

def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
    return L

list = [4,1,9,8,3]
print('Unsorted list is :'),
print(list)
print('Sorted list is : '), 
print selSort(list)
