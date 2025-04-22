import sys, heapq
heap = []
for i in range(int(input())):
	num = int(sys.stdin.readline()) * -1
	if num == 0:
		print(heapq.heappop(heap) * -1 if heap else 0)
	else:
		heapq.heappush(heap, num)