key=int(input("enter the searching key:"))

data=[10,20,30,40,50,60]

low=0
high=len(data)-1

while low <= high:
    mid = (low+ high)// 2

    if key==data[mid]:
        print(f"key found at index {mid}")
        break;
    elif key<data[mid]:
        high=mid-1

    else:
        low=mid+1


else:
    print("key not found in data")
     



