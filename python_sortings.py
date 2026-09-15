data=[10,42,66,2334,13215,65467,577,22,1,9]
                                        #INSERTION
def insertion_sort(data):                               
    for i in range(1, len(data)):                       #represents current value position
        for o in range(i-1, -1, -1):                    #inner loop starts at -1 and go back to -1
            if data[o]>data[o+1]:                       #o loop checks if num in position o is higher than o+1 
                data[o],data[o+1]=data[o+1],data[o]     #moves smaller value to the left
            else:                       
                break                                   #breaks when pairs are in order
    print(data) 
def insertion_sort(data):
    for i in range(1,len(data)):                        #creates position for values
        o = i-1                                    #for each position in list:
        while data[o]>data[o+1] and o>=0:               #checks if num in position o is higher than o+1 and position is not negative
            data[o],data[o+1]=data[o+1],data[o]         #replaces values in the correct order
            o-=1                                        #going in reversed order to the beggining(for all list)
    print(data)
def insertion_sort(data):
    for i in range(1,len(data)):
        current=data[i]
        for o in range(i-1,-1,-1):
            if data[o]>current:
                data[o+1]=data[o]
            else:
                break
    print(data)
# + revrite sorting with current number

                                        #SELECTION
def selection_sort(data):
    for i in range(0    ,len(data)-1):                  #outer loop for positions
        minnum=i                                   #marking first value as min
        for o in range(i+1,len(data)):                  #inner loop for each new sorted value
            if data[o]<data[minnum]:                    #checks if any value is smaller than value marked as min
                minnum=o                           #if there are such value, rewrites it
        if minnum!=i:                                   #checks if they are not equal
            data[i],data[minnum]=data[minnum],data[i]   #replaces them and repeat till last position is placed
    print(data)
                                        #BUBBLE
def bubble_sort(data):
    for i in range(0,len(data)-1):                       #set positions(the last value is sorted)
        for o in range(0,len(data)-1-i):                 #
            if data[o]>data[o+1]:
                data[o],data[o+1]=data[o+1],data[o]
    print(data)
                                        #MERGE
def merge_sort(A,first,mid,last):
    L=A[first:mid]
    R=A[mid:last+1]
    L.append(999999999)
    R.append(999999999)
    i=x=0
    for o in range(first,last+1):
        if L[i]<=R[x]:
            A[o]=L[i]
            i+=1
        else:
            A[o]=R[x]
            x+=1
            # WTF S THIS
                                        #QUICK
def quick_sort():
    ...
    # 2 separate lessons for 2 last methods
                                        #STALIN
def stalin_sort(data):
    i=0
    while i<len(data)-1:
        if data[i]>data[i+1]:
            data.pop(i+1)
        else:
            i+=1
    print(data)
stalin_sort(data)