def selection_sort(array):
    for i in range((len(array)-1)):
        minvalue = i
        for j in range(i+1,len(array)):
            if array[j]<array[minvalue]:
                minvalue = j
        array[i],array[minvalue] = array[minvalue],array[i]
    return a

a = [123,242,12,224,11,5435,212]
selection_sort(a)
    
