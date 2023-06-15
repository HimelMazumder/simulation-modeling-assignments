import random
import math
import matplotlib.pyplot as plt

r = 1
hits = 0
random.seed(3)

hx = []
hy = []

mx = []
my = []

ra = 2 * 4
ca = 0


def set_values(n):
    for i in range(0, n):
        x = round(random.uniform(0, 4), 4)
        y = round(random.uniform(0, 2), 4)

        global hits
        if 1 <= x <= 3 and y >= 1:
            if y <= math.sqrt(1 - math.pow(x - 2, 2)) + 1:
                hits += 1
                hx.append(x)
                hy.append(y)
            else:
                mx.append(x)
                my.append(y)
        elif 0 <= x <= 1 and y <= 1:
            if y <= x:
                hits += 1
                hx.append(x)
                hy.append(y)
            else:
                mx.append(x)
                my.append(y)
        elif 1 <= x <= 3 and y <= 1:
            hits += 1
            hx.append(x)
            hy.append(y)
        elif 3 <= x <= 4 and y <= 1:
            if y <= 4 - x:
                hits += 1
                hx.append(x)
                hy.append(y)
            else:
                mx.append(x)
                my.append(y)
        else:
            mx.append(x)
            my.append(y)


def do_plot():
    plt.figure(figsize=(6, 4))

    plt.plot([0, 4, 4, 0, 0], [0, 0, 2, 2, 0], c="black")

    interval = r / 1000
    cx = []
    cy = []

    for i in range(0, 3000):
        x = i * interval + 1
        # print(x)
        cx.append(x)
        y = math.sqrt(1 - math.pow(x - 2, 2)) + 1
        cy.append(y)
        if x >= 3:
            break

    plt.plot(cx, cy, c="blue")
    plt.plot([0, 1], [0, 1], c="blue")
    plt.plot([0, 1], [0, 0], c="blue")
    plt.plot([3, 4], [0, 0], c="blue")
    plt.plot([4, 3], [0, 1], c="blue")

    plt.scatter(hx, hy, c="blue")
    plt.scatter(mx, my, c="red")

    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")

    plt.show()


def show_result(n):
    print("total hits: " + str(hits))

    global ra
    global ca

    ca = (hits / n) * ra
    print("shaded region area: " + str(ca))
    print()


area = []
nv = [100, 1000, 10000]

for i in range(0, 3):
    set_values(nv[i])
    do_plot()
    show_result(nv[i])
    area.append(ca)

plt.figure(figsize=(15, 6))
plt.bar(nv, area, align='center', width=100)
plt.xlabel("trials")
plt.ylabel("area")
plt.show()
