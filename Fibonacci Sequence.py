# Fibonacci Number
# 0, 1, 1, 2, 3, 5, 8,......
# f0 = ?, f1 = ? 

def fibo(number):
    if number <= 1:
        return number
    else:
        return fibo(number - 1) + fibo(number - 2)

for i in range(13):
    print(fibo(i))