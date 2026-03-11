n=int(input("enter how many datas to be entered :- "))
l=[int(input("Enter number :- ")) for i in range(n)]
l.sort()
if (n%2==0):
    median = (l[n//2]+l[n//2-1])/2
else:
    median = l[n//2]    
print("Medain is ", median)