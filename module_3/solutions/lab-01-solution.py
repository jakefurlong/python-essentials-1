# 3.1.1.4

# Solution

print("Running developer code: ")
n = int(input("Enter a number: "))

def is_greater_than_100(n):
    return False if n < 100 else True

print(f'{n} >= 100 is', is_greater_than_100(n))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    (55, False),
    (99, False),
    (100, True),
    (101, True),
    (-5, False),
    (+123, True)
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = is_greater_than_100(input)
    print(f"Actual: {result}")
    if result == expected_output:
        print("Pass")
        return True
    print("Fail")
    return False

def main():
    passed = 0
    failed = 0
    for test_case in submit_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")

main()