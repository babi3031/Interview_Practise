n = input('Enter any name or word:')
for i in range (0,len(n)):
    for j in range(0,i+1):
        print(n[j], end=" ")
    print()

# output
# b
# b a
# b a b
# b a b i

n = int(input("Enter a number: "))
for i in range(0, n):
    m = 0
    for j in range(0,i+1):
        m+=1
        print(m,end="  ")
    print()

# output
# 1
# 1  2
# 1  2  3
# 1  2  3  4

n = int(input("Enter a number: "))
for i in range(n, 0, -1):
    m = 0
    for j in range(0, i):
        m += 1
        print(m, end="  ")
    print()

# output
# 1  2  3  4
# 1  2  3
# 1  2
# 1

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    # Print leading spaces
    for s in range(n - i):
        print("   ", end="")

    # Print the increasing part of the sequence
    for j in range(1, i + 1):
        print(j, end="  ")

    # Print the decreasing part of the sequence
    for j in range(i - 1, 0, -1):
        print(j, end="  ")

    print()

# output
#          1
#       1  2  1
#    1  2  3  2  1
# 1  2  3  4  3  2  1