import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = list(map(int, input().split()))
def quick_sort(start, end, k):
    global a
    if start < end:
        pivot = partition(start, end)
        if pivot == k:
            return
        elif k < pivot:
            quick_sort(start, pivot - 1, k)
        else:
            quick_sort(pivot + 1, end, k)
def swap(i, j):
    global a
    a[i], a[j] = a[j], a[i]
def partition(start, end):
    global a
    if start + 1 == end:
        if a[start] > a[end]:
            swap(start, end)
        return end
    middle = (start + end) // 2
    swap(start, middle)
    pivot = a[start]
    left = start + 1
    right = end
    while left <= right:
        while pivot < a[right] and right > 0:
            right -= 1
        while pivot > a[left] and left < len(a) - 1:
            left += 1
        if left <= right:
            swap(left, right)
            left += 1
            right -= 1
    a[start] = a[right]
    a[right] = pivot
    return right
quick_sort(0, n - 1, k - 1)
print(a[k - 1])