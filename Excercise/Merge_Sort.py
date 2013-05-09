import operator, random

def merge(left, right, compare):
    
    
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right) :
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result



def mergeSort(L, compare = operator.lt):
    
    if len(L) < 2:
        return L[:]
    else:
        middle = int(len(L) / 2)
        left = mergeSort(L[:middle], compare)
        # print('Applying mergeSort on: ' + str(left))
        right = mergeSort(L[middle:], compare)
        # print('Applying mergeSort on: ' + str(right))
        
        return merge(left, right, compare)

L = [68, 49, 2]
print(L)
print(mergeSort(L))


