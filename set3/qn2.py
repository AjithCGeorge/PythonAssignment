# Qn2
import re

mail=input('Enter the Email id to be checked:')
remail="^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
result=re.fullmatch(remail,mail)
if result:
    print('valid email')
else:
    print('not a valid email')
