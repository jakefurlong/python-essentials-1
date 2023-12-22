# 3.1.1.10

# Solution

user_string = input("Enter a plant name: ")

def is_spathiphyllum(user_string):
    if user_string == 'Spathiphyllum':
        return 'Yes - Spathiphyllum is the best plant ever!'
    elif user_string == 'spathiphyllum':
        return 'No, I want a big Spathiphyllum!'
    else:
        return f'Spathiphyllum! Not {user_string}!'
    
print(is_spathiphyllum(user_string))

# Driver code

# Create driver code here