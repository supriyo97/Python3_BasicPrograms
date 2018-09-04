def descending(l):
    if len(l) <= 1:
        return True
    elif l[0]>=l[1]:
        return descending(l[1:])
    else:
        return False

descending([4,4,3])
