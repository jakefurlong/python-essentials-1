# 3.2.1.14

blocks = int(input("Enter the number of blocks: "))

def pyramid(blocks):
    if blocks == 0:
        return 0
    else:
        height = 0
        blocks_used = 0
    while blocks > 0:
        height += 1
        blocks_used += 1
        blocks -= blocks_used
        if blocks <= height:
            return height
    return height

print('The height of the pyramid:', pyramid(blocks))


pyramid(blocks)

# Driver code

print('\nRunning units tests...')

submit_cases = [
    (6, 3),
    (20,5),
    (1000, 44),
    (2, 1)
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = pyramid(input)
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