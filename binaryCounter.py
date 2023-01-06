def binaryConverter(num):
    numOfBits = 8
    bitArr = []
    while num != 0:
        quotient = num // 2
        remainder = num % 2
        num = quotient
        bitArr.append(remainder)
    bitArr.reverse()
    if len(bitArr) < numOfBits:
        for x in range(numOfBits-len(bitArr)):
            bitArr.insert(0, 0)
    return bitArr

def binaryCounter(amount):
    for x in range (amount):
        print(binaryConverter(x))

num = int(input("Enter count: "))
if num > 2 ** 8:
    num = int(input("Out of range of an octet. Please try again: "))
# check = True
# while check == True:
#     numOfBits = int(input("Enter amount of bits: "))
#     if num > numOfBits:
#         numOfBits = int(input("Enter amount of bits: "))
#     else:
#         check = False

binaryCounter(num + 1)