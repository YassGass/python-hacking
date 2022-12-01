#!/usr/bin/python

from socket import *
import optparse
from threading import *

def connScan(tgHost, tgtPorts):
    try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((tgtPorts, tgHost))
            print('[+] %/tcp Open' % tgtPorts)
    except:
            print('[-] %d/tcp Closed' % tgtPorts)
    finally:
            sock.close()

def portScan(tgHosts,tgPorts):
    try:
            tgIP = gethostbyname(tgHosts)
    
    except:
            print('Unknown host %s' %tgHosts)
    
    try:
            tgName= gethostbyaddr(tgIP)
            print('[*]Scan results for: ' + tgName[0])

    except:
            print('[*]Scan results for: ' + tgIP)
    
    for tgtPort in tgPorts:
        t = Thread(target=connScan, args=(tgHosts, int(tgtPort)))
        t.start()

    
def main():
    parser = optparse.OptionParser('Usage of program: ' + '-H <target host> -P <target port>')
    parser.add_option('-H', dest='tgHost', type='string', help='specify target host')
    parser.add_option('-P', dest='tgPort', type='string', help='specify target port')
    (options,args) =parser.parse_args()
    tgHosts = options.tgHost
    tgPorts = str(options.tgPort).split(',')
    if (tgHosts == None) | (tgPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgHosts.tgPorts)

if __name__== '__main__':
    main()