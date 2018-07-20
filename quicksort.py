def quicksort(arr,low,high):

  if low>=high:
    return

  pivot=partition(arr,low,high)
  quicksort(arr,low,pivot-1)
  quicksort(arr,pivot+1,high)

  return arr

def partition(arr,low,high):
  ind=(low+high)//2

  swap(arr,ind,high)

  j=low

  for i in range(low,high):
    if arr[i]<=arr[high]:
      swap(arr,i,j)
      j=j+1
  
  swap(arr,j,high)

  return j

def swap(arr,i,j):
  temp=arr[i]
  arr[i]=arr[j]
  arr[j]=temp

arr=[5,4,3,2,1]
print(quicksort(arr,0,4))