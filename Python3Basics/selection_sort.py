def selection_sort(array):                   #SELECTION SORT function
    for i in range((len(array)-1)):          #array is group of elements/same types of values
        minvalue = i                         #minvalue is the minimum value
        for j in range(i+1,len(array)):
            if array[j]<array[minvalue]:
                minvalue = j
        array[i],array[minvalue] = array[minvalue],array[i]             #exchange the values between intial values and minimum values
    return a

a = [123,242,12,224,11,5435,212]
selection_sort(a)                            #call the selection_sort funtionn to sort the values in ascending order
