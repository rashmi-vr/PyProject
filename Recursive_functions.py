# sum of n numbers = 1+2+3+4+......+(n-1)+n
# sum(n) = sum(n-1) + n

def sum_recursive(n):
    if n==1 or n==0:
        return 1
    return n + sum_recursive(n-1)

s = sum_recursive(10)
print (s)

# factorial of n = n! = 1*2*3*4*5*........*(n-1)*n
# n! = (n-1)! * n

def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n * factorial_recursive(n-1)

f = factorial_recursive(5)
print (f)

