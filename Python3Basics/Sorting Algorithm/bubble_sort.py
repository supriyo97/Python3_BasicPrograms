def bubble(list):
    for i in range(len(list)-1):
        swap = 0
        for j in range(len(list)-1-i):
            if list[j]>list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                swap+=1
        if(swap == 0):
            break
    return list

list1 = [123,242,12,2424,1231,342,2344]
list2 = ['v','e','t','s','o']
bubble(list1)

bubble(list2)
