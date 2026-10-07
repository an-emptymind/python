#Lesson 1 — Variables & print()
name = "Raj"
age = 25
favourite_lang = "Python"

print("My name is", name)
print("I am", age, "years old")
print("My favourite programming language is", favourite_lang)

#Lesson 2 — Strings & Numbers (doing things with values)
a = 17
b = 5
print(f"The sum of a & b is {a + b} this is called addition")
print(f"The difference of a & b is {a - b} this is called subtraction")
print(f"The product of a & b is {a * b} this is called multiplication")
print(f"The division of a & b is {a / b} this is called division")
print(f"The modulus of a & b is {a % b} this is called modulus")

first_Name = "Raj"
last_Name = "Kumar"
full_Name = first_Name + " " + last_Name
print("My full name is", full_Name)
print(f"My full name is {first_Name} {last_Name} this is called concatenation")
#print (f"My full name is {first_Name} + {last_Name} this is called concatenation") not like this?

year_str = "2026"
print(f"After 5 years it will be {int(year_str)+5} this is called string formatting")


#Lesson 3 — Making decisions: if / elif / else
number = 17
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")

score = 82
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")


age = 12
has_ticket = True

if age >= 18 and has_ticket:
    print("Welcome")
else:
    print("Entry Denied")


#Lesson-4: Loops

#1.
for i in range(1,11):
    print(i)


#2.
for i in range(2,11,2):
    print(i)

#3
count=5
while count>0:
    print(count)
    count-=1
print("LiftOff!")

#4
for letter in "python":
    print(letter)


#Lesson 5 — Lists
#1,2,3
scores = [85, 92, 78, 90, 65]
print(f"There are {len(scores)} items in scores List")
print(f"The first item of the scores list is {scores[0]}")
print(f"The last item of scores list is {scores[-1]}")

#4
scores.append(88)
print(f"The new scores list is {scores}")

#5
for score in scores:
    print(f"Score: {score}")

#6
for score in scores:
    if score >=70:
        print(f"{score} is Pass")
    else:
        print(f"{score} is Fail")


#Lesson 6 — Functions

#1
def square(num):
    return num * num

print(f"square of 4 is: {square(4)}")
print(f"square of 13 is: {square(13)}")

#2
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

a=24
print(f"a is an even number: {is_even(a)}")

#3
languages=["french","spanish","kannada"]
def greet(name,language):
    if language not in languages:
        return "Invalid language"
    
    if language==languages[0]:
        return "Bonjour"
    elif language == languages[1]:
        return "Hola"
    elif language == languages[2]:
        return "Namaskara"

result = greet("raj",languages[0])
print(f"{result} raj!")

result2 = greet("ram","Tamil")
print(f"{result2} ram!")

#4
def average(nums):
    return sum(nums)/len(nums)

nums1=[2,4,6,8]
print(f"average of nums is {average(nums1)}")


#Lesson 7 — Dictionaries

#1
book = {"title":"If","author":"Rudyard kipling","year":1997}

print(f"{book['author']} is the author of {book['title']}")

#2
book["genre"]="philosophy"
book["year"]=2000
print(book)
print(book.keys())
print(book.values())
print(book.items())

#3
print(book.get("price","Unavailable"))

#4
for key,value in book.items():
    print(f"{key}:{value}")

#5
students = [{"name":"Prakash","grade":40},{"name":"Vipul","grade":60},{"name":"Karthik","grade":30}]
for p in students:
    print(f"{p['name']} got grade of {p['grade']}")  

grades=[]
for r in students:
    grades.append(r['grade'])

avg = average(grades)
print("Average of students is",avg)


#Lesson 8 — Handling errors with try / except

#1
marks=[]
try:
    print(average(marks))
except ZeroDivisionError:
    print("Can't divide by zero!")


#2
list=[23,534,56,3]
try:
    print(f"last element is {list[6]}")
except IndexError:
    print("No element exists at specified index")

#3
try:
    value=int(input("Enter a number:"))
    print(value*8)
except ValueError:
    print("Not a valid number")

#4
def safe_divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "Undefind"

print(safe_divide(4,0))
print(safe_divide(10,5))





        



