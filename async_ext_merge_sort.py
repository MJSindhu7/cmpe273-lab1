import os
import asyncio

data = []
async def read_data(file):
    with open(file) as f:
        for i in f:
            data.append(int(i))

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
        with open("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/output/async_sorted.txt",m)as ff:
                for obj in result:
                        ff.write('%s\n' % obj)

async def sort():
    for i in range(1,11):
        await read_data("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/input/unsorted_{}.txt".format(i))
    qsort(data, 0, len(data)-1)
    write(data,'w')

asyncio.run(sort())