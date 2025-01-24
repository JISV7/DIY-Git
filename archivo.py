import os


class Archivo:
    def __init__(self, name):
        self.name = name

    def read(self):
        with open(self.name, "r") as f:
            return f.read()

    def write(self, other):
        with open(self.name, "w") as f:
            f.write(other)

    def add(self, other):
        if not os.path.exists(self.name):
            raise FileNotFoundError(f"El archivo '{self.name}' no existe.")
        with open(self.name, "a") as f:
            f.write("\n" + other)


"""
import hashlib
archivo = Archivo("archivo.txt")
archivo.write("Hola mundo")
archivo.add("\nSegunda linea")
print(id(archivo))
printhashlib.md5(archivo)
"""
