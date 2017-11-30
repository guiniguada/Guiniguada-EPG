#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
#Objetivo: Descargar EPG MOVISTAR+
#Version: 1.0  

#Funcion para obtener la ruta/path
def pathRuta():
    
    #Obtenemos la ruta donde se esta ejecutando el script
    pathname = os.path.dirname(sys.argv[0])    
    ruta = str(os.path.abspath(pathname))  
      
    return ruta
############################################################      
#Funcion para registrar logs y mensajes
def ficheroLog(ruta,mensaje):
            
    filelog = open(ruta + '/GUINIGUADA-EPG_Install.log', 'a+')
    filelog.write(mensaje)
    filelog.write('\n')
    filelog.close()
    
############################################################
def mensajelog(mensaje):

    ficheroLog(pathRuta(),mensaje)   
    
############################################################
def menucabecera():
   
    print 
    mensaje = "\t#############################################################################"
    print mensaje
    print
    if contmenucabecera == 0: mensajelog(mensaje)
       
    mensaje = "\t  ############    INSTALACION -- G U I N I G U A D A -- EPG    ############"
    print mensaje
    if contmenucabecera == 0: mensajelog(mensaje)
    print
    
    mensaje = "\t\t    -------------     %s --  %s  --------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S"))
    print mensaje
    if contmenucabecera == 0: mensajelog(mensaje)
    print

############################################################
def menudatos():
    
    mensaje = "\t\tSISTEMA -- " + upper(so) + " -- " + sistemaname + " -- " +  SYNOLOGY_VERSION
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = "\t\tPYTHON v. -- " + upper(pyt)
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)

    mensaje = "\t\tRUTA INSTALACION -- " + GUINIGUADA_DIR
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
    print

    mensaje = "\t\tTVHEADEND_SERVICE -- " + TVHEADEND_SERVICE
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tSERVICES_MANAGEMENT -- " + SERVICES_MANAGEMENT
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_USER -- " + TVHEADEND_USER
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_USER_ID -- " + TVHEADEND_USER_ID
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
            
    mensaje = "\t\tTVHEADEND_GROUP -- " + TVHEADEND_GROUP
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_GROUP_ID -- " + TVHEADEND_GROUP_ID
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_PERMISSIONS -- " + TVHEADEND_PERMISSIONS
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = "\t\tTVHEADEND_DIR -- " + TVHEADEND_DIR
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_CONFIG_DIR -- " + TVHEADEND_CONFIG_DIR
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
     
    mensaje = "\t\tTVHEADEND_GRABBER_DIR -- " + TVHEADEND_GRABBER_DIR
    print mensaje
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = TVHEADEND_CHANNEL_USER
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_CHANNEL_GROUP
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_CHANNEL_PERMISSIONS
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = TVHEADEND_INPUT_USER
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_INPUT_GROUP
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_INPUT_PERMISSIONS
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = TVHEADEND_PICONS_USER
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_PICONS_GROUP
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_PICONS_PERMISSIONS
    if contmenudatos == 0: mensajelog(mensaje)
    
    mensaje = TVHEADEND_EPGGRAB_USER
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_EPGGRAB_GROUP
    if contmenudatos == 0: mensajelog(mensaje)
    mensaje = TVHEADEND_EPGGRAB_PERMISSIONS
    if contmenudatos == 0: mensajelog(mensaje)
        

############################################################
#Menu para activar el grabber    
def menucanales():
         
    print ("\t\t  ***** DESEA UD. INSTALAR LISTA DE CANALES ******")
    print
    barramenu(0)
    
    
############################################################
def barramenu(contbarramenu):
    
    mensaje = "\t#############################################################################"
    print mensaje 
    if contbarramenu == 0: mensajelog(mensaje)
    print
############################################################
#Menu para activar el grabber    
def IniciarTvh():
    #Segun el sistema, iniciamos el servicio, hacemos backup de epggrab/config e insertamos el grabber segun sistema
    if sistema == 1:
        
        dir1 = "/var/packages/"
        dir2 = commands.getoutput("ls /var/packages/ | grep tvheadend")
        dir3 = "/scripts/start-stop-status "
    
        #if  SERVICES_MANAGEMENT == "OLD":
             
        dir4 = "start"
        TVHEADEND_SERVICE_STOP_START = dir1 + dir2 + dir3 + dir4
        
        iniciado = commands.getoutput(TVHEADEND_SERVICE_STOP_START + " start")
        
        if "Tvheadend is running" in iniciado or "Starting Tvheadend" in iniciado: iniciado = 0
        
        os.system('clear')
        contmenucabecera = 1
        menucabecera()
        contmenudatos = 1
        menudatos()
       
        barramenu(1)
                         
        #else:
                     
            #iniciado = os.system('start -q ' + TVHEADEND_SERVICE)
            
    else:
        
        iniciado = os.system('systemctl start ' + TVHEADEND_SERVICE)
      
    if iniciado == 0:      
                            
        mensaje = "\t\t\t   ----- STATUS TVHEADEND START  -----"
        mensajelog(mensaje)
        print mensaje
        print     
        barramenu(0)
        
 
    else:
        
       mensaje = "\t\t\t     ----- ERROR AL INICIAR TVHEADEND   -----"
       mensajelog(mensaje)
       print mensaje
       print    
       barramenu(0)
        
    t.sleep(2)
         
    return iniciado

############################################################
#Menu para activar el grabber    
def PararTvh():
    
    #Segun el sistema, paramos el servicio, hacemos backup de epggrab/config e insertamos el grabber segun sistema
    if sistema == 1:
        
        dir1 = "/var/packages/"
        dir2 = commands.getoutput("ls /var/packages/ | grep tvheadend")
        dir3 = "/scripts/start-stop-status "
        
        #if  SERVICES_MANAGEMENT == "OLD":
                    
        dir4 = "stop"
        
        TVHEADEND_SERVICE_STOP_START = dir1 + dir2 + dir3 + dir4
        
        parado = commands.getoutput(TVHEADEND_SERVICE_STOP_START + " stop")
        
        if "Stopping Tvheadend" in parado: parado = 0
                
        os.system('clear')
        contmenucabecera = 1
        menucabecera()
        contmenudatos = 1
        menudatos()
       
        barramenu(1)
            
            
        #else:
            
            #parado = os.system('stop -q ' + TVHEADEND_SERVICE)  
            #print TVHEADEND_SERVICE
            
    else:
  
        parado = os.system('systemctl stop ' + TVHEADEND_SERVICE)
        
    if parado == 0:
      
        barramenu(0)
        mensaje = "\t\t\t   ----- STATUS TVHEADEND STOP  -----"
        mensajelog(mensaje)
        print mensaje
        print    
        barramenu(0)
        
    else:
        
        mensaje = "\t\t\t     ----- ERROR AL DETENER TVHEADEND   -----"
        mensajelog(mensaje)
        print mensaje
        print    
        barramenu(0)
        
    t.sleep(2)
    
    return parado
             
############################################################
def descargacanales():
    
    #mensaje = "\t\t       ----- DESCARGANDO LISTA DE CANALES -----"
    #mensaje = "\t\t       ----- COPIANDO LISTA DE CANALES -----"
