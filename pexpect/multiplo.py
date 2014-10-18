sp.sendline('something')

ret = sp.expect([pexpect.EOF, pexpect.TIMEOUT, 'a', 'b'], 15)

if ret == 0:
	print 'Recebido EOF do processo'
elif ret == 1:
	print 'Estourado tempo limite de espera'
elif ret == 2:
	print 'Recebido a'
elif ret == 3:
	print 'Recebido b'
