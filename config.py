#!/usr/bin/env python
from xml.dom import minidom
from os import environ

print('Configurando...')

CLIENTES = environ['IC_CLIENTES']
SOURCES = environ['IC_SOURCES']
QUEUESIZE = environ['IC_QUEUESIZE']
CLITIMEOUT = environ['IC_CLITIMEOUT']
HEADERTIMEOUT = environ['IC_HEADERTIMEOUT']
SOURCETIMEOUT = environ['IC_SOURCETIMEOUT']
BURSTCONNECT = environ['IC_BURSTCONNECT']
BURSTSIZE = environ['IC_BURSTSIZE']
SOURCEPASSWORD = environ['IC_SOURCEPASSWORD']
ADMIN = environ['IC_ADMIN']
PASSWORDADMIN = environ['IC_PASSWORDADMIN']
IP = environ['IC_IP']
PORT = environ['IC_PORT']

arquivo = open('/etc/icecast2/icecast.xml', 'r')

texto = arquivo.read()

arquivo.close()

arquivo = open('/etc/icecast2/icecast.xml', 'w')

texto = texto.replace("ic-clients", CLIENTES)
texto = texto.replace("ic-sources", SOURCES)
texto = texto.replace("ic-queuesize", QUEUESIZE)
texto = texto.replace("ic-clitimeout", CLITIMEOUT)
texto = texto.replace("ic-headertimeout", HEADERTIMEOUT)
texto = texto.replace("ic-sourcetimeout", SOURCETIMEOUT)
texto = texto.replace("ic-burstconnect", BURSTCONNECT)
texto = texto.replace("ic-burstsize", BURSTSIZE)
texto = texto.replace("ic-sourcepassword", SOURCEPASSWORD)
texto = texto.replace("ic-admin", ADMIN)
texto = texto.replace("ic-passwordadmin", PASSWORDADMIN)
texto = texto.replace("ic-localhost", IP)
texto = texto.replace("ic-port", PORT)

arquivo.write(texto)

arquivo.close()