#     mensajelog(mensaje)
#     print mensaje
#     print
#     barramenu(0)
    
    #REMOTE_LIST_VERSION = commands.getoutput("curl -fLs https://github.com/manuelrn/Tvheadend_Movistar-Spain/raw/master/version.txt | grep ^'LIST_VERSION' | cut -d'=' -f2")
        
   #Descargamos el archivo con los canales etc
    #commands.getoutput('wget -c -q https://github.com/manuelrn/Tvheadend_Movistar-Spain/raw/master/files/Configuracion_Tvheadend_' + REMOTE_LIST_VERSION + '.tar.xz && tar -Jxvf Configuracion_Tvheadend_' + REMOTE_LIST_VERSION +'.tar.xz')
    
    #filecanales = 'Configuracion_Tvheadend_' + REMOTE_LIST_VERSION + '.tar.xz'

    mensaje = "\t\t    --- COPIANDO LISTA DE CANALES EN TVHEADEND_DIR ---"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    t.sleep(2)
                           
    #Comprobamos si ya existen las carpetas 
    if isdir(pathRuta() + '/channel/'):
                                      
        commands.getoutput('chown -R ' + TVHEADEND_CHANNEL_USER + ':' + TVHEADEND_CHANNEL_GROUP + ' ' + pathRuta() + '/channel')        
        commands.getoutput('chmod -R ' + TVHEADEND_CHANNEL_PERMISSIONS +  ' ' + pathRuta() + '/channel')
        commands.getoutput('mv ' + pathRuta() + '/channel/ ' + TVHEADEND_DIR)
        
    mensaje = "\t\t    --- COPIANDO EPGGRAB EN TVHEADEND_DIR ---"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    t.sleep(2)
        
    if isdir(pathRuta() + '/epggrab/'):
                                      
        commands.getoutput('chown -R ' + TVHEADEND_EPGGRAB_USER + ':' + TVHEADEND_EPGGRAB_GROUP + ' ' + pathRuta() + '/epggrab')        
        commands.getoutput('chmod -R ' + TVHEADEND_EPGGRAB_PERMISSIONS +  ' ' + pathRuta() + '/epggrab')
        commands.getoutput('mv ' + pathRuta() + '/epggrab/xmltv ' + TVHEADEND_CONFIG_DIR + '/')
        
    mensaje = "\t\t    --- COPIANDO INPUT/DVB EN TVHEADEND_DIR ---"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    t.sleep(2)
        
    if isdir(pathRuta() + '/input/dvb'):
                                      
        commands.getoutput('chown -R ' + TVHEADEND_INPUT_GROUP + ':' + TVHEADEND_INPUT_GROUP + ' ' + pathRuta() + '/input')  
        commands.getoutput('chmod -R ' + TVHEADEND_INPUT_PERMISSIONS +  ' ' + pathRuta() + '/input')                            
        
        if isdir(TVHEADEND_DIR + '/input/dvb'):
            
            os.system("rm -R " + TVHEADEND_DIR + '/input/dvb')
            
        commands.getoutput('mv ' + pathRuta() + '/input/dvb '+ TVHEADEND_DIR + '/input/dvb')
        
    mensaje = "\t\t    --- COPIANDO PICON EN TVHEADEND_DIR ---"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    t.sleep(2)
        
    if isdir(pathRuta() + '/picon/'):
                                      
        commands.getoutput('chown -R ' + TVHEADEND_PICONS_USER + ':' + TVHEADEND_PICONS_GROUP + ' ' + pathRuta() + '/picon')        
        commands.getoutput('chmod -R ' + TVHEADEND_PICONS_PERMISSIONS +  ' ' + pathRuta() + '/picon')
        commands.getoutput('mv ' + pathRuta() + '/picon/ ' + TVHEADEND_DIR)
        
############################################################    
def opmenusnCANALES():
    
     #Usuario tiene que activar grabber para ello paramos e iniciamos tvheadend
    while True:

        # solicituamos una opción al usuario
        opcionMenu = raw_input("\t\t\t    Si(s) o No(n) Y LUEGO (intro) ")
        
        if opcionMenu == "s" or opcionMenu == "S":
            
            descargarcan = 1
            break
         
        elif opcionMenu == "n" or opcionMenu == "N":
                             
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            
            barramenu(1)
            mensaje =("\t\t -- TIENE UD QUE INSTALAR PREVIAMENTE UNA LISTA DE CANALES --")
            mensajelog(mensaje)
            print mensaje
            print
            
            barramenu(1)
            t.sleep(3)
            
            if parado == 0: IniciarTvh()
            exit(1)
        
        else: 
            
            print               
            raw_input("\t\t\t    -----   OPCION INCORRECTA  ----\n\t\t\t\t       PULSAR INTRO ")
            
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            
            mensaje = "\t\t       ----- NO TIENE UD. UNA LISTA DE CANALES  -----"
            
            print mensaje
            print
           
            barramenu(1)
            
    return descargarcan
                        
############################################################
def opmenusnCANALES2():
    
     #Usuario tiene que activar grabber para ello paramos e iniciamos tvheadend
    while True:
        
        print ("\t\t\t  ***** SELECCIONAR UNA OPCION ******")
        print
        print ("\t\t -- 1 --    MANTENER LISTA CANALES ACTUAL E INSTALAR GUINIGUADA--EPG")
        print
        print ("\t\t -- 2 --    INSTALAR LISTA DE CANALES Y GUINIGUADA--EPG")
        print
        print ("\t\t         **** Se realizará backup de la configuración actual. ****")
        print
        print ("\t\t -- s --           SALIR DE LA INSTALACION")
        print
        barramenu(1)

        # solicituamos una opción al usuario
        opcionMenu = raw_input("\t\t\t   '1'  o '2'  o 's'  Y LUEGO (intro) ")
        

        if opcionMenu == "1":
            
            descargarcan = 0
            
            break
         
        elif opcionMenu == "2":
            
            descargarcan = 1
           
            break
                  
        elif opcionMenu == "s": 
            
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            
            barramenu(1)
            
            borrararchdescarg()
            
            if parado == 0: IniciarTvh()
            exit(1)
            
        else:
            
            print               
            raw_input("\t\t\t    -----   OPCION INCORRECTA  ----\n\t\t\t\t       PULSAR INTRO ")
            
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            
            mensaje = "\t\t       ----- TIENE UD. UNA LISTA DE CANALES  -----"
            
            print mensaje
            print
           
            barramenu(1)
            
            
    return descargarcan

############################################################
def menufinal():
    
     #Usuario tiene que activar grabber para ello paramos e iniciamos tvheadend
    while True:
        
        print ("\t\t  ***** Tiene Ud. que activar el grabber en Tvheadend ******")
        print
        print ("\t\t1º.- Recargar en navegador pagina Tvheadend")
        print
        print ("\t\t2º.- Dirijase: Configuracion-Canal/EPG-Módulos para obtención de Guía")
        print
        print ("\t\t3º.- Seleccione grabber: Grabber ")
        print
        print ("\t\t4º.- Marque Enabled y Guardar")
        print
        
        barramenu()

        # solicituamos una opción al usuario
        opcionMenu = raw_input("\t\t   'c'  Y LUEGO (intro) PARA FINALIZAR INSTALACION ")

        if opcionMenu == "c":

            barramenu()
            break
                 
        else:
            
            print               
            raw_input("\t\t\t    -----   OPCION INCORRECTA  ----\n\t\t\t\t       PULSAR INTRO ")
            
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()

############################################################
def backup():
    
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t       ----- REALIZANDO BACKUP DE TVHEADEND_DIR -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    filebackup = 'Backup_Tvheadend_' + hoy.strftime("%d-%m-%Y-%H-%M-%S") + '.tar.xz '
    
    try:
        
        if sistema == 2:
        
            result = commands.getoutput('tar -cf ' + filebackup +  TVHEADEND_DIR)
            
        else:
            
            result = commands.getoutput('tar -cJf ' + filebackup +  TVHEADEND_DIR)
        
    except tarfile.TarError, e:
        
        barramenu(1)
        mensaje = "\t\t\       ----- ERROR AL GENERAR BACKUP  -----",e
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1) 
        
    except tarfile.CompressionError, e:
        
        barramenu(1)
        mensaje = "\t\t\       ----- ERROR AL GENERAR BACKUP  -----",e
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1) 
        
    except tarfile.StreamError, e:
        
        barramenu(1)
        mensaje = "\t\t\       ----- ERROR AL GENERAR BACKUP  -----",e
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1) 
    
    except tarfile.ExtractError, e:
        
        barramenu(1)
        mensaje = "\t\t\       ----- ERROR AL GENERAR BACKUP  -----",e
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1)        
        
    except tarfile.HeaderError, e:
        
        barramenu(1)
        mensaje = "\t\t\       ----- ERROR AL GENERAR BACKUP  -----",e
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1)       
############################################################       
def  descargaconfig(sistema):
    
    if sistema == 1:
        
        fileconfig = pathRuta()  +"/"+ "configsynology.txt"
        
        os.remove(pathRuta()  +"/"+ "config")
        
        os.rename(fileconfig, pathRuta()  +"/"+ "config" )

        fileconfig = pathRuta()  +"/"+ "config"
         
    else:
        
        filesynology = pathRuta()  +"/"+ "configsynology.txt"
        
        if filesynology: os.remove(filesynology)
        
        fileconfig = pathRuta()  +"/"+ "config"
    
