# 3.2.1.11

user_word = input("Enter a word: ")

def vowel_eater(user_word):
    user_word = user_word.upper()
    vowels = ['A','E','I','O','U']
    result = ''
    for letter in user_word:
        if letter in vowels:
            continue
        else:
            result += letter
    return result   

print(vowel_eater(user_word))

# Driver code

print('\nRunning units tests...')

submit_cases = [
    ('Gregory', 'GRGRY'),
    ('abstemious','BSTMS'),
    ('IOUEA','')
]

def test(input, expected_output):
    print("---------------------------------")
    print(f"Input: {input}")
    print(f"Expecting: {expected_output}")
    result = vowel_eater(input)
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