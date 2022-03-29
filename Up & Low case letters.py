s = 'The quick Brow Fox'

def string_test(s):
    d = {"upper_case": 0, "lower_case": 0}
    for i in s:
        if i.isupper():
           d["upper_case"] += 1
        elif i.islower():
           d["lower_case"] += 1
        else:
           pass

    print ("No. of Upper case characters : ", d["upper_case"])
    print ("No. of Lower case Characters : ", d["lower_case"])

string_test(s)