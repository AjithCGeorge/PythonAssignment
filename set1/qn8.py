
# Q8


import random
# nums=[random.randrange(1,100) for i in range(10)]
print('enter the numbers one by one : ')
nums=[]
while True:
    x=input()
    if(x==''):
        break
    else:
        nums.append(int(x))
nums=sorted(nums)
flag=0
for i in nums:
    if i%2==1:
        print('smallest odd number in the given list {} is {}'.format(nums,i))
        flag=1
        break
if flag==0:
    print('there is no odd numbers in the given string {}'.format(nums))
