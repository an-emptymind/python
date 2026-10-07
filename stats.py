def min_max_avg(nums):
    return min(nums),max(nums),sum(nums)/len(nums)


def split_even_odd(nums):
    evens = [n for n in nums if n%2==0]
    odds = [n for n in nums if n%2!=0]
    return evens,odds

low,high,avg =  min_max_avg([4, 8, 15, 16, 23, 42])
print(f"Min: {low}, Max: {high}, Avg: {avg:.1f}")

even,odd=split_even_odd([4, 8, 15, 16, 23, 42])
print("Even:",even)
print("Odd:",odd)

results = [("Raj", 85), ("Anita", 92), ("Karthik", 78), ("Meera", 95)]
highest=0
topper=""
for name,score in results:
    print(f"Name {name} scored {score} marks")
    if score>highest:
        highest=score
        topper=name

print(f"{topper} is the Topper with {highest} marks")