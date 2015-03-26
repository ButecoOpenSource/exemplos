import moduloteste

print dir(moduloteste)

param1 = 1
param2 = 3

param3 = 'teste'

try:
	print 'Valor de ' + str(param1) + ' + ' + str(param2) + ': ' + str(moduloteste.soma(param1, param2))
except moduloteste.erro as e:
	print 'erro na lib: ' + str(e)

try:
	print 'String ' + param3 + ' duplicada' + ': ' + moduloteste.duplicastring(param3)
except moduloteste.erro as e:
	print 'erro na lib: ' + str(e)
