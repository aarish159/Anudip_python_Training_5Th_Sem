# Delivery times list
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# 1. Fastest delivery
def fastest_delivery(times):
    return min(times)

# 2. Delayed orders (> 45 minutes)
def delayed_orders(times):
    delayed = []
    for t in times:
        if t > 45:
            delayed.append(t)
    return delayed

# 3. Average delivery time
def average_delivery_time(times):
    total = sum(times)
    return total / len(times)

# 4. Delivery category
def delivery_category(times):
    for t in times:
        if t <= 30:
            category = "Fast"
        elif 31 <= t <= 45:
            category = "Normal"
        else:
            category = "Delayed"
        print(f"{t} -> {category}")


# ---- Main Execution ----
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")
print("Delayed Orders:", delayed_orders(delivery_time))
print("Average Delivery Time:", round(average_delivery_time(delivery_time), 1), "minutes")
print("Categories:")
delivery_category(delivery_time)
