# A series of numbers in which each number is the sum of the two preceding numbers.
# 0 1 1 2 3 5 8 13 21 . . . .

# Aproach 1

def fib_series(n):
    fib_series = [0,1]
    if n<=0:
        return []
    elif n == 1:
        return [0]
    else:
        for i in range(2,n):
            new_fib = fib_series[i-1]+fib_series[i-2]
            fib_series.append(new_fib)
        return fib_series

n=int(input())
print(fib_series(n))

# Aproach 2 Recrusion method

def fib_series(n):
    if n<=0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    else:
        new_fib = fib_series(n-1)
        new_fib.append(new_fib[-1]+new_fib[-2])
        return new_fib

n=int(input())
print(fib_series(n))

# Aproach 3 using Generators

def fib_series():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

fib=fib_series()
for i in range(10):
    print(next(fib))