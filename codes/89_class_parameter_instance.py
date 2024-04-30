"""
    Define a class, which have a class parameter and have a same instance parameter.
"""


class X:
    name = "sidharth"

    def display(self, name=None):
        self.name = name
        print(f"name = {self.name}")


obj = X()
print(obj.name)  # access class parameter
obj.display(name="rashwana")  # access method parameter
