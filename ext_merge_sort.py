import os
import heapq
import asyncio


def read_data(file):
    data1 = []
    with open(file) as f:
        for i in f:
            data1.append(int(i))
        data1=[int(x) for x in data1]
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

def write_ind_files(file, sort_list):
    with open(file, 'w') as f:
        for i in sort_list:
            f.write('%s\n' % i)

def write(value):
        with open("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/output/async_sorted.txt",'w')as ff:
            ff.write(str(value) + "\n")

def sort(i):
    data = []
    data = read_data("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/input/unsorted_{}.txt".format(i))
    qsort(data, 0, len(data)-1)
    write_ind_files("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/output/sorted_{}.txt".format(i), data)

def combine():
    sort_files = []
    for i in range(1,11):
        sort_files.append(open("/Users/sindhuram/Documents/Mine/SJSU/Sem3/273-Sithu/Lab1/MyLab1/output/sorted_{}.txt".format(i), 'r'))
    heap = [(int(sort_files[file].readline().strip()), file) for file in range(len(sort_files))]
    
    heapq.heapify(heap)
    while heap:
        small, file = heapq.heappop(heap)
        write(small)

        value = sort_files[file].readline()
        if value:
            heapq.heappush(heap, (int(value.strip()), file))


def main():
    for i in range(1,11):
        sort(i)
        combine()
        
main()