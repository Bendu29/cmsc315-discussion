"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented
programming (OOP) concepts in Python.

This program demonstrates inheritance, namespaces,
shallow copying, and deep copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.

class ParentClass:

    # Class variable
    device_type = "IT Device"

    def __init__(self, name, location):
        self.name = name
        self.location = location

    def display_info(self):
        print("Device Name:", self.name)
        print("Location:", self.location)


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.

class ChildClass(ParentClass):

    # New class variable
    category = "Computer"

    def __init__(self, name, location, operating_system, memory):
        super().__init__(name, location)

        self.operating_system = operating_system
        self.memory = memory

        # Nested mutable data
        self.software = ["Microsoft Office", "Antivirus"]

    # Override parent method
    def display_info(self):
        super().display_info()
        print("Operating System:", self.operating_system)
        print("Memory:", self.memory)
        print("Installed Software:", self.software)

    # New method
    def add_software(self, software_name):
        self.software.append(software_name)
        print(software_name, "has been installed.")


# TODO 3:
# Create a function that demonstrates class namespaces
# and instance namespaces.
#
# Requirements:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after creation.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():

    print("\n=== Namespace Demonstration ===")

    computer1 = ChildClass(
        "Dell Laptop", "Office", "Windows 11", "16GB"
    )

    computer2 = ChildClass(
        "HP Desktop", "IT Department", "Windows 10", "8GB"
    )

    print("\nClass Variable Through Class:")
    print(ChildClass.category)

    print("\nClass Variable Through Object:")
    print(computer1.category)

    # Add a new attribute to only computer1
    computer1.owner = "IT Support"

    print("\nComputer 1 Namespace:")
    print(computer1.__dict__)

    print("\nComputer 2 Namespace:")
    print(computer2.__dict__)

    print("\nChild Class Namespace:")
    print(list(ChildClass.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying
# and deep copying.
#
# Requirements:
# - Create an object containing nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original, shallow copy, and deep copy.
# - Explain the difference using comments.

def demonstrate_copying():

    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Lenovo Laptop", "Office", "Windows 11", "16GB"
    )

    # Create a shallow copy
    shallow = copy(original)

    # Create a deep copy
    deep = deepcopy(original)

    print("\nBefore Modification:")

    print("Original:", original.software)
    print("Shallow Copy:", shallow.software)
    print("Deep Copy:", deep.software)

    # Modify the original object's nested list
    original.software.append("Google Chrome")

    print("\nAfter Modification:")

    print("Original:", original.software)
    print("Shallow Copy:", shallow.software)
    print("Deep Copy:", deep.software)

    # A shallow copy shares the nested software list.
    # Therefore, changes to the original list also
    # appear in the shallow copy.

    # A deep copy creates an independent software list.
    # Therefore, changes to the original list do not
    # affect the deep copy.


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one parent object.
# - Create at least one child object.
# - Demonstrate inheritance by calling methods.
# - Call namespace demonstration.
# - Call copy demonstration.

def main():

    print("=== Unit 1 OOP Assignment ===")

    # Create parent object
    print("\n=== Parent Object ===")

    device1 = ParentClass("Network Printer", "Office")
    device1.display_info()

    # Create child object
    print("\n=== Child Object ===")

    computer1 = ChildClass(
        "Dell Laptop", "IT Department", "Windows 11", "16GB"
    )

    computer1.display_info()

    # Student-created extension
    print("\n=== Student Extension ===")

    computer1.add_software("Python")

    print("\nUpdated Computer Information:")
    computer1.display_info()

    # Demonstrate namespaces
    demonstrate_namespaces()

    # Demonstrate copying
    demonstrate_copying()


if __name__ == "__main__":
    main()