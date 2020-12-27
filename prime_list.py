def is_prime(x):

    prime = True
    if x < 2:
        prime = False
    else:
        for n in range(2, x):
            if x % n == 0:
                prime = False
                break
            else:
                prime = True
    return prime

for x in range (1, 101):
    if is_prime(x):
        print('\n' + str(x) + ' is a prime number.')
    else:
            print('\n' + str(x) + ' is not a prime number.')
