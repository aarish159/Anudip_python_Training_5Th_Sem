# Food Delivery Performance Dashboard

delivery_times = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Fastest delivery
def fastest(times):
    fast = times[0]
    for t in times:
        if t < fast:
            fast = t
    return fast

# 2. Slowest delivery
def slowest(times):
    slow = times[0]
    for t in times:
        if t > slow:
            slow = t
    return slow

# 3. Average delivery time
def average(times):
    total = 0
    for t in times:
        total += t
    return total / len(times)

# 4. Delayed orders (>45 minutes)
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    return delayed

# 5. Categorize deliveries
def categorize(times):
    fast_count = 0
    normal_count = 0
    delayed_count = 0
    for t in times:
        if t <= 30:
            fast_count += 1
        elif t <= 45:
            normal_count += 1
        else:
            delayed_count += 1
    return fast_count, normal_count, delayed_count


# function call
print("Fastest Delivery:", fastest(delivery_times), "minutes")
print("Slowest Delivery:", slowest(delivery_times), "minutes")
print("Average Delivery Time:", round(average(delivery_times), 1), "minutes")
print("Delayed Orders:", delayed_orders(delivery_times))

fast, normal, delayed = categorize(delivery_times)
print("Fast Deliveries:", fast)
print("Normal Deliveries:", normal)
print("Delayed Deliveries:", delayed)
