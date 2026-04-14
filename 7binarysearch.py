list1=[]
listSize=int(input("How many elements would you like in the list? "))
for i in range(listSize):
    element=int(input("List element in integer form." ))
    list1.append(element)
    print("The element has been added.")
print(list1)

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
    elif targetValue<list1[middleIndex]:
        higherIndex=middleIndex-1
    else:
        lowerIndex=middleIndex+1        

if finder==False:
    print("Element was not found. ")