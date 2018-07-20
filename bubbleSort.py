def bubbleSort(arr):
  l=len(arr)

  for i in range(0,l):
    for j in range(0,l-i-1):
      if arr[j]>arr[j+1]:
        swap(arr,j,j+1)

  return print(arr)

def swap(arr,a,b):
  temp=arr[a]
  arr[a]=arr[b]
  arr[b]=temp

arr=[1,2,9,8,7,4]
bubbleSort(arr)