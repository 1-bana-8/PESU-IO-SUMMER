n=int(input('Enter a number'))
s=0

while n!=0:
    r=(n%10)
    s+=r
    n//=10

print('Sum=',s)

