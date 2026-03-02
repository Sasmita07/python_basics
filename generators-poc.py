def remote_control_next():
    yield "apple"
    yield "orange"

itr = remote_control_next()
print(next(itr))
print(next(itr))

for c in remote_control_next():
    print(c)

def fibonacci_sequence():
    a, b = 0, 1
    while True:
        yield a
        a = b
        b = a + b

for fib in fibonacci_sequence():
    if fib > 100:
        break
    print(fib)
