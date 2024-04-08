st=[2,4,7,1,8,1]
import heapq
heapq.heapify(st)
print(st)
def last_stone(st):
    heap=[]
    for n in st:
        heap.append(-n)
    heapq.heapify(heap)

    # Collision will happen only if there are two stones
    while len(heap) >1:
        s1=heapq.heappop(heap)
        s2=heapq.heappop(heap)
        s=s1-s2
        if s!=0:
            heapq.heappush(heap,s)
    if len(heap)==0:
        return 0
    else:
        return -heap[0]
a=last_stone(st)
print(a)
