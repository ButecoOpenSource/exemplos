import time
import atexit

def meChama():
	print 'Funcao chamada no encerramento do script'

def meChama2():
	print 'Serei chamado primeiro!'

# registrar a chamada da funcao no termino do script
atexit.register(meChama)
atexit.register(meChama2)

print 'As funcoes serao chamadas no encerramento do script'

time.sleep(3)
