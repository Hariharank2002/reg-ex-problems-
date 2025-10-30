#1. Write a Python program that matches a word containing 'z', not the start or end of the word.
#python program 
# re is reg-ex
import re
text="""i visited the zoo yesterday"""
texture=r'\b\w*z\w*\b'
match=re.findall(texture,text)
print(match)
