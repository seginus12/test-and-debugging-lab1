def is_prime(number):
    if number > 1:
        for i in range(2, int(number / 2) + 1):
            if (number % i) == 0:
                return False
        else:
            return True
    return False

print(is_prime(281))
