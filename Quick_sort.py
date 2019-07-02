from random import randint # for random array elements and random pivot

def create_random_array(size = 30 , max = 60): # array creation
    return [randint(0,max) for _ in range (size)]

def quicksort(a): #quick sort algorithm
    if len(a) <= 1: #recursive call
        return a
    larger,equal,smaller = [],[],[] #initialize three arrays for the elements of the array
    pivot = a[randint(0,len(a)-1)] #random pivot choice

    for x in range(len(a)): 
        if (a[x] > pivot):
            larger.append(a[x])
        elif (a[x] == pivot):
            equal.append(a[x])
        else :
            smaller.append(a[x])
    
    return quicksort(smaller)+equal+quicksort(larger)

a = create_random_array()
print ("Unsorted: ",a)
k= quicksort(a)
print ("Sorted :",k)


