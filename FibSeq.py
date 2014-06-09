def fib_seq(num):
    a = 1
    b = 0
    seq = []
    for i in range(0, num):
        seq.append(str(a + b))
        a = int(seq[i])
        if i - 1 < 0:
            b = 0
        else:
            b = int(seq[i-1])

    seq = ', '.join(seq)
    return seq

print "To what nth term would you like to see the Fibonacci Sequence?"

while True:
    nth = raw_input("> ")
    if not nth.isdigit():
        print "Integers only"
    else:
        break

print fib_seq(int(nth))
