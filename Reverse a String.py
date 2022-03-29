s = "1234abcd"

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]

print ("The original string  is : ", s)

print ("The reversed string(using recursion) is : ", reverse(s))