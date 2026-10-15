pi = 3.14159


def square(x):
    return x ** 2


def cude(x):
    return x ** 3


def circumference(radius):
    return 2 * pi * radius


def area(radius: float) -> float:
    """
    Takes the radius of a circle and returns the area
    """
    return pi * (radius ** 2)

if __name__ == "__main__":
    print("Just Testing")
    print(area(7))
    print(pi)
    # Every python file (aka Module) has a special built in variable called __name__
    # If you run the file directly, __name__ is set to "__main__"
    # If you import the file, __name__ becomes the name of that script
    print(__name__)
    print("Just Testing")
    

