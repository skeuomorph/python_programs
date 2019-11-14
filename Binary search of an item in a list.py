def binarySearch(itemList, item):
    first = 0
    last = len(itemList)-1
    found = False
    while first <= last and not found:
        mid = (first + last) // 2
        if itemList[mid] == item:
            found = True
        else:
            if item < itemList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

print (binarySearch([1,2,3,4,5],6))
print (binarySearch([1,2,3,4,5],5))
        
                
