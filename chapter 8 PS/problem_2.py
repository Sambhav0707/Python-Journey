def sumOfN(n):
    if n==0:
        return 0
    return n + sumOfN(n-1)

n = int(input("enter the number: "))

total = sumOfN(n)

print(total)

