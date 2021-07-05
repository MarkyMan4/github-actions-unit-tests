# collection of functions that I can run test cases on

# find nth number in Fibonacci sequence
def fib(n):
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)

# return the index of some element in a list, if it doesn't exist, return -1
def get_index(xs, x):
    index = -1

    for i in range(len(xs)):
        if xs[i] == x:
            index = i
            break

    return index

# reverse a string
def reverse_string(s):
    rev = list(s)

    for i in range(int(len(rev) / 2)):
        temp = rev[i]
        rev[i] = rev[len(rev) - i - 1]
        rev[len(rev) - i - 1] = temp

    return ''.join(rev)
