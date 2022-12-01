def get_fib(position):
    if position + 1 <= 2:
        return position
    else:
        sum = get_fib(position - 2) + get_fib(position - 1)
        return sum

# Test cases
print (get_fib(0))