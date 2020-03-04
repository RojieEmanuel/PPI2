professor1 = {'id':42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}

professor3 = dict(id=28, name='Jorge Armino', idade=37)

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla
# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos
a = dir(list)
print('=========================================== MÉTODOS DE LISTA =======================================', '\n')
print(a)
print('=========================================== FIM ====================================================', '\n')

b = dir(tuple)
print('=========================================== MÉTODOS DE TUPLA =======================================', '\n')
print(a)
print('=========================================== FIM ====================================================', '\n')

# lista
list = [2, 3, 5, 7, 11, 13, 17, 19]
# tupla
tuple = (2, 3, 5, 7, 11, 13, 17, 19)



print("=========================================== LISTA ==================================================", '\n')
print("Lista:", list)

print("Inserindo elemento no final da Lista:", '\n')
list.append(22)
print(list)

print("Concatenando Listas:", '\n')
list.extend(list)
print(list)

print("Inserindo elementos em determinada posição:", '\n')
list.insert(0, 0)
print(list)

print("Removendo elementos:", '\n')
list.remove(0)
print(list)


print("Remove o item que está no indice passado:", '\n')
list.pop()
print(list)


print("Descobrindo o índice do número 7 na Lista:", '\n')
print(list.index(7))

print("contando quantas vezes o número 2 aparece na Lista:", '\n')
print(list.count(2))

print("Invertendo lista:", '\n')
list.reverse()
print(list)

print("Ordenando elementos:")
list.sort()
print(list)

print("========================================== TUPLA ==================================================", '\n')
print("Tupla:", tuple)


print("Tuplas são imutáveis em sua maioria, com raras exceções, por isso todos os métodos que existem na lista de manipulação, não podem ser utilizados nas tuplas.", '\n')

# tuple.append(22)
# tuple.extend(tuple)
# tuple.insert(0, 0)
# tuple.remove(0)
# tuple.pop()
print("Descobrindo o índice do número 7 na Tupla:", '\n')
print(tuple.index(7))

print("contando quantas vezes o número 2 aparece na Tupla:", '\n')
print(tuple.count(2))




# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py
professor1['latitude'] = '22º 27´N'
professor1['longitude'] = '113º 56´E'

professor2['latitude'] = '38º 4´N'
professor2['longitude'] = '9º 8´W'

professor3['state_origin'] = 'Rio Grande do Sul'
professor3['courses'] = ['Filosofia', 'Informática e Sociedade']
professor3['latitude'] = '22º 55´S'
professor3['longitude'] = '34º 53´W'


print(professor1,'\n')
print(professor2,'\n')
print(professor3,'\n')