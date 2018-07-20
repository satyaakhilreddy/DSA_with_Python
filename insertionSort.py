def insertionSort(arr):

  l=len(arr)

  for i in range(0,l):
    j=i

    while j>0 and arr[j-1]>arr[j]:
      swap(arr,j-1,j)
      j=j-1
    
  return arr

def swap(arr,a,b):

  temp=arr[a]
  arr[a]=arr[b]
  arr[b]=temp

arr=[5,4,3,2,1]

print(insertionSort(arr))