# num = int(input("Enter num: "))
# divList = []

# for x in range(2, num):
#     if num % x == 0:
#         divList.append(x)
#         flag = True
#         break
#     else:
#         flag = False
# if flag == False:
#     print("Prime")
# else:
#     print("Composite")
#     print(divList)

num = int(input("Enter num: "))
def checkPrime(num):

    primeList = []
    flag = False
    i = 0
    n = 0
#    global flag
    if num == 2:
        flag = True
    else:
        for x in range(2, num):
            if num % x == 0:
                flag = False
                break
            else:
                flag = True

    while i < num:
        flag = checkPrime(n)
        if flag == True:
            primeList.append(n)
            i += 1
        n += 1
    print(primeList)

checkPrime(num)