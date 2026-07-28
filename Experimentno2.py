n=int(input("Enter a no of customer:"))
my_list=[]

for i in range(n):
    id=int(input("enter acc no"))
    my_list.append(i)
    
print(my_list)
a=my_list
n=int(input("which no to you search"))

for i in range(len(a)):
    if n1 ==a[i]:
        print("found the no (a[i]on the index[i])")
    else:
        i=i+1