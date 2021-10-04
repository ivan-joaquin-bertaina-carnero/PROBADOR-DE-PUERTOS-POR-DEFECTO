#-----------------------------------------------------------------------------------------------
# -*- coding: latin-1 -*-
#-----------------------------------------------------------------------------------------------

import threading    
import socket       
import os           

#-----------------------------------------------------------------------------------------------

tiempo_de_espera = 0.65
puertos_reporte = ''

puertos = [1,
5,
7,
9,
11,
13,
17,
18,
19,
20,
21,
22,
23,
25,
37,
39,
42,
43,
49,
50,
53,
63,
66,
67,
68,
69,
70,
79,
80,
88,
95,
101,
107,
109,
110,
111,
113,
115,
117,
119,
123,
135,
137,
138,
139,
143,
161,
162,
174,
177,
178,
179,
194,
199,
201,
202,
204,
206,
209,
210,
213,
220,
245,
347,
363,
369,
370,
372,
389,
427,
434,
435,
443,
444,
445,
465,
500,
512,
513,
514,
515,
520,
521,
587,
591,
631,
666,
690,
993,
995,
1080,
1194,
1337,
1352,
1433,
1434,
1494,
1512,
1521,
1701,
1720,
1723,
1761,
1812,
1813,
1883,
18633,
1935,
2049,
2082,
2083,
2086,
2427,
3030,
3074,
3128,
3306,
3389,
3396,
3690,
3799,
4200,
4443,
4662,
4672,
4899,
5000,
5001,
5060,
5190,
5222,
5223,
5269,
5432,
5517,
5631,
5632,
5400,
5500,
5600,
5700,
5800,
5900,
6000,
6112,
6129,
6346,
6347,
6348,
6349,
6350,
6355,
6667,
6881,
6969,
7100,
8000,
8080,
8118,
8443,
9009,
9898,
10000,
19226,
12345,
25565,
31337,
41121,
42000,
42001,
42002,
42003,
42004,
45003]

#-----------------------------------------------------------------------------------------------

