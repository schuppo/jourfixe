#!python
def sudo(command, password=None, prompt="Enter password "):

import pexpect

if not password:
import getpass
password = getpass.getpass(prompt)

command = "sudo " + command
child = pexpect.spawn(command)
child.expect(['ssword', pexpect.EOF])
child.sendline(password)
child.expect(pexpect.EOF)
# is this necessary?
child.close()
