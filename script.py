#!/usr/bin/env python3
import tkinter as tk
import random
import time

import SortFuncs

# Global variables #
GW = 1800 # means "Graph Width"
GH = 1000 # means "Graph Height"

delay = {"time": 0}

ElemSize = {}

# Warning Function #
def warning(text):
    WarningWindow = tk.Toplevel()
    WarningWindow.geometry("500x100")
    WarningWindow.title("Warning")
    WarningWindow.resizable(0, 0)
    MessageLabel = tk.Label(WarningWindow, text = text)
    MessageLabel.pack(pady = 10)
    def finish(event):
        WarningWindow.destroy()
    OkButton = tk.Button(WarningWindow, text = "OK", width = 4)
    OkButton.pack(pady = 10)
    OkButton.bind("<Button-1>", finish)
    WarningWindow.mainloop()

# Draw Element Function #
## This function can draw an element of graph
## by receiving the canvs, the position of the element(num),
## and the color of the element
def DrawElement(canvas, ElemList, num, color):
    canvas.delete("e{}".format(num))
    x0 = num * ElemSize["w"]
    y0 = GH
    x1 = (num + 1) * ElemSize["w"]
    y1 = GH - (ElemList[num] * ElemSize["h"])
    canvas.create_rectangle(x0, y0, x1, y1, fill = color, tag = "e{}".format(num))
    canvas.update()

# Range Drawing Function #
## This function can draw a graph of a given range
def RangeDrawing(start, goal, canvas, ElemList, color):
    for i in range(start, goal + 1):
        DrawElement(canvas, ElemList, i, color)

# Draw Graph Function #
## Open the window for drawing a graph,
## and then, call the sort function selected by user
def DrawGraph(SortType, ElemNum):
    if (ElemNum <= 0) or (1000 < ElemNum):
        warning("\"Number of Elements to sort\" should be integer between 1 to 1000")
        return
    GraphWindow = tk.Toplevel()
    GraphWindow.geometry("{}x{}".format(GW, GH))
    GraphWindow.title("Graph")
    GraphWindow.resizable(0, 0)

    ElemSize["w"] = GW / ElemNum
    ElemSize["h"] = GH / ElemNum

    canvas = tk.Canvas(GraphWindow, width = GW, height = GH)
    canvas.create_rectangle(0, 0, GW, GH, fill = "black")

    ElemList = []
    for i in range(0, ElemNum):
        ElemList.append(i + 1)
    random.shuffle(ElemList)
    for i in range(0, ElemNum):
        DrawElement(canvas, ElemList, i, "white")

    canvas.place(x = 0, y = 0)

    if SortType == 0:
        ElemList = SortFuncs.BubbleSort(canvas, ElemList, ElemNum)
    elif SortType == 1:
        ElemList = SortFuncs.SelectionSort(canvas, ElemList, ElemNum)
    elif SortType == 2:
        ElemList = SortFuncs.InsertionSort(canvas, ElemList, ElemNum)
    elif SortType == 3:
        ElemList = SortFuncs.HeapSort(canvas, ElemList, ElemNum)
    elif SortType == 4:
        ElemList = SortFuncs.MergeSort(canvas, ElemList, ElemNum)
    elif SortType == 5:
        ElemList = SortFuncs.QuickSort(canvas, ElemList, ElemNum)

    if ElemNum > 200:
        d = 0
    else:
        d = 0.01

    for i in range(0, ElemNum):
        if ElemList[i] == i + 1:
            DrawElement(canvas, ElemList, i, "green")
            ResultMessage = "Success!!"
        else:
            ResultMessage = "Faild..."
            break
        time.sleep(d)

    result = tk.Toplevel()
    result.geometry("200x100+{}+{}".format(int(GW / 2), int(GH / 2)))
    result.title("Result")

    MessageLabel = tk.Label(result, text = ResultMessage, font = ("", 20))
    MessageLabel.pack()

    def finish(event):
        result.destroy()
        GraphWindow.destroy()

    FinishButton = tk.Button(result, text = "FINISH")
    FinishButton.pack(pady = 10)
    FinishButton.bind("<Button-1>", finish)
    result.mainloop()


# Main Function #
## User can choose the sort function type in this function through the UI
## such as a button or an entry box
def main():
    root = tk.Tk()
    root.geometry("500x250")
    root.title("Configuration")
    root.resizable(0, 0)

    Label1 = tk.Label(text = "Sort Selection")
    Label1.pack(pady = 10)

    var = tk.IntVar()
    var.set(0)

    BS = tk.Radiobutton(root, value = 0, variable = var, text = "Bubble Sort")
    BS.place(x = 10, y = 40)
    SS = tk.Radiobutton(root, value = 1, variable = var, text = "Selection Sort")
    SS.place(x = 160, y = 40)
    IS = tk.Radiobutton(root, value = 2, variable = var, text = "Insertion Sort")
    IS.place(x = 310, y = 40)
    HS = tk.Radiobutton(root, value = 3, variable = var, text = "Heap Sort")
    HS.place(x = 10, y = 70)
    MS = tk.Radiobutton(root, value = 4, variable = var, text = "Merge Sort")
    MS.place(x = 160, y = 70)
    QS = tk.Radiobutton(root, value = 5, variable = var, text = "Quick Sort")
    QS.place(x = 310, y = 70)

    Label2 = tk.Label(text = "Number of Elements to Sort")
    Label2.place(x = 100, y = 115)

    GetElemNum = tk.Entry(width = 5)
    GetElemNum.insert(tk.END, "100")
    GetElemNum.place(x = 300, y = 115)

    Label3 = tk.Label(text = "Delay")
    Label3.place(x = 190, y = 160)

    GetDelayTime = tk.Entry(width = 5)
    GetDelayTime.insert(tk.END, "0")
    GetDelayTime.place(x = 270, y = 160)

    def CallDrawGraph(event):
        delay["time"] = float(GetDelayTime.get())
        if 0 <= delay["time"]:
            DrawGraph(var.get(), int(GetElemNum.get()))
        else:
            warning("\"delay\" should be a decimal fraction greater than 0.")
            return

    OkButton = tk.Button(root, text = "OK", width = 4)
    OkButton.pack(pady = 10, side = "bottom")
    OkButton.bind("<Button-1>", CallDrawGraph)

    root.mainloop()
