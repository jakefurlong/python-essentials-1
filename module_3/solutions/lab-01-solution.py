# 3.1.1.4

# Solution

print("Running developer code: ")
n = int(input("Enter a number: "))

def is_greater_than_100(n):
    return False if n < 100 else True

print(f'{n} >= 100 is', is_greater_than_100(n))

# Driver code

print('\nRunning unit tests...')
  
test_numbers = [55, 99, 100, 101, -5, +123]

def unit_test(test_numbers):
    for i in test_numbers:
        response = is_greater_than_100(i)
        print(f'{i} >= 100 is {response}')

unit_test(test_numbers)