import os
from ctypes import *

lib = CDLL('/tmp/minha_lib.so')

print(lib.soma(2, 3))
print(lib.inc(5))

fname = '/tmp/arquivo_python'

lib.cria_arquivo(fname)

if os.path.exists(fname):
	print('Arquivo existe! Conteudo: ')
	with open(fname) as f:
		print(f.read())
