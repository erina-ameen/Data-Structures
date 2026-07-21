#recursion-repeating function (for example, when finding the sum of n numbers the repeated fuction is addition)

def sum_finder(n):
    if n==1:
        return 1
    return n+sum_finder(n-1)

print(sum_finder(10))