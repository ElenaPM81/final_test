from codeop import typeCompiler


class Animal:
    def _init_(self, name):
        self.name = name

class Pet(Animal):
    def _init_(self, name, type):
        super()._init_(name)
        self.type = type

class Dog(Pet):
    def _init_(self, name, type):
        super()._init_(name,type)   

class Cat(Pet):
    def _init_(self, name, type):
        super()._init_(name,type) 

class Hamster(Pet):
    def _init_(self, name, type):
        super()._init_(name,type) 

class PackAnimal(Animal):
    def _init_(self, name, type):
        super()._init_(name)
        self.type = type


class Horse(PackAnimal):
    def _init_(self, name, type):
        super()._init_(name,type) 

class Donkey(PackAnimal):
    def _init_(self, name, type):
        super()._init_(name,type) 