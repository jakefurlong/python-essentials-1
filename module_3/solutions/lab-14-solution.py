# 3.6.1.9

# This simple solution is to return a set of the list, which removes all duplicates; however,
# the purpose of this exercise is to get practice with lists.

random_list = [1, 1, 2, 3, 4, 4, 4, 5, 5]

def remove_duplicates(dupes):
    result = []
    
    for i in dupes:
        if i not in result:
            result.append(i)
        else:
            continue
            
    return result

print(remove_duplicates(random_list))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    ([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 3, 3, 3, 3, 4, 5, 5],[1, 2, 3, 4, 5]),
    ([1, 1, 2, 3, 4, 5, 5, 5, 5, 5], [1, 2, 3, 4, 5])
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = remove_duplicates(input)
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
