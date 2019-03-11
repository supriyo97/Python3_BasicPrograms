def selection_sort(array):                   #SELECTION SORT function
    for i in range((len(array)-1)):          #array is group of elements/same types of values
         = i                         #minindex is the minimum index fo the array
        for j in range(i+1,len(array)):
            if array[j]<array[minindex]:
                minindex = j
        array[i],array[minindex] = array[minindex],array[i]             #exchange the values between intial values and minimum index
    return a

a = [123,242,12,224,11,5435,212]
selection_sort(a)                            #call the selection_sort funtionn to sort the values in ascending order
