# Hospital Patient Management System

#  Display all patient records
def display_all():
    f = open("patients.txt", "r")
    for line in f:
        print(line.strip())
    f.close()

#  Display critical patients
def display_critical():
    f = open("patients.txt", "r")
    print("Critical Patients:", end=" ")
    for line in f:
        data = line.strip().split(",")
        if data[2] == "Critical":
            print(data[1], end=" ")
    print()
    f.close()

#  Count patients under each status
def count_status():
    normal = 0
    stable = 0
    critical = 0
    f = open("patients.txt", "r")
    for line in f:
        data = line.strip().split(",")
        status = data[2]
        if status == "Normal":
            normal += 1
        elif status == "Stable":
            stable += 1
        elif status == "Critical":
            critical += 1
    f.close()
    print("Patient Count: Normal :", normal, "Stable :", stable, "Critical :", critical)
    return normal, stable, critical

#  Search patient details using Patient ID
def search_patient(pid):
    f = open("patients.txt", "r")
    for line in f:
        data = line.strip().split(",")
        if data[0] == pid:
            print("Patient Found:", line.strip())
            f.close()
            return
    f.close()
    print("Patient Not Found")

#  Save critical patient records to critical_patients.txt
def save_critical():
    f = open("patients.txt", "r")
    out = open("critical_patients.txt", "w")
    for line in f:
        data = line.strip().split(",")
        if data[2] == "Critical":
            out.write(line)
    f.close()
    out.close()
    print("Critical Patient Report Generated Successfully.")


# function call
display_critical()
count_status()
search_patient("P104")
save_critical()