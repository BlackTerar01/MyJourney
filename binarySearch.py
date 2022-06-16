input_array = [1,3,9,11,15,19]
value = 11
def binary_search(input_array, value):
    arrLength = len(input_array)
    checkEven = False
    start = 0
    checkNum = False
    end = arrLength - 1
    middle = 0
    if arrLength % 2 == 0:
        checkEven = True
    if checkEven == False:
        for element in range(start, end):
            middle = (end + start)//2
            if input_array[middle] == value:
                checkNum = True
                break
            elif value < input_array[middle]:
                end = middle - 1
            elif value > input_array[middle]:
                start = middle + 1
    else:
        end = arrLength
        for element in range(start, end):
            middle = ((end + start)//2)
            if input_array[middle] == value:
                checkNum = True
                break
            elif value < input_array[middle]:
                end = middle
            elif value > input_array[middle]:
                start = middle
    if checkNum == True:
        return (middle + 1)
    return -1

# test_val1 = 25
# print (binary_search(test_list, test_val1))
# print (binary_search(test_list, test_val2))