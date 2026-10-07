class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

    def birthday(self):
        self.age +=1
        print(f"{self.name} turned {self.age} today, Happy Birthday!")

    def describe(self):
        print(f"{self.name} is {self.age} years old")


dog1 = Dog("puppy",2)
dog1.describe()
dog1.bark()
dog1.birthday()
dog1.describe()

dog2 = Dog("charlie",5)
dog2.describe()
dog2.bark()
dog2.birthday()
dog1.describe()


class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        print(f"Area= {self.width * self.height}")

    def perimeter(self):
        print(f"Perimeter = {2 * (self.width + self.height)}")

    def is_square(self):
        return self.width == self.height
          


rec1 = Rectangle(4,6)
rec2 = Rectangle(3,3)
rec1.area()
rec1.perimeter()
result = rec1.is_square()
result2 = rec2.is_square()
print(f"rec1 is a square: {result}")
print(f"rec2 is a square: {result2}")


class Student:
    def __init__(self,name):
        self.name = name
        self.grades= []

    def add_grade(self,grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

student1 = Student("Rohan")
student1.add_grade(10)
student1.add_grade(35)
student1.average()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

   

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n1.next = n2
n2.next = n3

print(n1.value)
print(n1.next.value)
print(n1.next.next.value)


def print_list(head):
    current = head
    while current is not None:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
    
def build_list(values):
    head = None
    tail = None
    for v in values:
        node = Node(v)
        if head is None:
            head = node
            tail = node
        else:
            tail.next = node
            tail = node
    return head

def sum_list(head):
    current = head
    s = 0
    while current is not None:
        s+=current.value
        current = current.next
    return s


def count_list(head):
    current = head
    c=0
    while current is not None:
        c+=1
        current = current.next
    return c

print_list(n1)
values = [1,2,3,4,5]
h = build_list(values)
print_list(h)
print(sum_list(h))
print(count_list(h))