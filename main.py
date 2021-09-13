# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt

global n
global a
global c
global g
global t
global x
a = c = g = t = n = 0
gcPer = 0
numSize = 50818468
with open("chr22.fa") as f:
    l = list(f.read().upper().strip())
    print(l)
    while numSize >= 100:
        for element in range(0, len(l), 100):
            for character in element:
                if character == 'N':
                    n += 1
                    break
                elif character == 'G':
                    g += 1
                elif character == 'C':
                    c += 1
            if n >= 1:
                break
            break

        #plt.plot(x, gcPer)
        if n == 0:
            gcPer = (g + c) / float(100)
            f1 = open("tableRes.txt", "a")
            f1.write("x: " + str(x) + " GC% " + str(gcPer) + "\n")
        n = 0
        g = 0
        c = 0
        x += 1
        numSize -= 100


    #plt.show()
    print("A: ")
    print(a)
    print("C: ")
    print(c)
    print("G: ")
    print(g)
    print("T: ")
    print(t)
    print("N: ")
    print(n)
    f.close()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
