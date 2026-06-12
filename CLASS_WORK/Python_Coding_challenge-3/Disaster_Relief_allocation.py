# Problem: Relief Material Analyzer

resources = {
    "Warehouse1": ["Food", "Medicine", "Blankets"],
    "Warehouse2": ["Water", "Food", "Tents"],
    "Warehouse3": ["Medicine", "Tents", "Clothes"],
    "Warehouse4": ["Food", "Water", "Medicine"]
}

def unique_resources(resources):
    all_items = set()
    for items in resources.values():
        for item in items:
            all_items.add(item)
    return all_items

def warehouses_with_medicine(resources):
    result = []
    for warehouse, items in resources.items():
        if "Medicine" in items:
            result.append(warehouse)
    return result

def resource_availability(resources):
    availability = {}
    for warehouse, items in resources.items():
        for item in items:
            if item in availability:
                availability[item] += 1
            else:
                availability[item] = 1
    return availability

def most_widely_available(availability):
    max_count = max(availability.values())
    result = [item for item, count in availability.items() if count == max_count]
    return result

def resources_in_all(resources):
    # Start with items of first warehouse
    common = set(list(resources.values())[0])
    for items in resources.values():
        common = common.intersection(set(items))
    return common

# ---- Driver Code ----
try:
    unique = unique_resources(resources)
    medicine_warehouses = warehouses_with_medicine(resources)
    availability = resource_availability(resources)
    widely_available = most_widely_available(availability)
    common_resources = resources_in_all(resources)

    print("Unique Resources:", unique)
    print("Warehouses with Medicines:", " ".join(medicine_warehouses))

    print("Resource Availability:")
    for item, count in availability.items():
        print(f"{item} : {count}")

    print("Most Widely Available Resources:", " ".join(widely_available))

    if common_resources:
        print("Resources Available in All Warehouses:", " ".join(common_resources))
    else:
        print("Resources Available in All Warehouses: None")

except Exception as e:
    print("Error occurred:", e)
