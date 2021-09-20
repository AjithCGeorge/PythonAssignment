# Q9


lines=1
words=0
data=open("sample.txt","r")
x=data.read()
# print(x)
for i in x:
    if i=='\n':
        lines+=1
    if i=='\n' or i==' ':
        words+=1

print('There are {} characters, {} words and {} lines in this document '.format(len(x),words,lines))


