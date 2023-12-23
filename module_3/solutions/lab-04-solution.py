year = int(input("Enter a year: "))

def is_leap_year(year):
    result = ''
    if year % 4 != 0:
        result = 'Common year'
    elif year % 100 != 0:
        result = 'Leap year'
    elif year % 400 != 0:
        result = 'Common year'
    else:
        result = 'Leap year'
    return result

print(is_leap_year(year))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    (2000, 'Leap year'),
    (2015, 'Common year'),
    (1999, 'Common year'),
    (1996, 'Leap year')
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = is_leap_year(input)
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
