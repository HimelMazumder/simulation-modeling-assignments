import numpy as np
import matplotlib.pyplot as plt

np.random.seed(10)

# m = 11
# n = 5
# Take m,n as input

m = int(input("m: "))
n = int(input("n: "))

# print(m)
# print(n)

beginning_inventory = 3
demand = 0
ending_inventory = 0
shortage_quantity = 0
order_quantity = 8
days_until_next_arrival = 2
shortage_days = 0

ending_units = []

print(f"Initial Beginning Inventory: {beginning_inventory}")
print(f"Initial Order Quantity: {order_quantity}")
print(f"Initial Lead: {days_until_next_arrival}")

for cycle in range(1, 11):
    print(f"Cycle No: {cycle}  ---------------------------------------------------------------------------------------")
    for day in range(1, n + 1):
        print("Day: ", day)

        # Calculate beginning inventory (beginning inventory + quantity arrived)
        # Write code here

        if days_until_next_arrival == 0:
            beginning_inventory += order_quantity

        # Today's demand
        daily_demand = np.random.choice([0, 1, 2, 3, 4], p=[0.10, 0.25, 0.35, 0.21, 0.09])
        total_demand = daily_demand + shortage_quantity

        if total_demand <= beginning_inventory:
            ending_inventory = beginning_inventory - total_demand
            shortage_quantity = 0
        else:
            extra_demand = total_demand - beginning_inventory
            shortage_quantity = extra_demand
            ending_inventory = 0
            # Count shortage days
            shortage_days += 1

        ending_units.append(ending_inventory)

        # print Beginning inventory, Daily demand, Ending inventory, Shortage quantity
        print(f"Beginning Inventory: {beginning_inventory}, Daily Demand: {daily_demand}, "
              f"Ending Inventory: {ending_inventory}, Shortage Quantity: {shortage_quantity}")

        if day == n:
            # Review day
            # Place order
            # Find order quantity
            # Generate random Lead time
            # days_until_next_arrival, order_quantity set

            order_quantity = m - ending_inventory
            days_until_next_arrival = np.random.choice([1, 2, 3], p=[0.6, 0.3, 0.1])

            print(f"Order Quantity: {order_quantity}")

        beginning_inventory = ending_inventory
        if day != n:
            days_until_next_arrival -= 1

        if days_until_next_arrival >= 0:
            print(f"Days until next arrival: {days_until_next_arrival}")

    print("")
    print("")

# Avg ending inventory
# Shortage day
# Ending inventory plot

print(f"Average ending inventory: {sum(ending_units) / (n * 10)}")
print(f"Shortage days: {shortage_days}")

tick_label = range(1, (10 * n) + 1)
plt.bar(tick_label, ending_units, width=0.5, color='blue')
plt.xlabel('Day number')
plt.ylabel('Ending inventory of each day')
plt.title('Inventory_level vs day graph')
plt.show()
