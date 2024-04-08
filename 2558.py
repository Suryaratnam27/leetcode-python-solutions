gifts=[25,64,9,4,100]
import heapq
def piggifts(gifts,k):
    heap=[]
    for i in gifts:
        heap.append(-i)
    heapq.heapify(heap)
    while k>0:
        s1=heapq.heappop(heap)
        s1=(-s1)**0.5
        heapq.heappush(heap,int(-s1))
        k-=1 
    return -sum(heap)
a=piggifts(gifts,4)
print(a)
