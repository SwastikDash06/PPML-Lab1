arr=[]
x=int(input("enter the number of elements: "))
for i in range(x):
    m=int(input("Enter the element:"))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range(len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]