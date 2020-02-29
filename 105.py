## Usando a lista: ['a','b','c']
# 1) Faca um loop para retornar: ['A','B','C']

def caps(lista):
	for c in lista:
		c = c.upper()
		print(c)



## Usando os numeros: [0, 1, 3, 4, 5]
# 2) Faca um loop para retornar a soma de todos os elementos da listas
def somas(listaNum):
	total = 0
	for soma in listaNum:
		total += soma 
	return total

	

# 3) Faca um loop para retornar apenas os numeros impares
def impares(listaNum):
	for i in listaNum:
		if(i%2 == 1):
			print(i)



caps(['a, b, c'])
print('Total = ', somas([0, 1, 3, 4, 5]))	
impares([0, 1, 3, 4, 5])				

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'


# 4) Conte quantas palavras de tamanho >= 5 existe nessa string
def contTamanho(frase):
	cont = 0
	frase = frase.replace(',', ' ').split(' ')
	for ver in frase:
		if(len(ver)>= 5):
			cont += 1 
	return cont

print(contTamanho( 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'))