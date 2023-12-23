# 3.1.1.10

# Solution

user_string = input("Enter a plant name: ")

def is_spathiphyllum(user_string):
    if user_string == 'Spathiphyllum':
        return 'Yes - Spathiphyllum is the best plant ever!'
    elif user_string == 'spathiphyllum':
        return 'No, I want a big Spathiphyllum'
    else:
        return f'Spathiphyllum! Not {user_string}!'
    
print(is_spathiphyllum(user_string))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    ('spathiphyllum', 'No, I want a big Spathiphyllum'),
    ('pelargonium', f'Spathiphyllum! Not pelargonium!'),
    ('Spathiphyllum','Yes - Spathiphyllum is the best plant ever!')
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = is_spathiphyllum(input)
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