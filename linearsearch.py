list1=[6, 9, 5, 0, 2, 7, 3, 1, 4, 8]
target=int(input("Pick a number as a target value."))

for i in list1:
    if i==target:
        print(target, "was found.")
        targetIndex=list1.index(target)
        print(targetIndex)
        break

print("No results match '", target, "'")