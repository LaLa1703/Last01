
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result < 2:
            print('Составное')
            return
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                return
        print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(a, b, c):
    result = a + b + c
    return result

result = sum_three(2, 3, 6)
print(result)