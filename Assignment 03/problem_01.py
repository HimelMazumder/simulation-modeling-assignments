import random
import math
import matplotlib.pyplot as plt

x = []
y = []

y_avg = 0

n = [10, 1000, 5000, 10000]
errors = []


def init_cords(nv, av, bv, fx):
    random.seed(427)
    global x
    global y

    for i in range(0, nv):

        x_val = random.uniform(av, bv)
        if fx == 0:
            y_val = 2 * math.sqrt(x_val)
        else:
            y_val = 8 - x_val

        x.append(x_val)
        y.append(y_val)


def get_integral(nv, av, bv):
    global x
    global y

    global y_avg

    y_sum = sum(y)
    # print("y_sum: ")
    # print(y_sum)
    y_avg = y_sum / nv
    # print("n: ")
    # print(nv)
    # print("y_avg: ")
    # print(y_avg)
    integral = (bv - av) * y_avg
    # print("integral: ")
    # print("(b - a): ")
    # print(b - a)
    # print("(b - a) * y_avg: ")
    # print(integral)

    return integral


def get_error(nv, av, bv):
    global y_avg

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
    error = ((bv - av) / math.sqrt(nv)) * (math.sqrt(variance))

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
    a = 0
    b = 4
    total_integral = 0
    total_error = 0
    for j in range(0, 2):
        init_cords(n[i], a, b, j)
        # print("x: ")
        # print(x)
        # print("y: ")
        # print(y)
        total_integral += get_integral(n[i], a, b)
        total_error += get_error(n[i], a, b)

        x.clear()
        y.clear()

        a += 4
        b += 4

    errors.append(total_error)
    print(f"n: {n[i]}")
    print(f"Integral: {total_integral}")
    print(f"Error: {total_error}")
    print()

draw_bar()
