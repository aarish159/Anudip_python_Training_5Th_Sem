# Problem: Login Logs Analyzer

def analyze_logins():
    try:
        with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\Python_Coding_challenge-3\login_logs.txt", "r") as f:
            lines = f.readlines()

        success_count = 0
        fail_count = 0
        failure_dict = {}
        success_users = set()

        # Process each line
        for line in lines:
            line = line.strip()
            if not line:
                continue
            username, status = line.split(",")

            if status == "Success":
                success_count += 1
                success_users.add(username)
            elif status == "Failed":
                fail_count += 1
                if username in failure_dict:
                    failure_dict[username] += 1
                else:
                    failure_dict[username] = 1

        # Identify users with >2 failures
        review_users = [user for user, count in failure_dict.items() if count > 2]

        # ---- Output ----
        print("Successful Login Attempts:", success_count)
        print("Failed Login Attempts:", fail_count)

        print("Failure Count per User:")
        for user, count in failure_dict.items():
            print(f"{user} : {count}")

        print("Users with Successful Logins:", success_users)

        if review_users:
            print("Accounts Requiring Review:", review_users)
        else:
            print("Accounts Requiring Review: None")

    except FileNotFoundError:
        print("Error: login_logs.txt not found.")
    except Exception as e:
        print("Error occurred:", e)


# ---- Driver Code ----
analyze_logins()
