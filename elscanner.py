#!/usr/bin/python

from socket import *
import optparse
from threading import *

def retVersion(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket()
        s.connect((ip, port))
        version = s.recv(1024)
        return version
    except:
        return None    

def connScan(tgtHost, tgtPort):
    try:
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect((tgtHost, tgtPort))
        ver = retVersion(gethostbyaddr(tgtHost), tgtPort)
        print('[+] /tcp open :' , tgtPort, ':', ver)
    except:
        print('[-] /tcp closed :', tgtPort)
    finally:
        sock.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print('Unknown Host ', tgtHost)   
    try:
        tgtName = gethostbyaddr(tgtIP)
        print('[+] Scan Results for: ', tgtName[0],'(' ,tgtIP, ')')
    except:
        print('[+] Scan Results for: ', tgtIP, ':')
    setdefaulttimeout(2)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='specify target ports separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)   

if __name__ == '__main__':
    main()    