import random
from colorama import Fore
from colorama import init
init()

class Object:
    class Generate:
        def __init__(self, nameobject):
            list_of_typeclass = ["Rect", "Triangle", "Circle"]
            self.TypeClass = list_of_typeclass[random.randint(0, 2)]
            self.coordinates = (random.randint(0, 1000), random.randint(0, 1000))
            self.nameobject = nameobject
            if self.TypeClass == "Circle":
                self.range = random.randint(0, 1000)
            else:
                self.width = random.randint(0, 1000)
                self.height = random.randint(0, 1000)
    class Rect:
        def __init__(self, nameobject, coordinates, width, height):
            self.TypeClass = "Rect"
            self.coordinates = coordinates
            self.nameobject = nameobject
            self.width = width
            self.height = height

    class Triangle:
        def __init__(self, nameobject, coordinates, width, height):
            self.TypeClass = "Triangle"
            self.coordinates = coordinates
            self.nameobject = nameobject
            self.width = width
            self.height = height

    class Circle:
        def __init__(self, nameobject, coordinates, range):
            self.TypeClass = "Circle"
            self.coordinates = coordinates
            self.nameobject = nameobject
            self.range = range

    def showinfo(self):
        if self.TypeClass == "Rect":
            picture = [ [" ", " ", " ", " ", " ", " ", " "],
                        [" ", " ", "#", "#", "#", " ", " "],
                        [" ", " ", "#", "#", "#", " ", " "],
                        [" ", " ", "#", "#", "#", " ", " "], ]
        if self.TypeClass == "Triangle":
            picture = [ [" ", " ", " ", "#", " ", " ", " "],
                        [" ", " ", "#", "#", "#", " ", " "],
                        [" ", "#", "#", "#", "#", "#", " "],
                        ["#", "#", "#", "#", "#", "#", "#"], ]
        if self.TypeClass == "Circle":
            picture = [ [" ", " ", "#", "#", "#", " ", " "],
                        [" ", "#", "#", "#", "#", "#", " "],
                        [" ", "#", "#", "#", "#", "#", " "],
                        [" ", " ", "#", "#", "#", " ", " "], ]
        for i in range(len(picture)):
            for j in range(len(picture[i])):
                print(Fore.GREEN + picture[i][j], end=' ')
            print()
        if self.TypeClass == "Circle":
            print(Fore.RESET + f"\n\nType: {self.TypeClass}\nObject name: {self.nameobject}\nPosition: {Fore.RED} x, {Fore.GREEN} y {Fore.RESET} = {self.coordinates}\nRange: {self.range}\n\n")
        else:
            print(Fore.RESET + f"\n\nType: {self.TypeClass}\nObject name: {self.nameobject}\nPosition: {Fore.RED} x, {Fore.GREEN} y {Fore.RESET} = {self.coordinates}\nScale: Width = {self.width}, Height = {self.height}\n\n")