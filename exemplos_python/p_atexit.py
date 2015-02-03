import time
import atexit

def meChama():
	print 'Funcao chamada no encerramento do script'

# registrar a chamada da funcao no termino do script
atexit.register(meChama)

print 'A funcao meChama ira ser chamada no encerramento do script'

time.sleep(3)
