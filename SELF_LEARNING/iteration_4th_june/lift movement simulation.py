# Lift Travel Tracker

current_floor = 0
total_travelled = 0

while True:
    print("Current Floor:", current_floor)
    dest = int(input("Enter Destination (-1 to stop): "))
    
    if dest == -1:
        break
    
    travelled = abs(dest - current_floor)   # difference in floors
    print("Travelled:", travelled, "floors")
    
    total_travelled += travelled
    current_floor = dest   # update current floor

print("Total Travelled:", total_travelled, "floors")
