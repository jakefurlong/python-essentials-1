# 3.2.1.3

secret_number = 777

def magic_number(n):
    print(
    """
    +================================+
    | Welcome to my game, muggle!    |
    | Enter an integer number        |
    | and guess what number I've     |
    | picked for you.                |
    | So, what is the secret number? |
    +================================+
    """)
    guess = 0
    while guess != secret_number:
        guess = int(input('Enter a number: '))
        if guess != secret_number:
            print('Ha ha! You\'re stuck in my loop!')
        else:
            print(f'You correctly guessed {guess}. Well done, muggle! You are free now.')

magic_number(secret_number)

# Driver code

# No driver code for this lab. Input is based on user input.