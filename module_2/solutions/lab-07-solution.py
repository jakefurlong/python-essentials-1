# 2.4.1.10

x =  0

def algebriac_notation(x):
    x = float(x)
    y = 3*x**3 - 2*x**2 + 3*x - 1
    return y

print(algebriac_notation(x))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    (0, -1.0),
    (1, 3.0),
    (-1, -9.0)
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = algebriac_notation(input)
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