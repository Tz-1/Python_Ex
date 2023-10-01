class Libro:
    pass

libro_1 = Libro()
libro_1.autor = "Dan Brown"
libro_1.titulo = "Infierno"

libro_2 = Libro()
libro_2.autor = "Dan Brown"
libro_2.titulo = "Codigo Da Vinci"
libro_2.ann = 2003

print(libro_1.__dict__)
print(libro_2.__dict__)