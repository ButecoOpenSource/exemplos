from memory_profiler import profile

a = ['marcos paulo de souza', 'marcos paulo de souza', 'marcos paulo de souza', 'marcos paulo de souza', 'marcos paulo de souza', 'marcos paulo de souza']

@profile
def a():
	global a
	import moduloteste
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

	print a
	a.clear

a()
