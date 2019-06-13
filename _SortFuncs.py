#!/usr/bin/env python3
import time

import script

def _MergeSort(canvas, ElemList, front, num):
    if num == 1:
        script.DrawElement(canvas, ElemList, front, "red")
        time.sleep(script.delay["time"])
        script.DrawElement(canvas, ElemList, front, "white")
        return ElemList

    ElemList = _MergeSort(canvas, ElemList, front, int(num / 2))
    if (num % 2) == 0:
        ElemList = _MergeSort(canvas, ElemList, front + int(num / 2), int(num / 2))
    else:
        ElemList = _MergeSort(canvas, ElemList, front + int(num / 2), int(num / 2) + 1)

    LeftTop = front
    RightTop = front + int(num / 2)

    for i in range(0, num):
        if LeftTop == RightTop:
            break
        elif RightTop == front + num:
            break
        else:
            script.DrawElement(canvas, ElemList, LeftTop, "red")
            script.DrawElement(canvas, ElemList, RightTop, "red")
            if ElemList[LeftTop] <= ElemList[RightTop]:
                script.RangeDrawing(front, front + num - 1, canvas, ElemList, "white")
                LeftTop += 1
            else:
                ElemList.insert(front + i, ElemList.pop(RightTop))
                script.RangeDrawing(front, front + num - 1, canvas, ElemList, "white")
                LeftTop += 1
                RightTop += 1
    return ElemList
