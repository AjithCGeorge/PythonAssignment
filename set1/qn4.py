# Qn 4

seq=input('enter the string of words to be sorted :')
# seq="without,hello,bag,world"
lisT=seq.split(',')
lisT=sorted(lisT)
seq=''
for i in lisT:
    seq+=str(i)+','

seq=seq[:-1]
print(seq)
