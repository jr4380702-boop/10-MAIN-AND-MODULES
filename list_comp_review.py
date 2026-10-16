import random

# use list comprehension to create a new list of surnames
surnames = ["GOAT", "Living Thing", "Imposter", "Banana"]
students = ["Even", "Zach", "Jace","Mr. Klins", "Christian", "Duane", "John"]

# use list comprehension to create a new list with the names combined with a random surname
student_names = [student + " the " + random.choice(surnames) for student in students if student != "Mr. Klins"]
print(student_names)
