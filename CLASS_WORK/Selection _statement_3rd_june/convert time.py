second =(int (input("Enter the number of seconds: ")) )                  
if second >= 3600:
    hours = second // 3600
    minutes = (second % 3600) // 60
    seconds = second % 60
    print(f"{hours} hours, {minutes} minutes, {seconds} seconds")
elif second >= 60:  

    minutes = second // 60
    seconds = second % 60
    print(f"{minutes} minutes, {seconds} seconds")
else:
    print(f"{second} seconds")