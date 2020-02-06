import os
def read_data():
    data = []
    for i in range(1,11):
        with open("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/input/unsorted_{}.txt".format(i)) as f:
            for i in f:
                data.append(i)
            data1=[int(x) for x in data]
    return data1


def partition(arr,low,high):
    i = low-1
    pivot = arr[high]
    for j in range(low,high):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def qsort(arr, low, high):
    if low<high:
        pi = partition(arr,low,high)
        qsort(arr, low, pi-1)
        qsort(arr, pi+1, high)
    pass

def write(result,m):
        with open("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/output/sorted.txt",m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)
def sort():
    x = read_data()
    qsort(x, 0, len(x)-1)
    write(x,'w')
    print(len(x))
sort()