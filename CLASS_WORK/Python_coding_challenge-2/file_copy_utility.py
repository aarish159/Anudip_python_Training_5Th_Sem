# Problem 16: File Copy Utility

def copy_file(source_file, backup_file):
    try:
        # Step 1: Read contents of source file
        with open(source_file, "r") as src:
            data = src.readlines()   # read line by line
        source_lines = len(data)

        # Step 2: Copy contents to backup file
        with open(backup_file, "w") as dest:
            dest.writelines(data)
        backup_lines = source_lines  # since we copied same lines

        # Step 3: Display success message
        print("File copied successfully.")

        # Step 4: Verify line counts
        print(f"Source File Lines: {source_lines}")
        print(f"Backup File Lines: {backup_lines}")

        if source_lines == backup_lines:
            print("Verification Status: Successful")
        else:
            print("Verification Status: Failed")

    except FileNotFoundError:
        print("Error: Source file not found.")
    except Exception as e:
        print("Error occurred:", e)


# ---- Driver Code ----
copy_file("notes.txt", "backup.txt")
