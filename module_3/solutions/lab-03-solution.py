# 3.1.1.11

income = float(input("Enter your income: "))

def pit(income):
    if income < 85_528:
        tax = income * 0.18 - 556.02
        return 0.0 if tax < 0 else round(tax, 0)
    else:
        tax = 14_839.02 + (income - 85_528) * 0.32
        return round(tax, 0)

tax = pit(income)

print(f"The tax is: {tax} thalers")

# driver code

print('\nRunning units tests...')

submit_cases = [
    (10000, 1244.0),
    (100000,19470.0),
    (1000, 0.0),
    (-100, 0.0)
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = pit(input)
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