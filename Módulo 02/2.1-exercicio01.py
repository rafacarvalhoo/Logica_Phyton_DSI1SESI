# ======================================================
# MÓDULO 1 — CRIAÇÃO DE STRINGS
# ======================================================

# EX 01
texto1 = "logica"
print(texto1)

# EX 02
texto2 = 'Eu sou top em python' 
print(texto2) 

# EX 03
string = 'Copa "padrão fifa"' 
print(string)

# EX 04
string2 = "Copa 'padrão fifa'" 
print(string2) 

# ======================================================
# MÓDULO 2 — STRINGS MULTILINHA
# ======================================================

# EX 05 
menu = """\
Uso: Programa [OPÇÕES]
-A Exibe ajuda
-E Executa agora, quero jogar!
"""
print(menu)

# EX 06
poema = """\
No silêncio da tarde, floresce o pensamento,
O vento leva sonhos por caminhos de luar,
E o coração descansa no abraço do momento.
"""
print(poema)

# ======================================================
# MÓDULO 3 — CONCATENAÇÃO AUTOMÁTICA
# ======================================================

# EX 07
texto = ("Volei" "top")
print(texto) 

# EX 08
texto2 = ("Python" "é" "demais")
print(texto2)

# ======================================================
# MÓDULO 4 — STRINGS COMO SEQUÊNCIAS
# ======================================================

# EX 09
st = "software"
print("Primeira letra:", st[0]) 

# EX 10
print("Última letra:", st[-1])

# EX 11
print("Trecho1:", st[1:4])

# EX 12
print("Do ínicio até 3:", st[:3])

# EX 13
print("Do 2 até o fim:", st[2:])

# EX 14
print("Tamanho:", len(st))

# EX 15
print("Última letra:", st[7])

# EX 16
print(st[::2])

# EX 17
print(st[::-1])