# EX 01
ano = 2024 
print(type(ano))

# EX 02
print(isinstance(3.14159, float))

# EX 03
print(type(100)) == type(True)

# EX 04
print(isinstance(True, int))

# EX 05
resultado = 5 / 2

print(type(resultado)) 
print(isinstance(resultado, float))

# EX 06
def verifica_numero(valor):
    if isinstance (valor, (int, float, complex)):
        print("EX06: É número")
    else: 
        print("Ex06: Não é número") 
verifica_numero(42) 
verifica_numero("texto")

# EX 07
print(type(True) == int)
print(isinstance(True, int))

# EX 08
numero_complexo = 3 + 4j
print(type(numero_complexo))

# EX 09
print(isinstance(None, type (None)))

# EX 10
numero = 3.0

print(isinstance(numero, (int, float, complex)))
print(isinstance(numero, int))