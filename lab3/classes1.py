import math

# 1. 
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Enter a string: ")

    def printString(self):
        print(self.string.upper())

# 2.
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

# 3. 
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# 4.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# 5.
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

# 6.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(1, 51))  # Числа от 1 до 50
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers:", prime_numbers)


# Тест


str_obj = StringManipulator()

str_obj.string = "hello"  
str_obj.printString()  

# 2.
sq = Square(4)
print("Square area:", sq.area())  # 16

# 3. 
rect = Rectangle(4, 6)
print("Rectangle area:", rect.area())  # 24

# 4. 
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()  # Point(1, 2)
print("Distance:", p1.dist(p2))  

# 5. 
acc = Account("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)  

# 6. 
print("Prime numbers:", prime_numbers)  
