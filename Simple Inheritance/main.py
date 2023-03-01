from classes import *
# importa todas as classes de uma vez
"""
Associação - Usa outro objeto | 
Agregação - Tem outro objeto
| Composição - É dono de outro ou outros objetos
| Herança - É outro objeto
"""

c1 = Cliente('Luiz', 45)
#p  rint(c1.nome)
c1.falar()
c1.comprar()

a1 = Aluno('Maria', 54)
# print(a1.nome)
a1.falar()
a1.estudar()