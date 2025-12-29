import heapq

list1 = [1,2,3,45]
heapq.heapify_max(list1)
largest = heapq.heappop_max(list1)
print(largest)
