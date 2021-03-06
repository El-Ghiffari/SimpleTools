#!/usr/bin/python

import pexpect

PROMPT = ['#', '>>> ', '> ', '\$ ']

def send_command(offspring, command):
    offspring.sendline(command)
    offspring.expect(PROMPT)
    print(offspring.before)

def connect(user, host, password):
    ssh_newkey = 'Are you sure want to continue connecting'
    connStr = 'ssh ' + user + '0' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error Connecting')
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT,'[P|p]assword: '])
        if ret == 0:
            print('[-] Error Connecting')
            return
    child.sendline(password)
    child.expect(PROMPT)
    return child                

def main():
    host = input('[+] Your Host :')
    user = input('[+] Your Username :')
    password = input('[-] Your Password :')
    offspring = connect(user, host, password)
    send_command(offspring, 'cat /etc/shadow | grep root;ps')

main()      
