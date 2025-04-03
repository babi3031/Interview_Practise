def generteFibonacciloop(n):
    fib_series = [0,1]
    if n <= 0:
        return []
    elif n==1:
        return [0]
    else:
        for i in range(2,n):
            next_fib_series = fib_series[i-1]+fib_series[i-2]
            fib_series.append(next_fib_series)
        print(len(fib_series))
        return fib_series

n=int(input())
result = generteFibonacciloop(n)
print(result)

"""
Implement a function generateFibonacciRecursion to generate
the Fibonacci series up to the nth term using recursion.
"""
# def generateFibonacciRecursion(n):
#     if n <= 0:
#         return []
#     elif n == 1:
#         return [0]
#     elif n == 2:
#         return [0, 1]
#     else:
#         fibonacci_series = generateFibonacciRecursion(n - 1)
#         fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
#         return fibonacci_series
#
# # Example usage:
# n = 10
# result = generateFibonacciRecursion(n)
# print(result)  # Output: [0, 1, 1, 2, 3, 5, 8, 13]


# def fib_series():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# fib=fib_series()
# for _ in range(10):
#     print(next(fib))

# def even_numbers(n):
#     for i in range(n):
#         if i % 2 == 0:
#             yield i
#
#
# # Using the generator
# even_gen = even_numbers(10)
# for num in even_gen:
#     print(num)