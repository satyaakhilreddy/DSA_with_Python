def mergesort(arr,low,high):

  if low<=high:
    return
  
  middle=(low+high)//2

  mergesort(arr,low,middle)
  mergesort(arr,middle+1,high)
  merge(arr,low,middle,high)

  return arr

def merge(arr,low,middle,high):

  temp=[]
  for i in range(low,high+1):
    temp[i]=arr[i]
  
  a=low
  b=middle+1
  c=low

  while a<=middle and b<=high:
    if temp[a]<=temp[b]:
      arr[c]=temp[a]
      a=a+1
    else:
      arr[c]=temp[b]
      b=b+1
    c=c+1
  
  while a<=middle:
    arr[c]=temp[a]
    a=a+1
    c=c+1
  while b<=high:
    arr[c]=temp[b]
    c=c+1
    b=b+1
  
arr=[5,4,3,2,1]
print(mergesort(arr,0,4))

