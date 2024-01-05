# 2.6.1.10

x = int(input("Enter a value for x: "))

def weird_math(x):
    y = 1 / (x + (1 / x + (1 / (x / (1 / x)))))
    return y 

print(weird_math(x))