detalle_puertos = ['1 # tcpmux (Multiplexor TCP).',
'5 # rje    (Entrada de trabajo remota).',
'7 # echo (Protocolo Echo).',
'9 # discard    (Protocolo Discard).',
'11 # systat (Listar puertos).',
'13 # daytime (Protocolo Daytime).',
'17 # qotd (Quote of the Day, envía la cita del día).',
'18 # msp (Protocolo de envío de mensajes).',
'19 # chargen (Generador de caracteres).',
'20 # ftpS-data (FTPS File Transfer Protocol).',
'21 # ftp-control (FTP File Transfer Protocol).',
'22 # ssh (SSH, scp, SFTP).',
'23 # telnet (Telnet, INSEGURO!!!).',
'25 # smtp (SMTP Simple Mail Transfer Protocol).',
'37 # time (Time Protocol. Sincroniza hora y fecha).',
'39 # rlp (Protocolo de ubicación de recursos).',
'42 # nameserver    (Servicio de nombres de Internet).',
'43 # nickname (Servicio de directorio WHOIS).',
'49 # tacacs (Terminal Access Controller Access Control System).',
'50 # re-mail-ck (Protocolo de verificación de correo remoto).',
'53 # DNS (Domain Name System).',
'63 # whois++ (Servicios extendidos de WHOIS).',
'66 # Oracle SQLNet.',
'67 # bootps (BOOTP BootStrap Protocol (Servidor)).',
'68 # bootpc (BOOTP BootStrap Protocol (Cliente)).',
'69 # tftp (TFTP Trivial File Transfer Protocol).',
'70 # gopher (Gopher).',
'79 # finger (Finger).',
'80 # http (HyperText Transfer Protocol (www)).',
'88 # kerberos (Kerberos Agente de autenticación).',
'95 # supdup (Extensión del protocolo Telnet).',
'101 # hostname (Servicios de nombres de host en máquinas SRI-NIC).',
'107 # rtelnet (Telnet remoto).',
'109 # pop2 (POP2 Post Office Protocol (E-mail)).',
'110 # pop3 (POP3 Post Office Protocol (E-mail)).',
'111 # sunrpc (sunrpc).',
'113 # auth (ident (auth) antiguo sistema de identificación).',
'115 # SFTP (Simple FTP).',
'117 # uupc-path (Rutas de Unix-to-Unix Copy Protocol (UUCP)).',
'119 # nntp (NNTP usado en los grupos de noticias de usenet).',
'123 # ntp (NTP Protocolo de sincronización de tiempo).',
'135 # epmap / SMB.',
'137 # netbios-ns (NetBIOS Servicio de nombres).',
'138 # netbios-dgm (NetBIOS Servicio de envío de datagramas).',
'139 # netbios-ssn (NetBIOS Servicio de sesiones).',
'143 # imap (IMAP4 Internet Message Access Protocol (E-mail)).',
'161 # snmp (SNMP Simple Network Management Protocol).',
'162 # snmptrap (SNMP-trap).',
'174 # mailq (Cola de transporte de correos electrónicon MAILQ).',
'177 # xdmcp (XDMCP Protocolo de gestión de displays en X11).',
'178 # nextstep (Servidor de ventanas NeXTStep).',
'179 # bgp (Border Gateway Protocol).',
'194 # irc (Internet Relay Chat).',
'199 # smux (SNMP UNIX Multiplexer).',
'201 # at-rtmp (Enrutamiento AppleTalk).',
'202 # at-nbp (Enlace de nembres AppleTalk).',
'204 # at-echo (Echo AppleTalk).',
'206 # at-zis (Zona de información AppleTalk).',
'209 # qmtp (Protocolo de transferencia rápida de correo (QMTP)).',
'210 # z39.50 (Base de datos NISO Z39.50).',
'213 # ipx (Protocolo de intercambio de paquetes entre redes).',
'220 # imap3 (IMAP versión 3).',
'245 # link (Servicio LINK / 3-DNS iQuery).',
'347 # fatserv (Admin. cintas y archivos FATMEN).',
'363 # rsvp_tunnel (Túnel RSVP).',
'369 # rpc2portmap (Portmapper del sistema de archivos Coda).',
'370 # codaauth2 (Autenticación del sistema de archivos Coda).',
'372 # ulistproc (UNIX LISTSERV).',
'389 # ldap (LDAP Protocolo de acceso ligero a Directorios).',
'427 # svrloc (Protocolo de ubicación de servicios (SLP)).',
'434 # mobileip-agent (Agente móvil del Protocolo Internet).',
'435 # mobilip-mn (Gestor móvil del Protocolo Internet).',
'443 # https (HTTPS/SSL Transferencia de datos segura).',
'444 # snpp (Protocolo simple de Network Pagging).',
'445 # microsoft-ds (Active Directory, gusano Sasser, Agobot).',
'465 # smtps (SMTP Sobre SSL).',
'500 # IPSec ISAKMP (Autoridad de Seguridad Local).',
'512 # exec.',
'513 # Rlogin.',
'514 # syslog (usado para logs del sistema).',
'515 # usado para la impresión en windows.',
'520 # rip (RIP Routing Information Protocol).',
'521 # ripng (RIP Routing Information Protocol IPv6).',
'587 # smtp (SMTP Sobre TLS).',
'591 # FileMaker 6.0 (alternativa para HTTP, ver puerto 80).',
'631 # CUPS (sistema de impresión de Unix).',
'666 # identificación de Doom para jugar sobre TCP.',
'690 # VATP (Velneo Application Transfer Protocol).',
'993 # imaps (IMAP4 sobre SSL (E-mail)).',
'995 # (POP3 sobre SSL (E-mail)).',
'1080 # SOCKS Proxy.',
'1194 # OpenVPN (Puerto por defecto en NAS Synology y QNAP).',
'1337 # suele usarse en máquinas comprometidas o infectadas.',
'1352 # IBM Lotus Notes/Domino RCP.',
'1433 # Microsoft-SQL-Server.',
'1434 # Microsoft-SQL-Monitor.',
'1494 # Citrix MetaFrame Cliente ICA.',
'1512 # WINS (Windows Internet Naming Service).',
'1521 # Oracle (puerto de escucha por defecto).',
'1701 # Enrutamiento y Acceso Remoto para VPN con L2TP.',
'1720 # H.323 (Video y Audio sobre IP, muy parecido a SIP).',
'1723 # Enrutamiento y Acceso Remoto para VPN con PPTP.',
'1761 # Novell Zenworks Remote Control utility.',
'1812 # RADIUS authentication protocol, radius.',
'1813 # RADIUS accounting protocol, radius-acct.',
'1883 # MQTT protocol.',
'18633 # MSN Messenger.',
'1935 # FMS Flash Media Server.',
'2049 # NFS Archivos del sistema de red.',
'2082 # cPanel puerto por defecto.',
'2083 # CPanel puerto por defecto sobre SSL.',
'2086 # Web Host Manager puerto por defecto.',
'2427 # Cisco MGCP.',
'3030 # NetPanzer.',
'3074 # Xbox Live.',
'3128 # HTTP usado por web caches (por defecto en Squid cache). / NDL-AAS.',
'3306 # MySQL (sistema de gestión de bases de datos).',
'3389 # RDP (Remote Desktop Protocol) / Terminal Server.',
'3396 # Novell agente de impresión NDPS.',
'3690 # Subversion (sistema de control de versiones).',
'3799 # RADIUS CoA -change of authorization.',
'4200 # Angular (puerto por defecto).',
'4443 # AOL Instant Messenger (sistema de mensajería).',
'4662 # eMule TCP.',
'4672 # eMule UDP.',
'4899 # RAdmin (Remote Administrator).',
'5000 # Universal plug-and-play.',
'5001 # Agente v6 Datadog4.',
'5060 # Session Initiation Protocol (SIP) - UDP.',
'5190 # AOL y AOL Instant Messenger.',
'5222 # Jabber/XMPP (conexión de cliente).',
'5223 # Jabber/XMPP (puerto por defecto para conexiones de cliente SSL).',
'5269 # Jabber/XMPP (conexión de servidor).',
'5432 # PostgreSQL (sistema de gestión de bases de datos).',
'5517 # Setiqueue (proyecto SETI@Home).',
'5631 # PC-Anywhere protocolo de escritorio remoto.',
'5632 # PC-Anywhere protocolo de escritorio remoto.',
'5400 # VNC protocolo de escritorio remoto (usado sobre HTTP).',
'5500 # VNC protocolo de escritorio remoto (usado sobre HTTP).',
'5600 # VNC protocolo de escritorio remoto (usado sobre HTTP).',
'5700 # VNC protocolo de escritorio remoto (usado sobre HTTP).',
'5800 # VNC protocolo de escritorio remoto (usado sobre HTTP).',
'5900 # VNC protocolo de escritorio remoto (conexión normal).',
'6000 # X11 usado para X-windows.',
'6112 # Blizzard.',
'6129 # Dameware (Software conexión remota).',
'6346 # Gnutella compartición de ficheros (Limewire, etc.).',
'6347 # Gnutella UDP.',
'6348 # Gnutella UDP.',
'6349 # Gnutella UDP.',
'6350 # Gnutella UDP.',
'6355 # Gnutella UDP.',
'6667 # IRC IRCU (Internet Relay Chat).',
'6881 # BitTorrent (puerto por defecto).',
'6969 # BitTorrent (puerto de tracker).',
'7100 # Servidor de Fuentes X11.',
'8000 # iRDMI / streaming ShoutCast / SimpleHTTPServer (Python). ',
'8080 # HTTP HTTP-ALT. (puerto Tomcat por defecto).',
'8118 # privoxy.',
'8443 # ssl/https-alt.',
'9009 # Pichat (peer-to-peer chat server).',
'9898 # Gusano Dabber (troyano/virus).',
'10000 # Webmin (Administración remota web).',
'19226 # Panda Security (Puerto de comunicaciones de Panda Agent).',
'12345 # NetBus en:NetBus (troyano/virus).',
'25565 # Minecraft (servidores del juego).',
'31337 # Back Orifice, (administración remota, por lo general troyanos).',
'41121 # tentacle (Protocolo de transferencia utilizado por Pandora FMS).',
'42000 # Percona Monitoring Management (recoger métricas generales).',
'42001 # Percona Monitoring Management (recabar datos de desempeño).',
'42002 # Percona Monitoring Management (recabar métricas de MySQL).',
'42003 # Percona Monitoring Management (recabar métricas de MongoDB).',
'42004 # Percona Monitoring Management (recabar métricas de ProxySQL).',
'45003 # Calivent (herramienta de administración remota SSH).']

