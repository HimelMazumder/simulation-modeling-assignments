import matplotlib.pyplot as plt

z_1 = []
z_2 = []
z_3 = []

u = []

u_1 = []
u_2 = []
u_3 = []


def clear_all():
    z_1.clear()
    z_2.clear()
    z_3.clear()

    u_1.clear()
    u_2.clear()
    u_3.clear()
    u.clear()


def initiate_g1(n):
    global u_1
    global z_1

    a_11 = 13
    c_1 = 3
    m_1 = 16

    z_1.append(12)
    z_1.append(7)

    for i in range(2, n + 2):
        z_1_i = ((a_11 * z_1[i - 1]) + z_1[i - 2] + c_1) % m_1
        z_1.append(z_1_i)

        u_1_i = z_1_i / m_1
        u_1.append(u_1_i)


def initiate_g2(n):
    global u_2
    global z_2

    a_21 = 12
    a_22 = 13
    m_2 = 17

    z_2.append(3)
    z_2.append(5)

    for j in range(2, n + 2):
        z_2_i = ((a_21 * (z_2[j - 1] ** 2)) + (a_22 * (z_2[j - 2]))) % m_2
        z_2.append(z_2_i)

        u_2_i = z_2_i / m_2
        u_2.append(u_2_i)


def initiate_g3(n):
    global u_3
    global z_3

    m_3 = 15

    z_3.append(2)
    z_3.append(7)

    for k in range(2, n + 2):
        z_3_i = ((z_3[k - 1] ** 3) + (z_3[k - 2])) % m_3
        z_3.append(z_3_i)

        u_3_i = z_3_i / m_3
        u_3.append(u_3_i)


def initiate_w_h_method(n):
    for m in range(0, n):
        total = u_1[m] + u_2[m] + u_3[m]
        u_i = total - int(total)
        u.append(u_i)


def show_random_numbers():
    print("U 1: ")
    print(u_1)

    print("")

    print("U 2: ")
    print(u_2)

    print("")

    print("U 3: ")
    print(u_3)

    print("")

    print("U ")
    print(u)

    print("")


def draw_hist():
    plt.hist(u, bins=20, rwidth=0.8)
    plt.gca().set(title='Frequency Histogram', ylabel='Frequency');
    plt.show()


n = [100, 1000, 5000]

for p in n:
    initiate_g1(p)
    initiate_g2(p)
    initiate_g3(p)
    initiate_w_h_method(p)
    show_random_numbers()
    draw_hist()
    clear_all()
