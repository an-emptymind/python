import random

counts={}
c=0

while c<100:
    roll = random.randint(1, 6)
    counts[roll] = counts.get(roll, 0) + 1
    c+=1
print(f"Counts is {counts}")
for face in range(1, 7):
    count = counts.get(face, 0)
    print(f"{face} : {'*' * count} ({count})")

