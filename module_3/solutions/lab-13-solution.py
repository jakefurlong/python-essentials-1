# 3.4.1.13

def line_up():
    beatles = []
    beatles.append('John Lennon')
    beatles.append('Paul McCartney')
    beatles.append('George Harrison')
    
    for beatle in beatles[0:2]:
        b = input("Enter a band member name: ")
        beatles.append(b)

    del beatles[3:]

    beatles.insert(0,'Ringo Starr')

    return beatles

print(line_up())

# Driver code

# There are no tests for this lab