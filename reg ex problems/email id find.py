# 1. Find the correct gmail
# 2. Write the pattern for find the Gmail id format 
import re
str = input("Enter the Gmail : ")
match = re.search(r'\w+@\w+', str)
if match:
    print("Your Gmail is Correct ",match.group()) 
else:
    print("Not Match")