#-----------------------------------------------------------------------------------------------

def generar_reporte(nombre, modo):
  try:
    reporte = open(nombre, modo)
    return reporte
  except OSError as err:
    print("Error: {0}".format(err))
  return

#-----------------------------------------------------------------------------------------------

def limpiarPantalla():
    command = 'clear'
    if os.name in ('nt', 'dos'): 
        command = 'cls'           
    os.system(command)
    print(chr(27)+"[1;37m")

#-----------------------------------------------------------------------------------------------

def probar(objetivo,puerto,n):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(tiempo_de_espera)# 
    nombre_de_archivo = objetivo + '.txt'
    archivo = generar_reporte(nombre_de_archivo, 'a')

    try:
        con = s.connect((objetivo,puerto))
        print '#', puerto, '#',detalle_puertos[n]
        print "-------------------------------------------------------------------------------"
        puertos_reporte = str(puerto) + '\n'
        #print(puertos_reporte)
        archivo.write(puertos_reporte)
        con.close()
    except: 
        #print '#', detalle_puertos[n]
        #print "-------------------------------------------------------------------------------"
        pass
    archivo.close()
#-----------------------------------------------------------------------------------------------

def tarea_escanear(objetivo):

    x = range (0,len(puertos))
    for n in x:
        t = threading.Thread(probar(objetivo,puertos[n],n)) 
        t.start() 
    #print "> pasé por: tarea_escanear"

    
    
 #-----------------------------------------------------------------------------------------------
   
