# Problem 17: Daily Sales Performance Analyzer (Simple Loops + Functions)

sales = [15000, 22000, 18000, 25000, 30000, 17000, 28000, 26000, 21000, 19000]

def find_highest(sales):
    highest = sales[0]
    for s in sales:
        if s > highest:
            highest = s
    return highest

def find_lowest(sales):
    lowest = sales[0]
    for s in sales:
        if s < lowest:
            lowest = s
    return lowest

def calculate_average(sales):
    total = 0
    for s in sales:
        total += s
    return total / len(sales)

def count_above_20k(sales):
    count = 0
    for s in sales:
        if s > 20000:
            count += 1
    return count

def sales_below_average(sales, avg):
    below = []
    for s in sales:
        if s < avg:
            below.append(s)
    return below

# ---- Driver Code ----
try:
    highest = find_highest(sales)
    lowest = find_lowest(sales)
    avg_sales = calculate_average(sales)
    above_20k = count_above_20k(sales)
    below_avg = sales_below_average(sales, avg_sales)

    print(f"Highest Sales: ₹{highest}")
    print(f"Lowest Sales: ₹{lowest}")
    print(f"Average Sales: ₹{avg_sales:.0f}")
    print(f"Days with Sales Above ₹20,000: {above_20k}")
    print(f"Sales Below Average: {below_avg}")

except Exception as e:
    print("Error occurred:", e)
