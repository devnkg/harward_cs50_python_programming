# students = ["sita", "ram", "hari", "vishnu"]
# houses = ["mithila", "ayodhya", "vaikunth", "bhaktapur"]

# for students in students:
#     print(students)
    
# for i in range(len(students)):
#     print(i + 1, students[i])

# names = {
#     "ram": "ayodhya", 
#     "sita": "mithila", 
#     "hari": "bhaktapur", 
#     "vishnu": "vaikunth"
# }

# for name in names:
#     print(name, names[name], sep=", ")

from unicodedata import name


gods = [
    {"name": "ram", "house": "ayodhya", "weapon": "bow"},
    {"name": "sita", "house": "mithila", "weapon": "lotus"},
    {"name": "krishna", "house": "vrindavan", "weapon": "flute"},
    {"name": "radha", "house": "barsana", "weapon": None}
]

for god in gods:
    print(god["name"], god["house"], god["weapon"], sep=", ")