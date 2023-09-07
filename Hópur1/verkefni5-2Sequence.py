n = int(input())  # Do not change this line

a, b, c =  1, 2, 3

for i in range (n):

    if i == 0:

        print(a)

    elif i == 1:
        print(b)

    elif i == 2:
        print(c)

    else:
        next_num = a + b +c 
        print (next_num)
        a, b, c = b, c, next_num
    



    