
k = 0
p = 0
summa = 0

n = int(input())
m = int(input())


for i in range (20 , n):
    k = i // 10
    p = i % 10
    summa = p + k
    if summa ** 2 == i:
        print(i)



for i in range(1,n):
    sum=0
    for j in range(1 ,i+1):
        if i % j == 0:
            sum += 1
    if sum == m:
        print(i)