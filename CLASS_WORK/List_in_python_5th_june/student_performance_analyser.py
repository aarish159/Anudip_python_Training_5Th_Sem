#creating the list
marks=[78,45,92,35,88,40,99,56]
#displaying all passed students marks>=40
passed_students=[]
for i in marks:
    if(i>=40):
        passed_students.append(i)
#counting number of failed students
failed_count=0
for i in marks:
    if i<40:
        failed_count=+1
#finding highest and lowest marks
highest=marks[0]
lowest=marks[0]
for i in marks[1:]:
    if i>highest:
        highest=i
    if i<lowest:
        lowest=i
# creating list of marks more than 75
merit_list=[]
for i in marks:
    if i>75:
        merit_list.append(i)
#output
print("passed students: ",passed_students)
print("Failed count: ",failed_count)
print("Highest marks: ",highest)
print("lowest marks: ",lowest)
print("Merit list: ",merit_list)