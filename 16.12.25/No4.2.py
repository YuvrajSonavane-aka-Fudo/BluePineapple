def maxHeapify(arr , n , i):
    largest = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        maxHeapify(arr , n , largest)

def maxHeapBuild(arr):
    n = len(arr)
    for i in range(n//2-1 , -1 , -1):
        maxHeapify(arr , n ,i)


arr = [1,2,3,4,5]
maxHeapBuild(arr)
print(arr[0] , "is the largest element")

