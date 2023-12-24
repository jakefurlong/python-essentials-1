# 3.4.1.6

def hat_trick():
    hat_contents = [1, 2, 3, 4, 5]

    middle_int = int(input("Enter a number: "))
    hat_contents[2] = middle_int
    del hat_contents[-1]

    print(len(hat_contents))

hat_trick()

# Driver code

# There are no tests for this lab