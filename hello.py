# # Ask the user for their name
# name = input("What is your name? ").strip().title()  # Best Practice

# name = name.strip()  # Remove any leading/trailing whitespace
# name = name.capitalize()  
# name = name.title()# Capitalize the first letter of the name
# print("Hello, " + name)
# print("Hello,", name)
# print(f"Hello, {name}") # best practice

# #  def - define
def main(): 
    name = input("what's your name? ")
    print(hello(name))

def hello(to="World"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()


