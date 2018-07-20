def selectionSort(arr):

   l=len(arr)

   for i in range(0,l-1):

    ind=i

    for j in range(i+1,l):
      if arr[j]<arr[ind]:
        ind=j
    
    if ind is not i:
      swap(arr,ind,i)
  
   return arr

def swap(arr,a,b):
  temp=arr[a]
  arr[a]=arr[b]
  arr[b]=temp

arr=[5,4,3,2,1]
print(selectionSort(arr))