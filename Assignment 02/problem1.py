import random
import math
import matplotlib.pyplot as plt

random.seed(3)

r = 3

hx = []
hy = []

mx = []
my = []

hits = 0
est_pi = 0

sa = 5 * 5
ca = 0


def set_values(n):
    for i in range(0, n):
        x = round(random.uniform(0, 5), 4)
        y = round(random.uniform(0, 5), 4)
        if x <= r and y <= r:
            if y <= math.sqrt(math.pow(r, 2) - math.pow(x, 2)):
                global hits
                hits += 1

                hx.append(x)
                hy.append(y)
            else:
                mx.append(x)
                my.append(y)
        else:
            mx.append(x)
            my.append(y)

    global est_pi
    est_pi = round((100 * hits) / (9 * n), 4)


def do_plot():
    plt.figure(figsize=(5.5, 5.5))

    plt.plot([0, 0, 5, 5, 0], [0, 5, 5, 0, 0], c="blue")

    interval = r / 1000
    ax = []
    ay = []

    for k in range(0, 1000):
        x = k * interval
        ax.append(x)
        y = math.sqrt(math.pow(r, 2) - math.pow(x, 2))
        ay.append(y)

    plt.plot(ax, ay, c="red")

    plt.scatter(hx, hy, c="red")
    plt.scatter(mx, my, c="blue")

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.show()


def show_result(n):
    print()
    print("total hits " + str(hits))
    print("estimated value of pi: " + str(est_pi))

    global sa
    global ca
    ca = round(4 * (hits / n) * sa, 4)
    print("Circle area: " + str(ca))


def do_bar_plot(x, y, yl):
    plt.figure(figsize=(15, 6))
    plt.bar(x, y, align='center', width=100)
    plt.xlabel("trials")
    plt.ylabel(yl)
    plt.show()


pi = []
area = []
nv = [100, 1000, 10000]

for i in range(0, 3):
    set_values(nv[i])
    do_plot()
    show_result(nv[i])
    pi.append(est_pi)
    area.append(ca)

do_bar_plot(nv, pi, "pi")
do_bar_plot(nv, area, "area")
