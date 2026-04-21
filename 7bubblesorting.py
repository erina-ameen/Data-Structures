list1=[]

listSize=int(input("How many elements would you like in the list?"))

for i in range(listSize):
    element=input("Add an element to the list.")
    list1.append(element)

print(list1)

for i in range(listSize):
    for j in range(listSize-i-1):
        if list1[j]>list1[j+1]:
            list1[j], list1[j+1]=list1[j+1], list1[j]

print(list1)