import re

file=open('cavity100.txt')
filenew=file.read()
filenew=str(filenew)
filet=filenew.replace('(','').replace(')','')
print(filet)
