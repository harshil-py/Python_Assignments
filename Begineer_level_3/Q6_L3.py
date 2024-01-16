"""
6. Create the custom Python classes which have methods and
attributes and implement single inheritance, multiple inheritance,
and multilevel inheritance.
"""

"Single Inheritance"

class Parent:
    def __init__(self,hair, height):
        self.hair = hair
        self.height = height

class Child(Parent):
    def __init__(self,hair, height, complexion):
        super().__init__(hair, height)
        self.complexion = complexion


"Multiple Inheritance"

class Parent:
    def __init__(self, hair, height):
        self.hair = hair
        self.height = height

class GrandParent:
    def __init__(self,gen_disorder):
        self.gen_disorder = gen_disorder

class Child(Parent, GrandParent):
    def __init__(self,hair, height, complexion, gen_disorder):
        Parent.__init__(self, hair, height)
        GrandParent.__init__(self, gen_disorder)
        self.complexion = complexion

"Multilevel Inheritance"

class GrandParent:
    def __init__(self,lastname):
        self.lastname = lastname

class Parent(GrandParent):
    def __init__(self, hair, height, lastname):
        self.hair = hair
        self.height = height
        GrandParent.__init__(self, lastname)

class Child(Parent):
    def __init__(self,hair, height, complexion, lastname):
        Parent.__init__(self, hair, height, lastname)
        self.complexion = complexion