#     if isfile(fileconfig):
#         
#         commands.getoutput('rm ' + fileconfig)
#                 
        os.system('clear')
        contmenucabecera = 1
        menucabecera()
        contmenudatos = 1
        menudatos()
        barramenu(1)
#         mensaje = "\t\t       -----     DESCARGANDO CONFIG    -----"
#         mensajelog(mensaje)
#         print mensaje
#         print
#         barramenu(0)
#     
#     if sistema == 1:
#         
#        commands.getoutput("wget -c -O " + fileconfig +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/configsynology.txt")
#         
#     else:
#         
#         commands.getoutput("wget -c -O " + fileconfig +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/config")
#             
#     t.sleep(2)
    
    if not isfile(fileconfig):
        
        barramenu(1)
        mensaje = "\t\t       ----- ERROR EN LA DESCARGA DE CONFIG -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1)
        
    else:
       
        #Buscamos el archivo config para sustituirlo
        fileb = TVHEADEND_CONFIG_DIR + "/config"
               
         #Si no existe config
        if isfile(fileb):
                             
            #Si existe hacemos un backup
            if not isfile(fileb +".bak"):

                os.rename(fileb, fileb +".bak")

                mensaje = "\t\t       ----- REALIZANDO BACKUP CONFIG -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)
                                   
            else:
                  
                os.remove(fileb +".bak")
                
                mensaje = "\t\t       ----- ELIMINANDO CONFIG BACKUP ANTERIOR -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)
                
                os.rename(fileb, fileb +".bak") 
                
                
                mensaje = "\t\t       ----- REALIZANDO BACKUP CONFIG -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)
                               
                commands.getoutput('chmod 0777 ' + TVHEADEND_CONFIG_DIR + "/config.bak")
                commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + TVHEADEND_CONFIG_DIR + "/config.bak")                                
                commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + TVHEADEND_CONFIG_DIR + "/config.bak")
                
                mensaje = "\t\t    ----- ASIGNANDO PROPIETARIO Y PERMISOS A CONFIG BACKUP -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)   
                t.sleep(2)                    
        
        os.system('clear')
        contmenucabecera = 1
        menucabecera()
        contmenudatos = 1
        menudatos()
                                         
        move(fileconfig, TVHEADEND_CONFIG_DIR)  
        
        barramenu(1)
        mensaje = "\t\t       ----- COPIANDO CONFIG EN TVHEADEND_CONFIG_DIR -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0) 
        
#         os.chown(TVHEADEND_CONFIG_DIR + "/config",int(TVHEADEND_USER_ID),0)        
#         os.chmod(TVHEADEND_CONFIG_DIR + "/config",0777) 
        
        commands.getoutput('chmod 0777 ' + fileb)
        commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + fileb)                                
        commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + fileb)
        
        mensaje = "\t\t    ----- ASIGNANDO PROPIETARIO Y PERMISOS A CONFIG  -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)   
        t.sleep(3)
                 
    
############################################################                    
def descargagrabber():    
    
    filetv_grab_file = pathRuta()  +"/"+ "tv_grab_movistar-guiniguada"
    
#     if isfile(filetv_grab_file):
#         
#         commands.getoutput('rm ' + filetv_grab_file)
#         
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
#     mensaje = "\t\t       -----     DESCARGANDO tv_grab_movistar-guiniguada    -----"
#     mensajelog(mensaje)
#     print mensaje
#     print
#     barramenu(0)
#             
#     commands.getoutput("wget -c -O " + filetv_grab_file +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/tv_grab_movistar-guiniguada")
#             
#     t.sleep(2)
    
    if not isfile(filetv_grab_file):
        
        barramenu(1)
        mensaje = "\t\t       ----- ERROR EN LA DESCARGA DE tv_grab_movistar-guiniguada -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1)
        
    else:
        
        filegrabopen = open(pathRuta() + '/tv_grab_movistar-guiniguada', 'r')
        filecopia = open(pathRuta() + '/tv_grab_movistar-guiniguada_copia', 'w')
    
        numfilegrabopen = filegrabopen.readlines()
        
        filegrabopen.close() 
        
        cont1 = 1
        
        for nfilegrabopen in numfilegrabopen:
                                                       
            if cont1  <= len(numfilegrabopen) - 1:
                                                                
                if cont1 == 3:
                    
                    contenido = nfilegrabopen
                    
                    contenido = contenido.replace('""','').replace('\n','')
                    
                    contenido = contenido + '"' + pathRuta() + '/guiatv.xml"'+ '\n'
                    
                    filecopia.write(contenido)
                    
                elif cont1 == 14:
                    
                    contenido = "    python "
                                        
                    contenido = contenido + '"' + pathRuta() + '/guiaTVXml.pyc"'+ '\n'
                    
                    filecopia.write(contenido)
                                                    
                else:
                    
                    filecopia.write(nfilegrabopen)
        
                cont1 += 1
            
        filecopia.close()
        
        os.remove(pathRuta() + '/tv_grab_movistar-guiniguada')
                         
        os.rename(pathRuta() + '/tv_grab_movistar-guiniguada_copia', pathRuta() + '/tv_grab_movistar-guiniguada')    
        
        tupm = pathRuta() + '/tv_grab_movistar-guiniguada'
                    
        filebb = TVHEADEND_GRABBER_DIR + '/tv_grab_movistar-guiniguada'                 
        
        if isfile(filebb):
            
            #Si existe hacemos un backup
            if not isfile(filebb +".bak"):

                os.rename(filebb, filebb +".bak")
                
            else:
                                            
                os.remove(filebb +".bak")
                os.rename(filebb, filebb +".bak")                            

        move(tupm, TVHEADEND_GRABBER_DIR)
        
        mensaje = "\t\t-- COPIANDO tv_grab_movistar-guiniguada EN TVHEADEND_GRABBER_DIR --"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0) 
                                                        
        commands.getoutput('chmod 0777 ' + filebb)
        commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + filebb)                                
        commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + filebb)
        
        mensaje = "\t\t--- ASIGNANDO PROPIETARIO Y PERMISOS A tv_grab_movistar-guiniguada --"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)   
        t.sleep(3)

############################################################ 
def piconconfig():
    
    barramenu(1)
    mensaje = "\t\t       ---- ASIGNANDO RUTA PICONS EN TVHEADEND_DIR -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    commands.getoutput('chmod 0777 ' + TVHEADEND_DIR + '/config')
    
    filepiconconfig = open(TVHEADEND_DIR + '/config', 'r')
        
    filecopia = open(TVHEADEND_DIR + '/config_copia', 'w')
    
    numfilepiconconfig = filepiconconfig.readlines()
        
    filepiconconfig.close() 
    
    cont1 = 1
    
    #chivapathpico = 0
    
    for nfilepiconconfig in numfilepiconconfig:
        
        if cont1  <= len(numfilepiconconfig) - 1:
            
            if  "prefer_picon" in nfilepiconconfig:
                                   
                nfilepiconconfig = nfilepiconconfig.replace('true','false')
                 
                filecopia.write(nfilepiconconfig)
                
            elif  "chiconpath" in nfilepiconconfig:
                
                rutapicon = '\t"chiconpath": "",\n'
                    
                filecopia.write(rutapicon)
                    
            
            elif  "chiconscheme" in nfilepiconconfig:
                                   
                nfilepiconconfig = nfilepiconconfig.replace('1','0').replace('2','0')
                
                filecopia.write(nfilepiconconfig)

            elif  "piconpath" in nfilepiconconfig:
                
                rutapicon = '\t"piconpath": "file://' + TVHEADEND_DIR + '/picon/",\n'
                                
                filecopia.write(rutapicon)
                                
            elif  "piconscheme" in nfilepiconconfig:
                                       
                nfilepiconconfig = nfilepiconconfig.replace('1','0').replace('2','0')              
                
                filecopia.write(nfilepiconconfig)
                         
            else:
                
                filecopia.write(nfilepiconconfig)
                #"piconpath": "file:///home/hts/.hts/tvheadend/picon/",

    filecopia.close()
    
    filepiconconfig = TVHEADEND_DIR + '/config'
    
    filecopia = TVHEADEND_DIR + '/config_copia'
    
    os.remove(filepiconconfig)
                     
    os.rename(filecopia, filepiconconfig)    
    
    commands.getoutput('chmod 0700 ' + filepiconconfig)
    commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + filepiconconfig)                                
    commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + filepiconconfig)
    
    mensaje = "\t\t    ---   ASIGNANDO PROPIETARIO Y PERMISOS A TVHEADEND_DIR/config   ---"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)   
    t.sleep(3)
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
            
