 #!/usr/bin/env python3
import time
import heapq

import script
import _SortFuncs

# Bubble Sort Function #
def BubbleSort(canvas, ElemList, ElemNum):
    for i in range(1, ElemNum):
        for j in reversed(range(i, ElemNum)):
            script.RangeDrawing(j - 1, j, canvas, ElemList, "red")
            if ElemList[j] < ElemList[j - 1]:
                remain = ElemList[j]
                ElemList[j] = ElemList[j - 1]
                ElemList[j - 1] = remain
            time.sleep(script.delay["time"])
            script.RangeDrawing(j - 1, j, canvas, ElemList, "white")
    return ElemList

# Selection Sort Function #
def SelectionSort(canvas, ElemList, ElemNum):
    for i in range(0, ElemNum):
        min = i
        script.DrawElement(canvas, ElemList, i, "red")
        for j in range(i, ElemNum):
            script.DrawElement(canvas, ElemList, j, "red")
            if ElemList[min] > ElemList[j]:
                min = j
            time.sleep(script.delay["time"])
            script.DrawElement(canvas, ElemList, j, "white")
        remain = ElemList[i]
        ElemList[i] = ElemList[min]
        ElemList[min] = remain
        script.DrawElement(canvas, ElemList, i, "white")
        script.DrawElement(canvas, ElemList, min, "white")
    return ElemList

# Insert Sort Function #
def InsertSort(canvas, ElemList, ElemNum):
    for i in range(1, ElemNum):
        script.DrawElement(canvas, ElemList, i, "red")
        for j in reversed(range(0, i)):
            script.DrawElement(canvas, ElemList, j, "red")
            if ElemList[i] > ElemList[j]:
                ElemList.insert(j + 1, ElemList.pop(i))
                script.RangeDrawing(0, i, canvas, ElemList, "white")
                break
            elif j == 0:
                ElemList.insert(0, ElemList.pop(i))
                script.RangeDrawing(0, i, canvas, ElemList, "white")
            else:
                script.DrawElement(canvas, ElemList, j, "white")
        time.sleep(script.delay["time"])
    return ElemList

# Heap Sort Function #
def HeapSort(canvas, ElemList, ElemNum):
    heap = []
    for i in range(0, ElemNum):
        script.DrawElement(canvas, ElemList, i, "red")
        time.sleep(script.delay["time"])
        script.DrawElement(canvas, ElemList, i, "white")
        heapq.heappush(heap, ElemList[i])
        script.RangeDrawing(0, i, canvas, heap, "white")
    for i in range(0, ElemNum):
        ElemList[i] = heapq.heappop(heap)
        script.RangeDrawing(i, ElemNum - 1, canvas, ElemList[:i+1] + heap, "white")
    return ElemList

# Merge Sort Function #
def MergeSort(canvas, ElemList, ElemNum):
    return _SortFuncs._MergeSort(canvas, ElemList, 0, ElemNum)

# Quick Sort Function #
def QuickSort(canvas, ElemList, ElemNum):
    return _SortFuncs._QuickSort(canvas, ElemList, 0, ElemNum)
