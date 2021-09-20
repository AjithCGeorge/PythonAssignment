# Qn3
import re

txt=input("Enter the string from mobile number to be extracted : ")
remno='[1-9]{1}[0-9]{9}'
result=re.findall(remno,txt)
print('Possible mobile numbers from the entered strings are: ',)
for i in result:
    print(i)
