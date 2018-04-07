a = 0
b = 1
def fibonacci(i = 0):
    global a
    global b
    if i == 10:
        exit()
    else:
        print(a)
        print(b)
        a += b
        b += a
        i += 1
        fibonacci(i)

fibonacci()