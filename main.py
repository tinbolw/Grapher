import numpy as np
from matplotlib import pyplot as plt


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def gety():
    y = [0, ]
    indexvar = 1
    pushy = input("What is the first Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the second Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the third Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the fourth Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the fifth Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the sixth Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the seventh Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the eighth Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the ninth Y value?\n")
    y.append(pushy)
    indexvar += 1
    pushy = input("What is the tenth Y value?\n")
    y.append(pushy)
    plt.plot(x, y)
    plt.show()

gety()
