import sys
import os
import hashlib

if len(sys.argv) == 1:
	print 'Uso: python md5_generator <caminho/para/arquivo>. Abortando!'
	sys.exit(1)

if not os.path.exists(sys.argv[1]):
	print 'Arquivo nao exite. Abortando!'
	sys.exit(1)

f = open(sys.argv[1])

md5 = hashlib.md5()

for line in f:
	md5.update(line)

f.close()
print md5.hexdigest() + '  ' + sys.argv[1]
