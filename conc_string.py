
# concatenating strings


def concatenation():
    list1 = ['Hello', 'Take']
    list2 = ['Dear', 'Sir']
    res = [x + " " + y for x in list1 for y in list2]

    print(res)


concatenation()
