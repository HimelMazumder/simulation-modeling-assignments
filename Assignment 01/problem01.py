x = input("n: ")
n = int(x)

i = 0
while not 0 <= n <= 9:
    print("Enter a value between 0 and 9")
    n = int(input("n: "))

print("the value of n: " + str(n))

for i in range(n):
    m = 1
    k = n - (i + 2)
    for j in range(n):
        if j <= k:
            print(" ", end=" "),
        else:
            print(str(m), end=" ")
            m += 1
    print("")