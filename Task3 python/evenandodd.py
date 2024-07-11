"""

To create twi list for odd and even

"""

n = int(input("Enter length of list::"))
l=[]
for i in range(1,n+1):
    e=int(input("Enter Element:"))
    l.append(e)
print(l)
#even
odd = []
even = []
for j in l :
    if(j%2==0):
         even.append (j)
    else:
        odd.append (j)     
print("even list:",even) 
print("odd list:",odd)          