s1, s2 = map(int, input().split())
s3, s4 = map(int, input().split())
s5, s6 = map(int, input().split())
s7, s8 = map(int, input().split())
sum1 = s2 -s3 + s4
sum2 = sum1 - s5 + s6
print(max(s2, sum1, sum2))