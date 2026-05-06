# AULA COMPLETA: NUMEROS EM PYTHON 
""" 
Vamos aprender:
1- Tipos numéricos 
2- Conversões de tipos 
3- Hierarquia numérica 
4- Operações matemáticas 
5- Coerção de tipos
6- Verificação de tipos 
7- Entrada de dados 
"""

## PASSO 01 - TIPOS NUMÉRICOS
#===============================
# INT -> números inteiros
# FLOAT -> números com casas decimais 
# COMPLEX -> números complexos (usado em matemática/engenharia)

print ("===== TIPOS NUMÉRICOS =====") 

# EXEMPLO 01 - NUMERO INTEIRO 

#criamos uma variável chamada numero_inteiro
numero_inteiro = 10

#Mostramos o valor
print ("Valor:", numero_inteiro)

#Type()mostra qual é o tipo da variável
print ("Tipo:", type(numero_inteiro))

print ("-----------------------------")

# EXEMPLO 2 - NUMERO DECIMAL

# Float é um número com ponto decimal 
numero_decimal = 3.14 

print ("Valor:", numero_decimal) 
print ("Tipo:", type(numero_decimal)) 

print ("-----------------------------")

# EXEMPLO 3 - NUMEROS COMPLEXOS
# Um número complexo smepre possui duas partes:
# Parte real (número real)
# Parte imaginária (multiplicada por j)

# Estrutura Geral: 
# numero = a + bj 

# a > parte real
# b > parte imaginária 
# j > unidade imaginária 

numero_complexo = 2 + 3j 

print ("Valor:", numero_complexo) 
print ("Tipo:", type(numero_complexo)) 

print ("------------------------------")
