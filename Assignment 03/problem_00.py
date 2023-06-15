import random
import math
import matplotlib.pyplot as plt

x = []
y = []

a = 0
b = 1

y_avg = 0

n = [10, 1000, 5000, 10000]
errors = []


def init_cords(nv):
    random.seed(427)
    global x
    global y

    global a
    global b

    for i in range(0, nv):

        x_val = random.uniform(a, b)
        y_val = (x_val ** 2) * math.exp(-x_val) * math.log(x_val + 2)

        x.append(x_val)
        y.append(y_val)


def get_integral(nv):
    global x
    global y
    global a
    global b
    global y_avg

    y_sum = sum(y)
    # print("y_sum: ")
    # print(y_sum)
    y_avg = y_sum / nv
    # print("n: ")
    # print(nv)
    # print("y_avg: ")
    # print(y_avg)
    integral = (b - a) * y_avg
    # print("integral: ")
    # print("(b - a): ")
    # print(b - a)
    # print("(b - a) * y_avg: ")
    # print(integral)

    return integral


def get_error(nv):
    global y_avg
    global a
    global b

    y_sqr = 0

    for i in range(0, nv):
        y_sqr += (y[i] ** 2)

    # print("y_sqr: ")
    # print(y_sqr)

    y_sqr_avg = y_sqr / nv
    # print("n: ")
    # print(nv)
    # print("y_sqr_avg (y_sqr / n): ")
    # print(y_sqr_avg)

    variance = y_sqr_avg - (y_avg ** 2)
    # print("variance (y_sqr_avg - y_ave ^ 2): ")
    # print(variance)
    error = ((b - a) / math.sqrt(nv)) * (math.sqrt(variance))

    return error


def draw_bar():
    global n
    global errors

    plt.bar(n, errors, width=500, color="green")
    # show x cords only those with y value
    plt.xticks(n, [10, 1000, 5000, 10000])

    plt.xlabel("Value of n")
    plt.ylabel("Error estimate")
    plt.show()


for i in range(0, 4):
    print(f"n: {n[i]}")
    init_cords(n[i])
    # print("x: ")
    # print(x)
    # print("y: ")
    # print(y)
    print(f"Integral: {get_integral(n[i])}")
    err = get_error(n[i])
    errors.append(err)
    print(f"Error: {err}")

    x.clear()
    y.clear()
    print()

draw_bar()
