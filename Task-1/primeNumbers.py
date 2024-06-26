def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


a = int(input("Введіть a: "))
b = int(input("Введіть b: "))

print(f"Прості числа між {a} і {b}:")
for num in range(min(a, b), max(a, b) + 1):
    if is_prime(num):
        print(num)
