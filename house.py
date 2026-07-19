name = input("what's your name? ")

match name:
    case "Radha" | "Krishna" | "Balram":
        print("Vrindavan")
    case "Ram" | "Sita":
        print("Ayodhya")
    case "Shiva" | "Parvati":
        print("Kailash")
    case _:
        print("1")