#!/usr/bin/python
import socket

#utiliser la fonction socket pour scanner les ports réseaux
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*]Taper votre ip: ")

port = int(input("[*]Taper votre port: "))

def portscanner(port):
    if sock.connect_ex((host, port)):
        print("le port est fermer")
    else:
        print("port est ouvert")

portscanner(port)