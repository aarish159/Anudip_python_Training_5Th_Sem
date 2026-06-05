# Battery Charging Indicator without any module/function

battery = 0   # starting battery percentage
charging = True   # assume charging initially

while battery <= 100:
    print("Battery:", battery, "%")
    
    if charging:
        print("Status: Charging ⚡")
    else:
        print("Status: Discharging 🔋")
    
    print("-" * 30)
    
    # update battery percentage
    if charging:
        battery += 10
        if battery == 100:
            charging = False   # switch to discharging
    else:
        battery -= 10
        if battery == 0:
            charging = True    # switch to charging
