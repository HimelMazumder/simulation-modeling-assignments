import os

queue = list()


def push_front(data):
    queue.insert(0, data)


def push_back(data):
    queue.append(data)


def pop_front():
    queue.pop(0)


def pop_back():
    queue.pop()


def front():
    return queue[0]


def back():
    return queue[len(queue)-1]


def show_list():
    print(queue)


def execute_file_instruction(f):
    for line in f:
        if not line == '/n':
            w = line.split()
            op = w[0].capitalize()
            if op == 'A':
                print("Inserts " + w[1] + " at the front")
                push_front(w[1])
                show_list()
            elif op == 'B':
                print("Inserts " + w[1] + " at the end")
                push_back(w[1])
                show_list()
            elif op == 'C':
                if queue:
                    print("Popping from front")
                    pop_front()
                    show_list()
                else:
                    print("List is empty")
            elif op == 'D':
                if queue:
                    print("Popping from end")
                    pop_back()
                    show_list()
                else:
                    print("List is empty")
            elif op == 'E':
                if queue:
                    print("first data")
                    print(front())
                else:
                    print("List is empty")
            elif op == 'F':
                if queue:
                    print("last data")
                    print(back())
                else:
                    print("List is empty")
    print("Final state: ", end=" ")
    show_list()


if os.path.exists("input.txt"):
    f = open("input.txt", 'r')
    execute_file_instruction(f)
else:
    print("input.txt file doesn't exist!!")
