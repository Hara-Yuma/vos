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
            time.sleep(script.delay["time"])
            if ElemList[LeftTop] <= ElemList[RightTop]:
                script.RangeDrawing(front, front + num - 1, canvas, ElemList, "white")
                LeftTop += 1
            else:
                ElemList.insert(front + i, ElemList.pop(RightTop))
                script.RangeDrawing(front, front + num - 1, canvas, ElemList, "white")
                LeftTop += 1
                RightTop += 1
    return ElemList

def _QuickSort(canvas, ElemList, front, num):
    if num <= 1:
        script.DrawElement(canvas, ElemList, front, "red")
        time.sleep(script.delay["time"])
        script.DrawElement(canvas, ElemList, front, "white")
        return ElemList

    pp = front + num - 1 # means "pivot point"
    lp = front # means "left point"
    rp = front + num - 2 # means "right point"

    script.DrawElement(canvas, ElemList, pp, "red")

    while True:
        while ElemList[lp] < ElemList[pp]:
            script.DrawElement(canvas, ElemList, lp, "red")
            time.sleep(script.delay["time"])
            script.DrawElement(canvas, ElemList, lp, "white")
            lp += 1
            if lp == pp:
                script.DrawElement(canvas, ElemList, pp, "white")
                return _QuickSort(canvas, ElemList, front, num - 1)
        while ElemList[rp] >= ElemList[pp]:
            script.DrawElement(canvas, ElemList, rp, "red")
            time.sleep(script.delay["time"])
            if rp == lp:
                remain = ElemList[pp]
                ElemList[pp] = ElemList[rp]
                ElemList[rp] = remain
                script.DrawElement(canvas, ElemList, pp, "white")
                script.DrawElement(canvas, ElemList, rp, "white")
                ElemList = _QuickSort(canvas, ElemList, front, rp - front)
                ElemList = _QuickSort(canvas, ElemList, rp + 1, pp - rp)
                return ElemList
            script.DrawElement(canvas, ElemList, rp, "white")
            rp -= 1
        remain = ElemList[lp]
        ElemList[lp] = ElemList[rp]
        ElemList[rp] = remain
        script.DrawElement(canvas, ElemList, lp, "white")
        script.DrawElement(canvas, ElemList, rp, "white")