############################################################  
def backupgrabbers():  
    
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t    -----     HACIENDO BACKUP DE GRABBER ANTERIORES    -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)             
    
    #Movemos a la competencia                    
    if not isdir(pathRuta() + '/back_grabbers'):
                
         os.mkdir(pathRuta() + '/back_grabbers')
     
     
    rutabkpgrab = pathRuta() + '/back_grabbers/'  
    
    #if not sistema == 2:
        
    files = os.listdir(TVHEADEND_GRABBER_DIR +'/')
    files.sort()
    for f in files:
        if 'tv_grab_' in f:
            src = TVHEADEND_GRABBER_DIR+'/'+f
            srcb = rutabkpgrab+f
            shutil.move(src,srcb)
            
    t.sleep(3) 
                    
############################################################
def borrarepgdbv2():
    
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t       -----     ELIMINANDO epgdb.v2    -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    #Eliminamos epgdb2 y los canales anteriomente realcionados
    fileepgdb2 = TVHEADEND_DIR + '/epgdb.v2'
        
    if isfile(fileepgdb2):
        
        os.remove(fileepgdb2)
        
    filepgdb2 = pathRuta() + '/epgdb.v2'
        
    if isfile(filepgdb2):
        
        move(filepgdb2, TVHEADEND_DIR)
        
        mensaje = "\t\t-- COPIANDO epgdb.v2 /home/hts/.hts/tvheadend/ --"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        
        filepgdb22 = TVHEADEND_DIR + '/epgdb.v2'
        
        commands.getoutput('chmod 0700 ' + filepgdb22)
        commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + filepgdb22)                                
        commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + filepgdb22)
        
        mensaje = "\t\t--- ASIGNANDO PROPIETARIO Y PERMISOS A epgdb.v2 --"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)   
        t.sleep(3)
        
    

############################################################
def borrarcanlanteriores():
    
    rutachannels = TVHEADEND_DIR + '/channel/'
    
    mensaje = ("\t\t    -----  ELIMINANDO %s  -----"%rutachannels)
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)

    if isdir(TVHEADEND_DIR + '/channel/'):
        
        os.system("rm -R " + rutachannels)
    
#         files = os.listdir(TVHEADEND_DIR + '/xmltv/channels/')
#     
#         if len(files) > 0:
#         
#             rutachannels = TVHEADEND_DIR + '/xmltv/channels/'
#             os.system("rm " + rutachannels + "*")
            
    t.sleep(2)
        
    mensaje = ("\t\t    -----  ELIMINANDO %s  -----"%rutachannels)
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)

    if isdir(TVHEADEND_CONFIG_DIR):
        
        os.system("rm -R " + TVHEADEND_CONFIG_DIR)
    
#         files = os.listdir(TVHEADEND_CONFIG_DIR + '/epggrab/xmltv/channels/')
#     
#         if len(files) > 0:
#         
#             rutachannels = TVHEADEND_CONFIG_DIR + '/epggrab/xmltv/channels/'
#             os.system("rm " + rutachannels + "*")
            
    t.sleep(2)
        
    rutachannels = TVHEADEND_DIR + '/input/dvb/'
    
    mensaje = ("\t\t    -----  ELIMINANDO %s  -----"%rutachannels)
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    if isdir(TVHEADEND_DIR + '/input/dvb/'):
        
        os.system("rm -R " + rutachannels)
        
    rutachannels = TVHEADEND_DIR + '/picon/'
    
    mensaje = ("\t\t    -----  ELIMINANDO %s  -----"%rutachannels)
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    if isdir(TVHEADEND_DIR + '/picon/'):
        
        os.system("rm -R " + rutachannels)
        
    t.sleep(2)
############################################################
def epgtrue():
    
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t       -----     ASIGNADO EPG AUTO A LOS CANALES    -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    #Asignamos epg true auto a todos los canales si existen
    dirchannelconfig = TVHEADEND_DIR  +'/channel/config'
        
    if isdir(dirchannelconfig):
        
        files = os.listdir(dirchannelconfig +'/')
        files.sort()
        
        for f in files:
            
            cont = 1
            contenido = ""
            
            filechannel = open(dirchannelconfig + '/' + f, 'r')
            numfilechannel = filechannel.readlines()
            filechannel.close()
            
            filechannel = open(dirchannelconfig + '/' + f, 'w')
                     
            for nl in numfilechannel:
               
                if cont == 6:
                    
                    contenido = contenido + nl.replace('epgauto": false,','epgauto": true,') 
                    
                else:
                    
                    contenido = contenido + nl                 
                    
                cont += 1
                
            filechannel.write(contenido)
            filechannel.close()
            
            
            
    t.sleep(2)
