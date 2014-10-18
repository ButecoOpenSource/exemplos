import pexpect

user = 'user'
password = 'pass'
server = '192.168.1.1'
command = 'ls'

sp = pexpect.spawned('telnet ' + server)

sp.expect(['username:'])
sp.sendline(user)

sp.expect(['password:'])
sp.sendline(password)

sp.expect(['%'])
sp.sendline(command)

sp.expect(['%'])

# print result
print sp.match.group()

sp.sendline('exit')
sp.expect([pexpect.EOF])
