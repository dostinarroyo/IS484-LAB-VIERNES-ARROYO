class persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print(f"hola muy buenos dias me llamo {self.nombre},tengo {self.edad}")
persona_1=persona("Robert",19)
persona_1.saludar()
    



