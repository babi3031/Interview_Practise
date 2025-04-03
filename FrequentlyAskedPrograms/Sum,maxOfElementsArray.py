# Maximum of the element array
# max()
arr = [10,20,30,40,50]
print(sum(arr))
print(max(arr))

arr = [10,20,30,40,50]
# sort array without buit-in function
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]>= arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
print(arr[0])
# sorting using built-in method sort(),sorted()
# sort()
arr = [10,20,30,40,50]
arr.sort()
print(arr)
# sorted()
result=sorted(arr)
print(result)


# length of array
arr = [10,20,30,40,50]
count=0
for i in arr:
    count+=1
print(f"length of {arr} is {count}")
print(f"length of {arr} is {len(arr)}")


# swap first and last element in a list
# Approach 1 using temp variable
arr = [10,20,30,40,50]
temp=arr[0]
arr[0]=arr[len(arr)-1]
arr[len(arr)-1]=temp
print(arr)
# Appraoch 2
arr[0],arr[-1]=arr[-1],arr[0]
print(arr)
# Approach 3 using tuple
get=(arr[-1],arr[0])
arr[0],arr[-1]=get
print(arr)
# Approach 4 using *operand
start,*middle,end=arr
arr=[end,*middle,start]
print(arr)
# Appraoch 5 using pop
first=arr.pop(0)
end=arr.pop(-1)
arr.insert(0,end)
arr.append(first)
print(arr)