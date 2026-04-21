list1=[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(list1)

listSize=len(list1)

targetValue=int(input("What is your target value? "))
lowerIndex=0
higherIndex=listSize-1

finder=False

while lowerIndex<=higherIndex:
    middleIndex=(lowerIndex+higherIndex)//2
    if targetValue==list1[middleIndex]:
        print("Element has been found at position",middleIndex+1)
        finder=True
        break
    elif targetValue>list1[middleIndex]:
        higherIndex=middleIndex-1
    else:
        lowerIndex=middleIndex+1

if finder==False:
    print("Element was not found. ")