def pantalla_principal():
    limpiarPantalla()
    print(chr(27)+"[1;36m")
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # #    PROBADOR DE PUERTOS POR DEFECTO    # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print(chr(27)+"[1;37m")
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print(chr(27)+"[1;36m")
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # #    I.J.B. - ARGENTINA - 20/06/2021    # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print(chr(27)+"[0;37m")
    #intensidad = raw_input('\t# INTENSIDAD ( 1.Baja | 2.Media | 3.Alta ): ')
    print '\n\t\t# PUERTOS A PROBAR: ',len(puertos), 'puertos (', len(puertos)*1000*tiempo_de_espera, 'ms).\n'
    objetivo = raw_input('\t\t# OBJETIVO: ')
    limpiarPantalla()

    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # #    PROBADOR DE PUERTOS POR DEFECTO    # # # # # # # # # #"
    print " # # # # # # # # # #                                       # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"
    print " # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #"

    print(chr(27)+"[1;36m")
    print '# OBJETIVO:', objetivo
    print(chr(27)+"[0;37m")
    print "-------------------------------------------------------------------------------"
    nombre_de_archivo = objetivo + '.txt'
    archivo = generar_reporte(nombre_de_archivo, 'w')
    archivo.close()
    tarea_escanear(objetivo,)
    
#-----------------------------------------------------------------------------------------------

pantalla_principal()
print("\n")
