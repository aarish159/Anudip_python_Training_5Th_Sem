# Problem: Sensor Telemetry Analyzer

def analyze_sensors():
    try:
        # Step 1: Read sensor readings
        with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_challenge-3\telemetry.txt", "r") as f:
            readings = list(map(int, f.read().split()))

        # Step 2: Identify abnormal readings
        abnormal = []
        normal_count, abnormal_count = 0, 0
        for r in readings:
            if r < 90 or r > 110:
                abnormal.append(r)
                abnormal_count += 1
            else:
                normal_count += 1

        # Step 3: Calculate average
        avg = sum(readings) / len(readings)

        # Step 4: Save abnormal readings to alerts.txt
        with open("alerts.txt", "w") as f:
            f.write(" ".join(map(str, abnormal)))

        # ---- Output ----
        print("Abnormal Sensor Readings:", " ".join(map(str, abnormal)))
        print(f"Average Sensor Value: {avg:.1f}")
        print("Normal Readings:", normal_count)
        print("Abnormal Readings:", abnormal_count)
        print("Alert File Generated Successfully.")

    except FileNotFoundError:
        print("Error: telemetry.txt not found.")
    except Exception as e:
        print("Error occurred:", e)


# ---- Driver Code ----
analyze_sensors()
