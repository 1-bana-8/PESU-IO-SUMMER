n=input('ENTER NUMBERS WITH SPACE BETWEEN THEM(sorted)=\n')
n=list(map(int,n.split()))

x=int(input('ENTER ELEMENT TO BE SEARCHED ='))

def bins(n,l,m,h):
    
    while l<=h:
        m=int((l+h)/2)
        if n[m]==x:
            return m
        elif n[m]<x:
            l=m+1
        else:
            h=m-1
    return -1

l,h,m=0,(len(n)-1),0
p=bins(n,l,m,h)

if p!=-1:
    print('Element found at position',p+1)
else:
    print('Element not found')