############################################################
def descargaguiepg():
    
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t       -----     DESCARGANDO FICHEROS GUINIGUADA EPG    -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    #Buscamos el archivo guiniguada.pyc 
    filedesc = pathRuta() + '/guiniguada.pyc'
                           
    if not isfile(filedesc):
    
        #Descargamos guiniguada.pyc                 
        mensaje = "\t\t           ----- DESCARGANDO guiniguada.pyc    -----"
        mensajelog(mensaje)
        print mensaje
        print       
                
        commands.getoutput("wget -c -O " + filedesc +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/guiniguada.pyc")
                
        if not isfile(filedesc):

           mensaje = "\t\t       ----- ERROR DESCARGANDO guiniguada.pyc    -----"
           mensajelog(mensaje)
           print mensaje
           print
           barramenu(0)
           exit(1)
        
    #Buscamos el archivo guiaTVXml.pyc
    filedesc = pathRuta()  + "/guiaTVXml.pyc"
                           
    if not isfile(filedesc):
        
        #Descargamos guiaTVXml.pyc                
        mensaje = "\t\t           ----- DESCARGANDO guiaTVXml.pyc    -----"
        mensajelog(mensaje)
        print mensaje
        print       
                   
        commands.getoutput("wget -c -O " + filedesc +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/guiaTVXml.pyc")
                   
        if not isfile(filedesc):

            mensaje = "\t\t       ----- ERROR DESCARGANDO guiaTVXml.pyc    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            exit(1)
         
    #Buscamos el archivo guiniguadamv.sqlite
    filedesc = pathRuta()  + "/guiniguadamv.sqlite"
                           
    if not isfile(filedesc):
           
        #Descargamos guiaTVXml.pyc                
        mensaje = "\t\t           ----- DESCARGANDO guiniguadamv.sqlite    -----"
        mensajelog(mensaje)
        print mensaje
        print
                          
        commands.getoutput("wget -c -O " + filedesc +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/guiniguadamv.sqlite")  
                
        if not isfile(filedesc):

           mensaje = "\t\t       ----- ERROR DESCARGANDO guiniguadamv.sqlite    -----"
           mensajelog(mensaje)
           print mensaje
           print
           barramenu(0)
           exit(1)
           
    #Buscamos el archivo guiatv.xml
    filedesc = pathRuta()  + "/guiatv.xml"
                           
    if not isfile(filedesc): 
              
        #Descargamos guiatv.xml
        #Descargamos guiaTVXml.pyc                
        mensaje = "\t\t           ----- DESCARGANDO guiatv.xml    -----"
        mensajelog(mensaje)
        print mensaje
        print
        
                           
        commands.getoutput("wget -c -O " + filedesc +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/guiatv.xml")                                               
                
        if not isfile(filedesc):

           mensaje = "\t\t       ----- ERROR DESCARGANDO guiatv.xml    -----"
           mensajelog(mensaje)
           print mensaje
           print
           barramenu(0)
           exit(1) 

    #Buscamos el archivo guiatv.xml
    filedesc = pathRuta()  + "/canalesmovistar.txt"
                           
    if not isfile(filedesc): 
              
        #Descargamos guiatv.xml
        #Descargamos guiaTVXml.pyc                
        mensaje = "\t\t           ----- DESCARGANDO canalesmovistar.txt    -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
                           
        commands.getoutput("wget -c -O " + filedesc +" https://github.com/guiniguada/Guiniguada-EPG/blob/master/Files/canalesmovistar.txt")                                               
                
        if not isfile(filedesc):

           mensaje = "\t\t       ----- ERROR DESCARGANDO canalesmovistar.txt    -----"
           mensajelog(mensaje)
           print mensaje
           print
           barramenu(0)
           exit(1) 
        
    #Asignamos permisos a todos los archivos guiniguada
    files = os.listdir(pathRuta() +'/')
    files.sort()
    for f in files:
        if 'gu' in f:
            filepermiso = pathRuta()+'/'+f

            commands.getoutput('chmod 0777 ' + filepermiso)
            commands.getoutput('chown ' + TVHEADEND_USER_ID + ' ' + filepermiso)                                
            commands.getoutput('chgrp ' + TVHEADEND_GROUP_ID + ' ' + filepermiso)
    
    
    t.sleep(2)
############################################################
def asigcrontab():
    
    #Si no existe asignamos tarea en crontab para descargar la epg 
    filecrontab = open("/etc/crontab",'r')
    numlinfile = filecrontab.readlines()
    filecrontab.close()
   
    cont1 = 1
    encontradocont = 0
            
    for nlinfile in numlinfile:
                             
        if cont1  <= len(numlinfile):
                
            busccontenido = "guiniguada"
           
            linea = nlinfile
                            
            if linea.find(busccontenido) >= 0:
                
                encontradocont = 1
                os.system('clear')
                contmenucabecera = 1
                menucabecera()
                contmenudatos = 1
                menudatos()
                barramenu(1)
                mensaje = "\t\t       ----- ENCONTRADA TAREA PROGRAMADA EPG GUINIGUADA    -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)
              
                break
               
            cont1 += 1
                       
    if encontradocont == 0:
        
        try:
        
            filecrontab = open("/etc/crontab",'a+')
                               
            filecrontab.write('00    7    *    *    *    root    python ' + pathRuta() + '/guiniguada.pyc\n')
            
            filecrontab.close()
                       
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- INSERTADA TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
        
        except:
            
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- ERROR AL INSERTAR TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            exit(1) 
    
    t.sleep(2)
    
############################################################
def asigcrontabLibreElec():
    
    #Si no existe asignamos tarea en crontab para descargar la epg 
    filecrontab = open("/storage/.cache/cron/crontabs/root",'r')
    numlinfile = filecrontab.readlines()
    filecrontab.close()
   
    cont1 = 1
    encontradocont = 0
    
    for nlinfile in numlinfile:
                             
        if cont1  <= len(numlinfile):
                
            busccontenido = "guiniguada"
           
            linea = nlinfile
                            
            if linea.find(busccontenido) >= 0:
                
                encontradocont = 1
                os.system('clear')
                contmenucabecera = 1
                menucabecera()
                contmenudatos = 1
                menudatos()
                barramenu(1)
                mensaje = "\t\t       ----- ENCONTRADA TAREA PROGRAMADA EPG GUINIGUADA    -----"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)
              
                break
               
            cont1 += 1
            
    if encontradocont == 0:
        
        try:
        
            filecrontab = open("/storage/.cache/cron/crontabs/root",'a+')
                               
            filecrontab.write('00    7    *    *    *   /usr/bin/python ' + pathRuta() + '/guiniguada.pyc\n')
            
            filecrontab.close()
            
            os.system("systemctl restart cron")
                       
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- INSERTADA TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
        
        except:
            
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- ERROR AL INSERTAR TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            exit(1) 
            
    else:
        
        try:
            
            os.system("touch /storage/.cache/cron/crontabs/root")
            os.system('chmod 0777 /storage/.cache/cron/crontabs/root')
            
            filecrontab = open("/storage/.cache/cron/crontabs/root",'a+')
            
            filecrontab.write('PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/storage\n')
            filecrontab.write('\n')
            filecrontab.write('00    7    *    *    *   /usr/bin/python ' + pathRuta() + '/guiniguada.pyc\n')
            
            filecrontab.close()
            
            os.system("systemctl restart cron")
                       
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- INSERTADA TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            
        except:
            
            os.system('clear')
            menucabecera()
            contmenudatos = 1
            menudatos()
            barramenu(1)
            mensaje = "\t\t       ----- ERROR AL INSERTAR TAREA PROGRAMADA EPG GUINIGUADA    -----"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            exit(1)   
    
    t.sleep(2)
    
    
############################################################
def borrararchdescarg():
    
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/input')
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/epggrab')
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/channel')
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/picon')
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/scripts_module')
    commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/service')
    commands.getoutput('rm  ' + GUINIGUADA_DIR + '/epgdb.v2')
    commands.getoutput('rm  ' + GUINIGUADA_DIR + '/tv_grab_movistar-guiniguada')
    commands.getoutput('rm  ' + GUINIGUADA_DIR + '/configsynology.txt')
    commands.getoutput('rm  ' + GUINIGUADA_DIR + '/config')

    
    
    if not sistema == 2:
        commands.getoutput('rm -R ' + GUINIGUADA_DIR + '/Guiniguada-EPG.tar.xz')

############################################################ 
def descargazip():

    fileconfig = pathRuta()  +"/"+ "Guiniguada-EPG.tar.xz"
    
    #if not sistema == 2:
        
    if isfile(fileconfig):
            
        commands.getoutput('rm ' + fileconfig)
                
    os.system('clear')
    contmenucabecera = 1
    menucabecera()
    contmenudatos = 1
    menudatos()
    barramenu(1)
    mensaje = "\t\t       -----     DESCARGANDO Guiniguada-EPG.tar.xz    -----"
    mensajelog(mensaje)
    print mensaje
    print
    barramenu(0)
    
    #if not sistema == 2:
        
    if isfile(pathRuta()  +"/"+ 'Guiniguada-EPG.tar.xz?dl=0.tmp'):
        
        commands.getoutput("rm -R " + pathRuta()  +"/"+ 'Guiniguada-EPG.tar.xz?dl=0.tmp')
        
    if isfile(pathRuta()  +"/"+ 'Guiniguada-EPG.tar.xz'):
        
        commands.getoutput("rm -R " + pathRuta()  +"/"+ 'Guiniguada-EPG.tar.xz')
        
    if not sistema == 2:
        
        commands.getoutput("wget -c -A -O Guiniguada-EPG.tar.xz https://github.com/guiniguada/Guiniguada-EPG/raw/master/Files/Guiniguada-EPG.tar.xz")
        
    else:
        
        commands.getoutput("wget -c -O Guiniguada-EPG.tar.xz https://github.com/guiniguada/Guiniguada-EPG/raw/master/Files/Guiniguada-EPG.tar.xz")

    file1 = pathRuta()  +"/"+ "Guiniguada-EPG.tar.xz?dl=0.tmp"
    file2 = pathRuta()  +"/"+ "Guiniguada-EPG.tar.xz"
    file3 = pathRuta()  +"/"+ "Guiniguada-EPG.tar.xz?dl=0"

    if not sistema == 2:
        
        if isfile(file1): 
            
            os.system("mv " + file1 + " " + file2)
            
        else:
            
            os.system("mv " + file3 + " " + file2)
    
    os.system('chmod 0777 *')

    commands.getoutput("tar -Jxvf Guiniguada-EPG.tar.xz")
    
    os.system('chmod 0777 *')

    if not isfile(fileconfig):
        
        barramenu(1)
        mensaje = "\t\t       ----- ERROR EN LA DESCARGA DE Guiniguada-EPG.tar.xz -----"
        mensajelog(mensaje)
        print mensaje
        print
        barramenu(0)
        exit(1)
    
    os.remove(pathRuta()  +"/"+ "Guiniguada-EPG.tar.xz")
        
#     elif sistema == 2:
#         
#         commands.getoutput("tar -Jxvf Guiniguada-EPG.tar.xz")
#         
#         os.system('chmod 0777 *')

############################################################ 
def pipinstall():
    
    #Comprobamos si esta instalado python
    os.system('pip -V >> pip.txt')
        
    if os.stat(pathRuta() + "/pip.txt").st_size == 0:
        
        menucabecera()
        contmenucabecera = 1
        
        print    
        mensaje = "\t\t\t\tPIP NO INSTALADO -- Se va a proceder a su instalación."
        mensajelog(mensaje)
        print mensaje
        print        
        
        if not isfile(pathRuta() +'/get-pip.py'):
            
            print
            mensaje = "\t\t\t\tDESCARGARGANDO -- get-pip.py ...."
            mensajelog(mensaje)
            print mensaje 
            print
        
            os.system("wget -c -q https://bootstrap.pypa.io/get-pip.py")
        
            if isfile(pathRuta() +'/get-pip.py'):
                
                print
                mensaje = "\t\t\t\tDESCARGA FINALIZADA -- get-pip.py"
                mensajelog(mensaje)
                print mensaje 
                print
                
            else:
                
                print
                mensaje = "\t\t\t\tDESCARGA ERRONEA -- get-pip.py"
                mensajelog(mensaje)
                print mensaje 
                print
                sys.exit(1)
                
        try:
        
            os.system("python get-pip.py")
            
            print
            mensaje = "          ------------------------------------------------------------------------------------------------------------"
            print mensaje
            print
            mensajelog(mensaje)
            
        except:
            
            print
            mensaje = "\t\t\t\tERROR EN INSTALACION DE PIP"
            mensajelog(mensaje)
            print mensaje
            barramenu()
            print
            mensajelog(mensaje)
            sys.exit(1)
            
        import pip

    else:
        import pip
       
        menucabecera()
        
    filepip = pathRuta() + '/pip.txt'
    commands.getoutput('rm ' + filepip)
    commands.getoutput('pip list >> pip.txt')

############################################################ 
def piplibinstall():

    piplist  = []
    
    filepip = pathRuta() + '/pip.txt'
    
    pipi = open(filepip, 'r')
    
    numpipi = pipi.readlines()
    
    pipi.close()
    
    for npi in numpipi:
        
        ln = npi.split(' ')
        rln = ln[0]
        piplist.append(rln)

    #for package in pip.get_installed_distributions():
     
        #print(package.location) # you can exclude packages that's in /usr/XXX
        #piplist.append(package.key)
    
    k = 0       
    
    while k in range(len(piplisti)):
        
        if not (piplisti[k]) in piplist:
            
            mensaje = "\t\tINSTALANDO -- " + piplisti[k]
            mensajelog(mensaje)
                        
            try:
                
                commands.getoutput("pip install " + piplisti[k])
                
                print mensaje
                mensaje = "\t\t-------------------------------------------------------------"
                print mensaje
                print
                mensajelog(mensaje)
                
            except:
                
                mensaje = "ERROR EN INSTALACION DE LIBRERIA" + piplisti[k]
                mensajelog(mensaje)
                print mensaje
                barramenu(0)
                print
                mensajelog(mensaje)
                sys.exit(1)
                        
        k = k + 1
        
############################################################         
def obtprogrpper():
    
    #Channel
    TVHEADEND_CHANNEL_USER  = commands.getoutput("stat -c %U " + TVHEADEND_DIR + '/channel')
    if TVHEADEND_CHANNEL_USER == "": TVHEADEND_CHANNEL_USER = TVHEADEND_USER
    
    TVHEADEND_CHANNEL_GROUP = commands.getoutput("stat -c %G " + TVHEADEND_DIR + '/channel')
    if TVHEADEND_CHANNEL_GROUP == "": TVHEADEND_CHANNEL_GROUP = TVHEADEND_GROUP
    
    TVHEADEND_CHANNEL_PERMISSIONS = commands.getoutput("stat -c %a " + TVHEADEND_DIR + '/channel')
    if TVHEADEND_CHANNEL_PERMISSIONS == "": TVHEADEND_CHANNEL_PERMISSIONS = TVHEADEND_PERMISSIONS
    
    
    #Input
    TVHEADEND_INPUT_USER  = commands.getoutput("stat -c %U " + TVHEADEND_DIR + '/input')
    if TVHEADEND_INPUT_USER == "": TVHEADEND_INPUT_USER = TVHEADEND_USER
    
    TVHEADEND_INPUT_GROUP = commands.getoutput("stat -c %G " + TVHEADEND_DIR + '/input')
    if TVHEADEND_INPUT_GROUP == "": TVHEADEND_INPUT_GROUP = TVHEADEND_GROUP
    
    TVHEADEND_INPUT_PERMISSIONS = commands.getoutput("stat -c %a " + TVHEADEND_DIR + '/input')
    if TVHEADEND_INPUT_PERMISSIONS == "": TVHEADEND_INPUT_PERMISSIONS = TVHEADEND_PERMISSIONS
    
    
    #Picon
    TVHEADEND_PICONS_USER  = commands.getoutput("stat -c %U " + TVHEADEND_DIR + '/picon')
    if TVHEADEND_PICONS_USER == "": TVHEADEND_PICONS_USER = TVHEADEND_USER
    
    TVHEADEND_PICONS_GROUP = commands.getoutput("stat -c %G " + TVHEADEND_DIR + '/picon')
    if TVHEADEND_PICONS_GROUP == "": TVHEADEND_PICONS_GROUP = TVHEADEND_GROUP
    
    TVHEADEND_PICONS_PERMISSIONS = commands.getoutput("stat -c %a " + TVHEADEND_DIR + '/picon')
    if TVHEADEND_PICONS_PERMISSIONS == "": TVHEADEND_PICONS_PERMISSIONS = TVHEADEND_PERMISSIONS
    
    #Epggrab
    TVHEADEND_EPGGRAB_USER  = commands.getoutput("stat -c %U " + TVHEADEND_DIR + '/epggrab')
    if TVHEADEND_EPGGRAB_USER == "": TVHEADEND_EPGGRAB_USER = TVHEADEND_USER
    
    TVHEADEND_EPGGRAB_GROUP = commands.getoutput("stat -c %G " + TVHEADEND_DIR + '/epggrab')
    if TVHEADEND_EPGGRAB_GROUP == "": TVHEADEND_EPGGRAB_GROUP = TVHEADEND_GROUP
    
    TVHEADEND_EPGGRAB_PERMISSIONS = commands.getoutput("stat -c %a " + TVHEADEND_DIR + '/epggrab')
    if TVHEADEND_EPGGRAB_PERMISSIONS == "": TVHEADEND_EPGGRAB_PERMISSIONS = TVHEADEND_PERMISSIONS

############################################################ 
 #Comprobamos que estan instaladas las librerias necesarias
try:
    
    sistema = 0
    sistemaname = ""
    iniciado = 0
    parado = 0
    contmenucabecera = 0
    contmenudatos = 0
    contbarramenu = 0
    descargarcan = 0
    mv = ""
    
    SYNOLOGY_VERSION = ""
        
    piplisti = ["pip","Babel","beautifulsoup4", "BeautifulSoup", "bs4","lxml","pytz","requests","tzlocal","html5lib"]
    piplist = []
        
    #Importamos las librerias         
    import os, sys, platform, errno  
    import commands
    import time as t
    import re
    import grp
    import pwd   
    import shutil
    import zipfile
    from os.path import isfile, isdir
    from os.path import join  
    from os import stat
    from datetime import datetime, time, timedelta, date
    from os import stat
    from string import upper
    from shutil import move
    
    SERVICES_MANAGEMENT = ""
    TVHEADEND_SERVICE = ""
    TVHEADEND_USER = ""
    TVHEADEND_USER_ID = ""
    TVHEADEND_GROUP = ""
    TVHEADEND_GROUP_ID = ""
    TVHEADEND_PERMISSIONS = "0755" #"u=rwX,g=,o="
    TVHEADEND_DIR = ""
    TVHEADEND_CONFIG_DIR = ""
    GUINIGUADA_DIR = pathRuta()
    REMOTE_LIST_VERSION = ""
    TVHEADEND_SCRIPTS_DIR = ""
    
    TVHEADEND_CHANNEL_USER  = ""
    TVHEADEND_CHANNEL_GROUP = ""
    TVHEADEND_CHANNEL_PERMISSIONS = ""
    
    TVHEADEND_INPUT_USER = ""
    TVHEADEND_INPUT_GROUP = ""
    TVHEADEND_INPUT_PERMISSIONS = ""
    
    TVHEADEND_PICONS_USER = ""
    TVHEADEND_PICONS_GROUP = ""
    TVHEADEND_PICONS_PERMISSIONS = ""
    
    TVHEADEND_EPGGRAB_USER = ""
    TVHEADEND_EPGGRAB_GROUP = ""
    TVHEADEND_EPGGRAB_PERMISSIONS = ""
    
    os.system('clear')
    
    #Fecha actual en formatado date
    hoy = datetime.now()
    
    #Comprobamos que tipo de Linux(Synology, Ubuntu o Librelec    
    uname = os.popen("uname -a").read()
    
    #Comprobamos que el Sistema Operativo es Linux
    so = platform.system()
    
    if not (so == "Linux" or so == "LibreELEC"):
        
        os.system('clear')
        menucabecera()
        barramenu(0)
        print
        mensaje = "\t\t     ----- SISTEMA DISTINTO DE LINUX -- NO SE PUEDE INSTALAR -----"
        mensajelog(mensaje)
        print mensaje
        print     
        exit(1)
        
    #Coprobamos que el usuario esta logueado como root
    usuroot = commands.getoutput('id -u')
   
    if not usuroot == '0':
        
        os.system('clear')
        menucabecera()
        
        mensaje = "\t\t\t\tNO ESTA UD. LOGUEADO COMO ROOT"
        mensajelog(mensaje)
        print mensaje
        exit(0)
        
    #Comprobamos si esta instalado python
    pyt = platform.python_version()
    
    if not pyt:
        
        os.system('clear')
        menucabecera()
        
        mensaje = "\t\t\t\tNO TIENE UD. INSTALADO PYTHON"
        mensajelog(mensaje)
        print mensaje
        mensaje = "          ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        print mensaje
        print
        ficheroLog(pathRuta()+ "/", mensaje)
        exit(1)
        
    #Copiamos fichero log anterior para no borrarlo
    file = pathRuta() + '/GUINIGUADA-EPG_Install.log'
    filer = pathRuta() + "/GUINIGUADA-EPG_Install.old.log"
    
    if isfile(file):
        
        os.rename(file,filer)       
            
    if "synology" in uname:
                
        sistema = 1 
        sistemaname = "SYNOLOGY" 
        versiondsm = commands.getoutput("more /etc.defaults/VERSION")
        versdsm = versiondsm.split('\n')
        
        for vdsm in versdsm:
         
            parte1 = ""
            parte2 = ""
            
            if "majorversion" in vdsm:
                
                parte1 = vdsm.split('=')
                parte2 = parte1[1].replace('"','')
                mav = parte2
                sys.path.append("/usr/local/lib/python2.7/site-packages")
                sys.path.append("/usr/lib/python2.7/site-packages")
#                 sys.path.remove("PYTHONPATH")
#                 sys.path.insert(0, "PYTHONPATH='${PYTHONPATH}/usr/local/lib/python2.7/site-packages:/usr/lib/python2.7/site-packages'")
               
                        
            elif "minorversion" in vdsm:
                
                parte1 = vdsm.split('=')
                parte2 = parte1[1].replace('"','')
                miv = parte2
                
            elif "buildnumber" in vdsm:
                
                parte1 = vdsm.split('=')
                parte2 = parte1[1].replace('"','')
                bum = parte2    
                
            elif "smallfixnumber" in vdsm:
            
                parte1 = vdsm.split('=')
                parte2 = parte1[1].replace('"','')
                smf = parte2
                
                
        SYNOLOGY_VERSION = mav + '.' + miv +'-' + bum +'-' + smf
        
        dir1 = "/var/packages/"
        dir2 = commands.getoutput("ls /var/packages/ | grep tvheadend")
        dir3 = "/target/var"
        
        if not dir2: 
            
            barramenu(0)
            mensaje = "\t\t     ----- SERVICIO TVHEADEND NO INSTALADO  -----"
            mensajelog(mensaje)
            print mensaje
            print
            sys.exit(0)
        
        TVHEADEND_SCRIPTS_DIR = dir1 + dir2 + "/scripts/start-stop-status"
        
        TVHEADEND_DIR = dir1 + dir2 + dir3
                
        status = commands.getoutput(TVHEADEND_SCRIPTS_DIR + " status")
        
        TVHEADEND_SERVICE = commands.getoutput("synoservicecfg --list | grep tvheadend")
        
        if not TVHEADEND_SERVICE == "pkgctl-tvheadend":
            
            SERVICES_MANAGEMENT = "OLD"
            #TVHEADEND_GRABBER_DIR="/usr/bin"
                       
        else:
            
            SERVICES_MANAGEMENT = "NEW"    
            #TVHEADEND_GRABBER_DIR="/usr/local/bin" 
        
        if "Tvheadend is not running" in status:
              
            barramenu(0)
            mensaje = "\t\t\t   ----- STATUS TVHEADEND STOP  -----"
            mensajelog(mensaje)
            print mensaje
            print
            
            barramenu(0)
            
            iniciado = IniciarTvh()          
        
        TVHEADEND_GRABBER_DIR="/usr/local/bin"
        
        TVHEADEND_USER = commands.getoutput('cut -d: -f1 /etc/passwd | grep -E tvheadend')
        TVHEADEND_USER_ID = commands.getoutput("id -u " + TVHEADEND_USER)
        
        if SERVICES_MANAGEMENT == "OLD":
            
            TVHEADEND_GROUP = commands.getoutput("id -gn " + TVHEADEND_USER)
                                  
        else:
                        
            groups = grp.getgrall()
            for group in groups:
                for user in group[3]:
                    if user == TVHEADEND_USER:
                        
                       TVHEADEND_GROUP = group[0]
                   
        TVHEADEND_GROUP_ID = commands.getoutput("cat /etc/group |grep " + TVHEADEND_GROUP + "| cut -d: -f3")
       
        TVHEADEND_CONFIG_DIR = dir1 + dir2 + dir3 + '/epggrab'
        
        os.system('clear')
            
        contmenucabecera = 1
        menucabecera()
        menudatos()
        barramenu(0)
        print
        
    elif "LibreELEC" in uname:
        
        sistema = 2
        sistemaname = "LIBRELEC"
        
        os.system('export LC_ALL=es_ES-UTF-8')
                
            
        dir1 = "/storage/.kodi/userdata/addon_data/"
        
        dir2 = commands.getoutput("ls /storage/.kodi/userdata/addon_data/ | grep tvheadend")
        
        if not dir2: 
        
            barramenu(0)
            mensaje = "\t\t     ----- SERVICIO TVHEADEND NO INSTALADO  -----"
            mensajelog(mensaje)
            print mensaje
            print
            sys.exit(0)
            
        TVHEADEND_SERVICE = commands.getoutput("systemctl list-unit-files| grep tvheadend | tr -s ' ' | cut -d' ' -f1")
        
        TVHEADEND_USER="root"
        TVHEADEND_GROUP="video"
        
        TVHEADEND_USER_ID = commands.getoutput("id -u " + TVHEADEND_USER)
        TVHEADEND_GROUP_ID = commands.getoutput("id -g " + TVHEADEND_USER)           
                    
        TVHEADEND_CONFIG_DIR = dir1 + dir2 + "/epggrab"
        
        TVHEADEND_DIR = dir1 + dir2
                
        dir3 = "/storage/.kodi/addons/"
        
        dir4 = commands.getoutput("ls /storage/.kodi/addons/ | grep tvheadend")
        
        dirt5 = "/bin"
        
        TVHEADEND_GRABBER_DIR= dir3 + dir4 + dirt5
        
        obtprogrpper()
        
        descargazip()
        
        dircpmod = pathRuta() + '/scripts_module'
        
        dirser = pathRuta() + '/service'
            
        if isdir(dircpmod) and isdir(dirser):
                
            os.system("cp -R " + dircpmod + "/* /storage/.kodi/addons/")
            
            os.system("cp -R " + dirser + "/resource.language.es_es /storage/.kodi/addons/")
            
            os.system("cp -R " + dirser + "/service.locale /storage/.kodi//userdata/addon_data/")
            
                    
            sys.path.append('/storage/.kodi/addons/script.module.beautifulsoup4/lib')
            sys.path.append('/storage/.kodi/addons/script.module.beautifulsoup/lib')
            sys.path.append('/storage/.kodi/addons/script.module.requests/lib')
            sys.path.append('/storage/.kodi/addons/script.module.tzlocal/lib')
            sys.path.append('/storage/.kodi/addons/script.module.pytz/lib')
            sys.path.append('/storage/.kodi/addons/script.module.urllib3/lib')
            sys.path.append('/storage/.kodi/addons/script.module.html5lib/lib')
            sys.path.append('/storage/.kodi/addons/script.module.six/lib')
            sys.path.append('/storage/.kodi/addons/script.module.chardet/lib')
            sys.path.append('/storage/.kodi/addons/script.module.certifi/lib')
            sys.path.append('/storage/.kodi/addons/script.module.metadatautils/lib')
            sys.path.append('/storage/.kodi/addons/script.module.disutils/lib')
            sys.path.append('/storage/.kodi/addons/script.module.simplecache/lib')
            sys.path.append('/storage/.kodi/addons/script.module.simplejson/lib')
            sys.path.append('/storage/.kodi/addons/script.module.dateutil/lib')
            sys.path.append('/storage/.kodi/addons/script.module.idna/lib') 
                             
            os.system('clear')
            
            contmenucabecera = 1
            menucabecera()
            menudatos()
            barramenu(0)
                        
            mensaje = "\t\t    --- COPIANDO SCRIPTS.MODULE /storage/.kodi/addons/ ---"
            mensajelog(mensaje)
            print mensaje
            print
            barramenu(0)
            t.sleep(2)
            
        else:
            os.system('clear')
            menucabecera()
            barramenu(0)
                       
            mensaje = "\t\t     ----- NO ENCONTRADO EN RUTA DE INSTALACION -----"
            mensajelog(mensaje)
            print mensaje 
            print
            mensaje = "\t\t     -----      DIRECTORIO module_scripts -----"
            mensajelog(mensaje)
            print mensaje  
            print          
            barramenu(0)            
            exit(1)
            
            
    else:
        
        sistema = 3
        sistemaname = "UBUNTU"
        
        pipinstall()
    
        piplibinstall()
        
        status = commands.getoutput("systemctl status tvheadend")
        
        statussplit = status.split("\n")
        
        statusloaded = statussplit[1]
        
        statusactive = statussplit[2]
        
        if "inactive" in statusactive or "dead" in statusactive:
              
            barramenu(0)
            mensaje = "\t\t\t   ----- STATUS TVHEADEND STOP  -----"
            mensajelog(mensaje)
            print mensaje
            print           
            
            TVHEADEND_SERVICE = 'tvheadend'  
                                           
            barramenu(0)
            
            #iniciado = IniciarTvh() 
           
        elif "No such file" in statusloaded:
            
            barramenu(0)
            mensaje = "\t\t     ----- SERVICIO TVHEADEND NO INSTALADO  -----"
            mensajelog(mensaje)
            print mensaje
            print
            sys.exit(0)
               
        else:
            
            TVHEADEND_SERVICE = 'tvheadend'    
          
        TVHEADEND_USER = commands.getoutput("cut -d: -f1 /etc/passwd | grep -E 'tvheadend|hts'")  
        TVHEADEND_USER_ID = commands.getoutput("id -u " + TVHEADEND_USER)
         
        groups = grp.getgrall()
        for group in groups:
            for user in group[3]:
                if user == TVHEADEND_USER:                        
                   TVHEADEND_GROUP = group[0]
        
        TVHEADEND_GROUP = "video"     
        TVHEADEND_GROUP_ID = commands.getoutput("cat /etc/group |grep " + TVHEADEND_GROUP + "| cut -d: -f3") 
        
        TVHEADEND_DIR = "/home/hts/.hts/tvheadend"
        
        TVHEADEND_CONFIG_DIR = "/home/hts/.hts/tvheadend/epggrab"
        TVHEADEND_GRABBER_DIR = "/usr/bin"
        
        obtprogrpper()
        
        
    #Paramos servicio tvheadend
    parado = PararTvh()
              
    if parado == 0:    
        
        #Comprobamos si existe lista de canales previa
        rutachannels = TVHEADEND_DIR + '/channel'
              
        #Si no existe lista de canales
        if not isdir(rutachannels):
            
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            
            barramenu(0)
            mensaje = "\t\t     ----- NO TIENE UD. LISTA DE CANALES  -----"
            mensajelog(mensaje)
            print mensaje
            print          
            barramenu(0)
            
            #Mostramos el menu
            menucanales()
          
            descargarcan = opmenusnCANALES()
                                 
            barramenu(0)
            
            if descargarcan > 0:
                
                backup()
                
                descargazip()
                
                borrarepgdbv2()
                
                descargacanales()
                
                descargaconfig(sistema)
                
                backupgrabbers()
                   
                descargagrabber()
                
                epgtrue()
                
                if not "LibreELEC" in uname:
            
                    asigcrontab()
                    
                else:
                    
                    asigcrontabLibreElec()
                
                piconconfig()
                
                borrararchdescarg()
                
            
            #Iniciamos servicio
            iniciado = IniciarTvh()
              
            if iniciado == 0:
                  
                os.system('clear')
                contmenucabecera = 1
                menucabecera()
                contmenudatos = 1
                menudatos()
                mensaje = "\t\t    ----- STATUS TVHEADEND START"
                mensajelog(mensaje)
                print mensaje
                print
                barramenu(0)   
                  
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
            
            
        #Si existe lista de canales       
        else:
           
            os.system('clear')
            contmenucabecera = 1
            menucabecera()
            contmenudatos = 1
            menudatos()
           
            barramenu(1) 
          
            mensaje = "\t\t       ----- TIENE UD. UNA LISTA DE CANALES  -----"
            mensajelog(mensaje)
            print mensaje
            print
            
            barramenu(0)  
          
            descargarcan = opmenusnCANALES2()
                                
            barramenu(1)  
            
            backup()
                
            descargazip()
            
            borrarepgdbv2()
            
            if descargarcan > 0:
                
                descargacanales()
                
            descargaconfig(sistema)
            
            backupgrabbers()
          
            descargagrabber()
            
            epgtrue()
            
            if not "LibreELEC" in uname:
            
                asigcrontab() 
                
            else:
                    
                asigcrontabLibreElec()
            
            piconconfig()
            
            borrararchdescarg()
        
            #Iniciamos servicio
            iniciado = IniciarTvh()
        
    else:
              
        mensaje = "\t\t     ----- FALLO AL DETENER SERVICIO TVHEADEND -----"
        mensajelog(mensaje)
        print mensaje
                  
        barramenu(0)
        exit(1)    
        
            
    
        
##############################################################################################

except IOError as e:        
    print("Error OS: {0}".format(e))
    if parado == 0:
        
        iniciado = IniciarTvh()      
    
except ValueError as e:
    print('Non-numeric data found in the file.', e )
    if parado == 0:
        
        iniciado = IniciarTvh()

except ImportError as e:    
    mensaje = "Ud. no tiene instalado el modulo: {0}".format(e.message[16:])
    print mensaje
    mensajelog(mensaje)
    print mensaje
    mensaje = "\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print mensaje
    print
    mensajelog(mensaje)

    mensaje = "                        -- -- -- -- -- -- --         FIN PROGRAMA         -- -- -- -- -- -- --    "
    print mensaje
    mensajelog(mensaje)
    print mensaje
    mensaje = "\t\t++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    print mensaje
    print
    mensajelog(mensaje)
    
        
except EOFError as e:
    print('Why did you do an EOF on me?', e )
    if parado == 0:
        
        iniciado = IniciarTvh()

except KeyboardInterrupt as e:
    print('You cancelled the operation.', e )
    if parado == 0:
       
        iniciado = IniciarTvh()
    
finally:           
    
    #Fecha actual en formatado date
    hoy = datetime.now()
    print
    mensaje = ("\t\t    ------ INSTALACION Finalizada: %s -- %s  -----" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S")))
    print mensaje   
    mensajelog(mensaje)
    print    
    barramenu(0) 
    
    #Asignamos permisos al directorio de instalacion
    commands.getoutput('chmod 0777 ' + pathRuta())  
################################################################################################      