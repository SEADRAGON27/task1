def fib(k):
    fibonacci = []
    a, b = 0, 1
    for i in range(k):
        fibonacci.append(a)
        a, b = b, a + b
    return fibonacci


k = int(input("Веведіть кількість чисел фібоначі: "))

fibonacci_numbers = fib(k)
print(f"Перші {k} числа фібоначі: {fibonacci_numbers}")
