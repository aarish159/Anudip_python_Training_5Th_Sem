#create e file to rread of data from a file and display the vowels,characters and lines into  the file

# File Handling 
vowels = "aeiouAEIOU"
vowel_count = 0
char_count = 0
line_count = 0

with open(r"C:\Users\aarish\OneDrive\Desktop\python Anudip Training\CLASS_WORK\File_handling_10th_june\sample.txt", "r") as f:
    for line in f:
        line_count += 1
        for ch in line:
            char_count += 1
            if ch in vowels:
                vowel_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Characters:", char_count)
print("Number of Lines:", line_count)
