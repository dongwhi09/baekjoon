import sys
input = sys.stdin.readline
n = int(input())

nums = []
for _ in range(n):
    x = int(input())
    nums.append(x)
nums.sort(reverse=True)

for i in range(len(nums)-2):
    if sum(nums[i+1:i+3]) > nums[i]:
        print(sum(nums[i:i+3]))
        break
else:
    print(-1)