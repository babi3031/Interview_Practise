# check number is prime or Not
# Natural Numer >1
# Which has only 2 factors 1 and itself
#
# 19 -> 1 and 19 -> Prime Number
# 28 -> 1,2,3,4,14,28 -> Not a prime Number

# Approach 1
def is_prime(num):
    count = 0
    if num>1:
        for i in range(1,num+1):
            if num%i == 0:
                count+=1
    if count ==2:
        print(f"{num} is a prime number")
        return True
    else:
        print(f"{num} is not a prime number")
        return  False
user=int(input())
result=is_prime(user)
print(result)

# Approach 2
def isPrime(num):
    if num<=1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i == 0:
            return False
    return True

def generateTwinPrime(start,end):
    twin_prime = []
    for num in range(start,end-1):
        if isPrime(num) and isPrime(num+2):
            twin_prime.append((num,num+2))
    return twin_prime

start = int(input("Enter start number:"))
end = int(input("Enter end number:"))
result=generateTwinPrime(start,end)

for twinPrime in result:
    print(f"Twin primes:{twinPrime}")