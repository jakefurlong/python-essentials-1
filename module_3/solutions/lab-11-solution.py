
c0 = int(input('Enter a number: '))

def collatz(c0):
    counter = 0

    while c0 > 1:

        if c0 % 2 == 0:
            c0 /= 2
        else:
            c0 = c0 * 3 + 1
        print(int(c0))
        counter += 1
    print(f'Steps = {counter}')
    return counter

# Driver code

print('\nRunning units tests...')

submit_cases = [
    (15, 17),
    (16, 4),
    (1023, 62)
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = collatz(input)
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

