#!/usr/bin/python
import socket

#utiliser la fonction socket pour scanner les ports réseaux
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*]Taper votre ip: ")


def portscanner(port):
    if sock.connect_ex((host, port)):
        print("le port %d est fermer" % (port))
    else:
        print("port est %d ouvert" % (port))

for port in range(1, 1000):
    portscanner(port)

