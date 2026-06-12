# Problem: Passenger Baggage Analyzer

baggage = (
    ("P101", 18), ("P102", 32), ("P103", 24), ("P104", 36),
    ("P105", 28), ("P106", 20), ("P107", 41), ("P108", 26),
    ("P109", 19), ("P110", 34)
)

def passengers_above_limit(baggage):
    result = []
    for pid, weight in baggage:
        if weight > 30:
            result.append(pid)
    return result

def count_within_exceed(baggage):
    within, exceed = 0, 0
    for _, weight in baggage:
        if weight > 30:
            exceed += 1
        else:
            within += 1
    return within, exceed

def excess_charges(baggage):
    charges = {}
    for pid, weight in baggage:
        if weight > 30:
            charges[pid] = (weight - 30) * 500
    return charges

def manual_inspection(baggage):
    inspection = []
    for pid, weight in baggage:
        if weight > 30:
            inspection.append(pid)
    return inspection

def heaviest_baggage(baggage):
    max_pid, max_weight = baggage[0]
    for pid, weight in baggage:
        if weight > max_weight:
            max_pid, max_weight = pid, weight
    return max_pid, max_weight

# ---- Driver Code ----
try:
    above_limit = passengers_above_limit(baggage)
    within, exceed = count_within_exceed(baggage)
    charges = excess_charges(baggage)
    inspection_list = manual_inspection(baggage)
    heavy_pid, heavy_weight = heaviest_baggage(baggage)

    print("Passengers Exceeding 30 kg Limit:", " ".join(above_limit))
    print("Passengers Within Limit:", within)
    print("Passengers Exceeding Limit:", exceed)

    print("Excess Baggage Charges:")
    for pid, charge in charges.items():
        print(f"{pid} : ₹{charge}")

    print("Passengers Requiring Manual Inspection:", inspection_list)
    print(f"Heaviest Baggage: {heavy_pid} ({heavy_weight} kg)")

except Exception as e:
    print("Error occurred:", e)
