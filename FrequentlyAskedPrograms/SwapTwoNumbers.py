# Swap two numbers
num1 = 10
num2 = 20

# Approach 1
num1,num2 = num2,num1

# Approach 2
temp = num1
num1 = num2
num2 = temp

print(f"Num1:{num1}")
print(f"Num2:{num2}")

