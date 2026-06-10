# Program to copy content from one file to another

# Open source file in read mode
with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\File_handling_10th_june\source.txt", "r") as src:
    # Read all content
    data = src.read()

# Open destination file in write mode
with open("destination.txt", "w") as dest:
    # Write content into destination file
    dest.write(data)

print("File copied successfully!")
