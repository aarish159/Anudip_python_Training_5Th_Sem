# Problem: Coupon Usage Analyzer

def analyze_coupons():
    try:
        # Step 1: Read coupons from file
        with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_challenge-3\coupons.txt", "r") as f:
            coupons = f.read().split()

        # Step 2: Count frequency using dictionary
        freq = {}
        for c in coupons:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1

        # Step 3: Identify suspicious coupons (>3 times)
        suspicious = [c for c, count in freq.items() if count > 3]

        # Step 4: Create set of unique coupons
        unique_coupons = set(freq.keys())

        # Step 5: Find most frequently used coupon
        max_coupon, max_count = None, 0
        for c, count in freq.items():
            if count > max_count:
                max_coupon, max_count = c, count

        # Step 6: Save suspicious coupons into fraud_report.txt
        with open("fraud_report.txt", "w") as f:
            if suspicious:
                f.write("Suspicious Coupons:\n")
                for c in suspicious:
                    f.write(c + "\n")
            else:
                f.write("No suspicious coupons found.\n")

        # ---- Output ----
        print("Coupon Usage Frequency:")
        for c, count in freq.items():
            print(f"{c} : {count}")

        if suspicious:
            print("Suspicious Coupons:", ", ".join(suspicious))
        else:
            print("Suspicious Coupons: None")

        print("Unique Coupons:", unique_coupons)
        print(f"Most Frequently Used Coupon: {max_coupon}")
        print("Fraud Report Generated Successfully.")

    except FileNotFoundError:
        print("Error: coupons.txt not found.")
    except Exception as e:
        print("Error occurred:", e)


# ---- Driver Code ----
analyze_coupons()

