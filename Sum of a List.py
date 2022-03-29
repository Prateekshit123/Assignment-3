l = [8,2,3,0,7]

def sum_of_list(l, n):
    if n == 0:
        return l[n]
    return l[n] + sum_of_list(l, n-1)

print("The sum of a given list is :", sum_of_list(l, len(l)-1))