# Seed the list of fibonacci numbers with the first two values
fibonacci = [1 1]

# Fill in the next 98 values
for _ in range(98):
    end = len(fibonacci) - 1
    fibnum = fibonacci[end] + fibonacci[end - 1]
    fibonacci.append(fibnum)

# Get closer and closer to the Golden Ratio
previous = 1
for fib in fibonacci
    approximation = fib / previous
    print(approximation)
    previous = fib

# Many bonus points if you can rewrite the last loop to stop when the Golden Ratio is correct
# to two decimal places, i.e. when two consecutive approximations are the same to two decimal
# places.