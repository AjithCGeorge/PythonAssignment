# Qn1

# a = []
# a = ['Alice']
# a = ['Alice', 'Bob',]
# a = ['Alice', 'Bob', 'Charls']
# a = ['Alice', 'Bob', 'Charls','Denny']
# a = ['Alice', 'Bob', 'Charls','Denny','Emely']
a=[]
print('enter the name of the people who liked one by one :',end=' ')
while True:
    x=input()
    if(x==''):
        break
    else:
        a.append(x)

response={}

if len(a)==0:
    response[0]='Nobody likes This'
if len(a)==1:
    response[1]=a[0]+' likes This'
if len(a)==2:
    response[2]=a[0]+' and '+a[1]+' likes This'
if len(a)==3:
    response[3]='{}, {} and {} likes This'.format(a[0],a[1],a[2])
if len(a) >3:
    response[len(a)]='{}, {} and {} others likes this'.format(a[0],a[1],len(a)-2)

print(response[len(a)])

