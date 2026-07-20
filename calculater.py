# #int

# x = input("What'is the x? ")

# y = input("What'is the y? ")

# z = int(x) + int(y)

# print(z)

# x = int(input("what's the x? "))

# y = int(input("what's the y? "))

# z = x + y

# print(z)

# #standard and readable way to do it

# x = int(input("what's the x? "))

# y = int(input("what's the y? "))

# print(x + y)

# print(int(input("what's the x? ")) + int(input("what's the y? ")))



# #float

# x = float(input("what's the x? "))

# y = float(input("what's the y? "))

# print(x + y)

# x = float(input("what's the x? "))

# y = float(input("what's the y? "))

# z = round(x + y)

# print(z)

# x = float(input("what's the x? "))

# y = float(input("what's the y? "))

# z = round(x + y, 2)

# print(z)

# x = float(input("what's the x? "))

# y = float(input("what's the y? "))

# z = x + y

# print(f"{z:.2f}")


# /

# x = float(input("what's the x? "))

# y = float(input("what's the y? "))

# z = x / y

# print(f"{z}")


# def

def main(): 
    x = int(input("what's the x? "))
    print("x sqaure is", square(x))

# def square(n):
#     return n + n

def square(n):
    return pow(n, 2)

if __name__ == "__main__":
    main()