# 1. 
def square_generator(N):
    for i in range(N + 1):
        yield i ** 2


print("Квадраты чисел до 10:", list(square_generator(10)))

# 2. 
def even_numbers(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input("Введите число n: "))
print("Четные числа:", ", ".join(map(str, even_numbers(n))))

# 3. 
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

print("Числа, делящиеся на 3 и 4:", list(divisible_by_3_and_4(50)))

# 4. 
def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


for num in squares(3, 7):
    print(num, end=" ")

print()  

# 5. 
def countdown(n):
    for i in range(n, -1, -1):
        yield i


print("Обратный отсчет:", list(countdown(10)))
