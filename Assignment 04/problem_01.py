import numpy as np
import matplotlib.pyplot as plt

x_positions = [[], [], [], []]
y_positions = [[], [], [], []]

velocities = [3, 5, 7, 2]

t_end = 20
length = 0
shots = [0, 0, 0, 0]


def init_positions():
    x_positions[0].append(10)
    y_positions[0].append(0)

    x_positions[1].append(0)
    y_positions[1].append(10)

    x_positions[2].append(10)
    y_positions[2].append(10)

    x_positions[3].append(0)
    y_positions[3].append(0)

    global length
    length = 1


def set_coord(tar, pur, time):
    target = [x_positions[tar][time], y_positions[tar][time]]
    pursuer = [x_positions[pur][time], y_positions[pur][time]]

    distance = np.linalg.norm(np.array(target) - np.array(pursuer))
    if distance < 5:
        shots[tar] += 1

        c = 'A'

        tt = ord(c) + tar
        pt = ord(c) + pur

        tc = chr(tt)
        pc = chr(pt)

        print(f"{pc} shots {tc} at t = {time}s with a distance of {distance} m")

    del_x = target[0] - pursuer[0]
    del_y = target[1] - pursuer[1]

    sin_theta = del_y / distance
    cos_theta = del_x / distance

    new_x = round(pursuer[0] + (velocities[pur] * cos_theta), 8)
    new_y = round(pursuer[1] + (velocities[pur] * sin_theta), 8)

    x_positions[pur].append(new_x)
    y_positions[pur].append(new_y)


def set_positions():
    for i in range(0, t_end):
        set_coord(2, 0, i)
        set_coord(1, 2, i)
        set_coord(3, 1, i)
        set_coord(0, 3, i)

        global length
        length += 1
        # print(length)


def show_positions():
    car = 'A'

    for i in range(4):
        print("Positions of ", car)
        for j in range(length):
            print(f"[{x_positions[i][j]}, {y_positions[i][j]}] at t = {j}s", end=" -- ")

        temp = ord(car) + 1
        car = chr(temp)
        print("||")
        print()

    # print(length)


def show_graph():
    x_pos_arr = np.array(x_positions)
    y_pos_arr = np.array(y_positions)

    plt.plot(x_pos_arr[0], y_pos_arr[0], marker='o', color='green')
    plt.plot(x_pos_arr[1], y_pos_arr[1], marker='o', color='blue')
    plt.plot(x_pos_arr[2], y_pos_arr[2], marker='o', color='red')
    plt.plot(x_pos_arr[3], y_pos_arr[3], marker='o', color='black')

    plt.title("Serial chase problem")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")

    plt.legend(['A', 'B', 'C', 'D'], bbox_to_anchor=(1.015, 1.15), ncol=2)

    plt.grid(color = 'grey', linestyle = '--', linewidth = 0.5)
    plt.show()


init_positions()
# print(x_positions)
# print(y_positions)
set_positions()
print()
print(f"A is shot {shots[0]} times")
print(f"B is shot {shots[1]} times")
print(f"C is shot {shots[2]} times")
print(f"D is shot {shots[3]} times")
print()
show_positions()
show_graph()
