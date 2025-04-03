# 5! = 1*2*3*4*5 = 120

# Approach 1

factorial = 1
num = int(input())
if num<=0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"Factorial of {num} is {factorial}")

# Approach 2 Recursion method

def fact(n):
    # if n == 0:
    #     return 1
    # return n*fact(n-1)
    return 1 if (n==0) else n*fact(n-1)
n=int(input())
print(fact(n))