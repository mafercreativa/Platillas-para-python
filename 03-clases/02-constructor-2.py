class Animal:
    
    def __init__(self):
        self.clase = "mamifero"
        self.especie = "perro"
        self.raza = "labrador golden"
    

dog = Animal()
cat = Animal()
cat.especie = 'gato'
cat.raza = 'criollito'

print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)
print('------------------------------------')
print(cat.clase)
print(cat.especie)
print(cat.raza)
print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)