class A:
    def __init__(self):
        print("Pertenezco a la clase A")
    def metodo_a(self):
        print("Método heredado de A")

class B:
    def __init__(self):
        print("Clase B")
    def metodo_b(self):
        print("Método heredado de B")

class C(B, A):
    def metodo_c(self):
        print("Metodo de Clase C")

classC = C()

classC.metodo_a()
classC.metodo_b()
classC.metodo_c()