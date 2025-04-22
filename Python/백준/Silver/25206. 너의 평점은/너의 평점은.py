rating = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0}
sum, grade_sum = 0, 0
for i in range(20):
    subject, score, grade = input().split()
    score = int(score[0:1])
    if grade == "P":
        continue
    for k, v in rating.items():
        if grade == k:
            grade_sum += score
            score *= v
    sum += score
try:
    print(f"{sum / grade_sum:<0.6f}")
except:
    print(0)