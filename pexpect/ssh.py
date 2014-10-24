def Login(username server password):
	sp = pexpect.spawn('/usr/bin/ssh ' + username + '@' + server)

	while True:
		ret = sp.expect(['Are you want to continue connecting (yes/no)?', 'password:'])

		if ret == 0:
			sp.sendline('yes')
		else:
			sp.sendline(password)
			break

	sp.interact()
