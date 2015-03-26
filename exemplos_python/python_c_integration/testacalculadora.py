import moduloteste

param1 = 1
param2 = 3

try:
	print 'Valor de ' + str(param1) + ' + ' + str(param2) + ': ' + str(moduloteste.soma(param1, param2))
except moduloteste.erro:
	print 'erro na lib'
