# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt


def show(mass, a, b, d=False):
    y = mass[1][a:b]
    x = mass[0][a:b]
    c = [y[0]] * len(y)
    if d:
        c = [d[1]] * len(y)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y, color="green")
    ax1.plot(x, c)
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("Loss", color="green")
    ax1.grid(True, color="green")
    ax1.tick_params(axis="y", which="major", labelcolor="green")
    ax1.set_title("Динамика Loss")
    plt.show()

    y = mass[2][a:b]
    x = mass[0][a:b]
    c = [y[0]] * len(y)
    if d:
        c = [d[0]] * len(y)
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y, color="green")
    ax1.plot(x, c)
    ax1.set_xlabel("Epoch")
    ax1.set_ylabel("accuracy", color="green")
    ax1.grid(True, color="green")
    ax1.tick_params(axis="y", which="major", labelcolor="green")
    ax1.set_title("Динамика accuracy")
    plt.show()
