def factorialNumber(n):
    if n==0:
        return 1
    return n*factorialNumber(n-1)
user=int(input())
result=factorialNumber(user)
print(result)