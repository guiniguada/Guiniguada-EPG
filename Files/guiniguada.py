#!/usr/bin/python
# -*- coding: utf-8 -*-
#Objetivo: Descargar EPG MOVISTAR+
#Version: 1.0  

############################################################
#Funcion para obtener datos del SO
def so():
    
    #PATH ruta
    ruta = pathRuta()
    
    #Mostramos informacion sobre el sistema
    nh = "Nombre del host: " + platform.node()
    ficheroLog(ruta,nh)
    so = "Sistema Operativo: " + platform.system()
    ficheroLog(ruta,so)
    dist = "Distribucion: " + str(platform.dist()).replace('(', '').replace(')', '').replace("'", '').replace(" ", '').replace(",", "-")
    ficheroLog(ruta,dist)
    rel = "Release del S.O.: " + platform.release()
    ficheroLog(ruta,rel)
    ver = "Version del S.O.: " + platform.version()
    ficheroLog(ruta,ver)
    pro = "Procesador: " + platform.processor()
    ficheroLog(ruta,pro)
    proc = "Procesador: " + platform.machine() + " compatible"
    ficheroLog(ruta,proc)
    arq = "Arquitectura: " + str(platform.architecture()).replace('(', '').replace(')', '').replace("'", '').replace(" ", '').replace(",", "-")
    ficheroLog(ruta,arq)
    pyt = "Version de Python: " + platform.python_version()
    ficheroLog(ruta,pyt)
    rut = "PATH: " + ruta
    ficheroLog(ruta,rut + "\n")
 
############################################################      
#Funcion para registrar logs y mensajes
def ficheroLog(ruta,mensaje):
            
    filelog = open(ruta + '/GUINIGUADA-EPG.log', 'a+')
    filelog.write(mensaje)
    filelog.write('\n')
    filelog.close()

############################################################    
#Funcion para obtener la ruta/path
def pathRuta():
    
    #Obtenemos la ruta donde se esta ejecutando el script
    pathname = os.path.dirname(sys.argv[0])    
    ruta = str(os.path.abspath(pathname))  
      
    return ruta

############################################################  
#Funcion para obtener la lista de Canales Activos
def obtenerCanalesActivos(cursor):
    
    cursor.execute("SELECT * FROM CANALES WHERE DESCARGA_ACTIVA='1'")    
    carows = cursor.fetchall()    
    #Si obtenemos Canales Activos
    if carows:
        
         return carows
    else:
        #print
        mensaje = "                        -- -- -- -- -- -- --   TABLA CANALES NO TIENE CANALES ACTIVOS     -- -- -- -- -- -- --    "
        ficheroLog(pathRuta(), mensaje)
        #print mensaje 
        mensaje = "                        -- -- -- -- -- -- --         FIN PROGRAMA         -- -- -- -- -- -- --    "
        #print mensaje
        ficheroLog(pathRuta(),mensaje)
        exit(1)           
        
#Funcion para borrar la parrilla  y las fichas que no esten en varios programas.
#def borrarParrillaFichas(dia,horaa):
#def borrarParrillaFichas():
def borrarParrilla(cursor, db):
        
        try:
                     
            cursor.execute("DELETE FROM PARRILLA")
            db.commit()
    
        except sqlite3.IntegrityError:
    
            pass 
        
        except sqlite3.OperationalError as e:
            
            mensaje = "OperationalError: " + e.args[0]
            ficheroLog(pathRuta(), mensaje)
            #print "OperationalError: " , e 
            
############################################################
#Funcion para borrar de la parrilla los programas cuya fecha de inicio y hora de inicio sea menor a la
#hora actual obtenidas de la Vista PARRFICH_A_BORRAR, y las fichas que no esten en varios programas.
def borrarFichasHuerfanas(cursor, db):
    
    cursor.execute("SELECT * FROM FICHASINPARRILLA")
    rowsParrilla = cursor.fetchall()
    
    if rowsParrilla:
        
        try:
        
            for z in rowsParrilla:       
                       
                cursor.execute("SELECT COUNT(*) FROM PARRILLA WHERE FICHA=? ORDER BY ROWID ASC", (z[0],))
                #resultado = cursor.execute("SELECT COUNT(FICHA) FROM PARRILLA2 WHERE FICHA='9999999999'")
                rowsresultado = cursor.fetchall()
                conta =  rowsresultado[0][0]
               
                if rowsresultado[0][0] == 0:
                
                    cursor.execute("DELETE FROM FICHA_TECNICA WHERE FICHA=?", (z[0],))
                    
                    
                #cursor.execute("DELETE FROM PARRILLA WHERE rowid=?", (z[0],))
                
                    db.commit()    

        except sqlite3.IntegrityError:
    
            pass 
        
        except sqlite3.OperationalError as e:
            
            mensaje = "OperationalError: " + e.args[0]
            ficheroLog(pathRuta(), mensaje)
            #print "OperationalError: " , e 
            
############################################################
#Funcion conectar con URL metodo GET
def peticionURLGet(url, ficha):
    statusCode = 0
    controlconec = 0

    while(statusCode != 200 and controlconec < 2):     
                        
        try:
            
            #req = requests.get(url, headers, timeout=None)  .
            req = requests.get(url,timeout=None)  
            #req = progressBar(url)       
            statusCode = req.status_code            
            controlconec += 1
            #print "controlconec", controlconec
                       
        except requests.exceptions.Timeout as e:
            
            #print("Timeout")
            ficheroLog(pathRuta(),"Error %s:" % e.args[0])
            #t.sleep(5)
            controlconec += 1
            #print "controlconec Timeout", controlconec
            
        except requests.exceptions.TooManyRedirects as e:
            
            #print("Too Many Redirects")
            ficheroLog(pathRuta(),"Error %s:" % e.args[0])
            t.sleep(10)
            controlconec += 1
            #print "controlconec Too Many Redirects", controlconec
            
        except requests.ConnectionError as e:
        
            #print("Connection Error")
            ficheroLog(pathRuta(),"Error %s:" % e.args[0])
            t.sleep(10)
            controlconec += 1
            #print "controlconec Connection Error", controlconec
            
                    
        if(controlconec > 1 and statusCode != 404):        
            
            mensaje = "         -- -- -- -- -- -- -- -- -- --          Reconexion   ~~    Status Code: %d -- -- -- -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            ficheroLog(pathRuta(),mensaje)
            #print
            #controlconec = 0
            progreso = 0
            pepe = "."
            while progreso <= 100:
                #print '%s%%' % progreso,
                #print '%s' % pepe,
                #------------------------------------------- if progreso == 100:
                    #------------------------------------------------- print'\r'

                progreso += 1
                t.sleep(0.2) # porque no veriamos nada, solo 99%
                sys.stdout.flush() # porque el stdout normalmente hace caching
            #print'\n' 
            #t.sleep(10)
            #sys.exit(1)  
            
    if(controlconec >= 5): 
        
        if url.find("=") >= 0:
            #Url de la Ficha Tecnica    
            fic = url[int(url.find("=")) + 1:]
            fic = fic.replace('R&id=','')
            
            mensaje = "          -- -- -- -- -- -- -- -- -- -- Conexión No Realizada ~~ " + ficha + "  Status Code: %d -- -- -- -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            ficheroLog(pathRuta(),mensaje)
            #print
        else:
            
            mensaje = "         -- -- -- -- -- -- -- -- -- -- -- Conexión No Realizada ....... Status Code: %d -- -- -- -- -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            ficheroLog(pathRuta(),mensaje)
            #print
        
    else:     
        
        if statusCode == 404:
            
            #Url de la Ficha Tecnica    
            fic = url[int(url.find("=")) + 1:]
            fic = fic.replace('R&id=','')
            mensaje = "                         -- -- -- -- -- -- -- Conexión NO Realizada ~~ " + ficha + "  Status Code: %d -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            ficheroLog(pathRuta(),mensaje)
            #print
        
        elif url.find("=") >= 0:
           
            #Url de la Ficha Tecnica    
            fic = url[int(url.find("=")) + 1:]
            fic = fic.replace('R&id=','')
            mensaje = "                         -- -- -- -- -- -- -- Conexión Realizada ~~ " + ficha + "  Status Code: %d -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            ficheroLog(pathRuta(),mensaje)
            #print
        #else:
                       
            #mensaje = "                        -- -- -- -- -- -- -- Conexión Realizada ~~ Status Code: %d -- -- -- -- -- -- -- " %statusCode
            #print mensaje
            #ficheroLog(pathRuta(),mensaje)
            #print
          
    return req

############################################################
def formatearDatosUrl(dato, modo):
    
    #Titulo o T Original
    if modo == "1":
        
        datolist = dato.split(" ")
        resultado = ""
        
        for i in range (len(datolist)):
        
            tit = str(datolist[i]).replace(","," ").replace(":","").replace(";","").replace("&"," ").replace("?"," ")
            
            if i < len(datolist) - 1:
                resultado = resultado + tit  + "+"
            else:
                resultado = resultado + tit      
    
    return resultado  

############################################################
def filtrosbusquedaImagenWeb(titulo, ficha, modo):
    
    encontrado = 0
    
    #Por Titulo
    if modo == "1":
        #&genre=TV_SE                      
        tipo = "&stype[]=title&country=&genre=TV_SE&fromyear=&toyear="
    
    else:
        
        tipo = "&stype[]=title&country=&genre=&fromyear=&toyear="
            
    divmovcard = busquedaImagenWeb(titulo,tipo)
    
    if len(divmovcard) == 1:
        
        encontrado = 1
     
    elif len(divmovcard) > 1:
        
        for divmov in divmovcard:
            
            divmovie = divmov.find('div',{'class':'mc-poster'})
            
            imgfich = divmovie.find('img')
            
            tit = imgfich.get('alt', None).encode('utf-8')
            
            tit = tit.replace(" (Serie de TV)","").replace(":","")
            
            if tit.find("(TV)") >= 0:
                
                tit = tit.replace(" (TV)","")
                
                if tit == titulo.replace("+"," "):
                                     
                    encontrado = 1    
                    
                    break           
                
            
            elif tit == titulo.replace("+"," "):
                                     
                encontrado = 1
                
                break
         
    if encontrado == 1:
                
        insertarImagenWeb(divmovcard,titul)
                
    else:

        mensaje = "              -- -- -- -- -- -- --  FICHA: %s ~~ TITULO NO ENCONTRADO: %s  -- -- -- -- -- -- --    "%(ficha[0].encode('utf-8'),titulo)
        #print mensaje
        ficheroLog(pathRuta(),mensaje)
        #print
        
        
    return encontrado

############################################################
def busquedaImagenWeb(data, tipo):
    
    req = peticionURLGet(urlImgFilmAfBA + data + tipo, ficha) 
    
    #Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(req.text, 'lxml')
    
    #Obtenemos body desde htm para poder capturar ('div',{'id':'container_parrilla_vacia'}), 
    bod = html.find('body')
   
    divpageinfo = bod.find('div',{'class':'adv-search-page-info'})
   
    if divpageinfo:
       
        divmovcardlist = []
       
        if divpageinfo.text <> " ":
           
            bb = divpageinfo.find_all('b')
            
            np = ""
           
            for b in range(len(bb) - 1):
               
                np = bb[b].text
               
            divmovc = bod.find_all('div',{'class':'movie-card movie-card-1'})
               
            for divmov in divmovc:
               
                divmovcardlist.append(divmov) 
               
            if np <> "":
               
                numpage = int(np)               
    
                for n in range(1,numpage):
                   
                   p = n + 1
                   
                   urlpage = "http://www.filmaffinity.com/es/advsearch.php?page=" + str(p) + "&stext="  + data  + "&stype[]=title&genre=TV_SE"           
                              
                   req = peticionURLGet(urlpage, ficha) 
                                 
                   #Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
                   html = BeautifulSoup(req.text, 'lxml')
                    
                   #Obtenemos body desde htm para poder capturar ('div',{'id':'container_parrilla_vacia'}), 
                   bod = html.find('body')
                   
                   divmovc = bod.find_all('div',{'class':'movie-card movie-card-1'})
                   
                for divmov in divmovc:
               
                    divmovcardlist.append(divmov)
                       
            
                divmovcard = divmovcardlist
                
                
            else:
            
                divmovcard = divmovcardlist
                
                
        else:
            
            divmovcard = bod.find_all('div',{'class':'movie-card movie-card-1'})
            
        
    else:
       
        divmovcard = bod.find_all('div',{'class':'movie-card movie-card-1'})
       
           
   
    return divmovcard 

############################################################
def insertarImagenWeb(divmovcard,titul):
    
    divimage = divmovcard[0].find('div',{'class':'mc-poster'})
                
    aimage = divimage.find('a')
    
    im = aimage.find('img')
    
    imagen = im.get('src', None).encode('utf-8').replace("msmall","mmed")
    
    cursor.execute('SELECT * FROM FICHAS_SINIMAGSERIE WHERE TITULO=?',(titul))
    
    rowsFichasActualizar = cursor.fetchall()
    
    for fichsinimgact in rowsFichasActualizar:

        cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagen,fichsinimgact[0],))

        db.commit()
    
    titul = ""

############################################################
############################################################
def fuente1(canalid, cadena, idlist,filist,hilist,fflist,hflist,titlist,generolist,urlfichalist, statusCode):
    
    ################
    #Variable con la hora actual en formato time
    hoy = datetime.now()
    fechaEPG = hoy
    
    #################
    # Numero de dias a descargar
    i = 15   
    
    #Variable para controlar cuando de forma consecutiva figura la misma ficha. 
    ultimaficha = "99999999999"
    ficha = ""
    
    #Variable para poder asignar la hora final a cada entrada de la parrilla, de la cual, solo obtenemos la hora inicial. 
    ultimahora = "00:00"
    hora = ""

    contador = 0
    
    chivatohf = 0
    
    pre = re.compile(r'[a-zA-ZñÑáéíóúÁÉÍÓÚ\s]+')
    
    cadena1 = cadena
    cadena1 = cadena1.replace(' ','').replace('.','')
    
    if cadena1.find('BeinMax') >= 0:
        
        cadre = pre.search(cadena1)
        cadena7 = cadre.group(0)
        
    else:
        
        cadena1 = "XXXXXX"
    
    cadena2 = "BeinLaLigaMax"
    cadena3 = "MovistarPartidazo"
    cadena6 = "LaLigaTV"
    cadena7 = "BeinMax"
    cadena8 = "Multideporte"            
    cadena9 = "Multifútbol"
    
    if cadena1.find('BeinMax') >= 0:
        
        cadre = pre.search(cadena1)
        cadena7 = cadre.group(0)
    
    for j in range(i):
                
        #print
        mensaje = "     ............... ****** DESCARGANDO EPG DEL CANAL: " + canalid + " | " + cadena + " FECHA: " + fechaEPG.strftime("%d-%m-%Y") + " ****** ..............."
        #print mensaje
        ficheroLog(pathRuta(), mensaje)
        #print
        
        url = urlParrilla  + "/" + canalid + "/" + fechaEPG.strftime("%Y-%m-%d")
        req = peticionURLGet(url, ficha)
        statusCode = req.status_code 
        
        if statusCode == 200:  
    
            html = BeautifulSoup(req.text, 'lxml')
            
            #Obtenemos body desde htm para poder capturar ('div',{'id':'container_parrilla_vacia'}), 
            bod = html.find('body')
          
            divele = bod.find_all('div',{'id':re.compile('ele-[0-9\s]*')})
            
            c = 1
            
            #Variable para controlar la fecha y hora final del primer y ultimo elemento de la parrilla de cada canal    
            chivato = 0
            
            chivatom = 0
            
            if len(divele) > 1:
                
                #for d in range(1, len(divele)):
                d = 0
                
                del divele[0]
                
                while d < len(divele):
                    
                    if divele[d].find('a',{'class':'j_ficha'}):
                        
                        a = divele[d].find('a',{'class':'j_ficha'})
                        
                        urlficha = a.get('href', None)
                                        
                        #Cuando la url de la ficha tecnica viene mal
                        if urlficha:
                                
                            if urlficha.find("=") >= 0:
                                
                                #Url de la Ficha Tecnica    
                                ficha = urlficha[int(urlficha.find("=")) + 1:]   
                                ficha = ficha.replace('R&id=','')
                                                        
                            else:
                                    
                                ficha = ""
                        
                        else:
                         
                            urlficha = ""
                     
                    divgth = divele[d].find('div',{'class':'box'})
                    
                    #Genero
                    l1 = divgth.find('li',{'class':'genre'})
                    
                    if l1 is None:
                                 
                        genero = "Otros"
                                                              
                    else:
                           
                        genero = l1.text
                    
                    #Titulo
                    l2 = divgth.find('li',{'class':'title'})
                    ttitulo = l2.text.encode('utf8')
                    titulo = str(ttitulo).lstrip()
                    tit = titulo.replace(' ','')                                                                              
                    
                    #Hora
                    l3 = divgth.find('li',{'class':'time'})
                    hora = l3.text.strip()
                    
                    if chivato == 0 and ficha:
                                                                    
                        horc1 = hora.split(':')
                        horc2 = ultimahora.split(':')
                        inthorc1 = int(horc1[0])
                        inthorc2 = int(horc2[0])
    
                        if inthorc1 < 23 and inthorc1 < inthorc2:  #and fechaEPG <= (filist[len(filist) - 1])
    
                            chivato += 1
    
                            fechaEPG = fechaEPG + timedelta(days=1)
                            
                    if ficha and (not cadena1 in tit and not cadena2 in tit and not cadena7 in tit
                                  and not cadena8 in tit and not cadena9 in tit): 
                        
                        urlfichalist.append(urlficha)                       
                        idlist.append(ficha)                        
                        filist.append(fechaEPG)
                        generolist.append(genero)
                        titlist.append(titulo)
                        hilist.append(datetime.strptime(hora + ":00", "%H:%M:%S").time())
                        
                        if chivatohf > 0:
                            
                            hflist.append(datetime.strptime(hora + ":00", "%H:%M:%S").time())
                            fflist.append(fechaEPG)
                            
                        else:
                            
                            chivatohf = 1
                        
                        ultimaficha = ficha                              
                        ultimahora = hora
                        #print ultimahora
                        
                        
                    elif chivatohf > 0 and (cadena1 in tit or cadena2 in tit or cadena7 in tit
                                            or not cadena8 in tit or not cadena9 in tit):
                         
                        hflist.append(datetime.strptime(hora + ":00", "%H:%M:%S").time())
                        fflist.append(fechaEPG)
                        
                        chivatohf = 0
                        ultimahora = "00:00"
                        hora = ""
                            
                    ficha = ""         
                    del divele[d]
                             
            else:
    
                #print
                mensaje = "                           ............... ******    CANAL SIN PARRILA      ****** ...............              "
                #print mensaje
                ficheroLog(pathRuta(),mensaje)
                #print
                mensaje = "          ------------------------------------------------------------------------------------------------------------"
                ficheroLog(pathRuta(),mensaje)
                #print mensaje
                #print
                
                if not (canalid =="CPPART" or canalid =="BEMAX1" or canalid =="MULTI5" or canalid =="ARTHUR"
                    or canalid =="MFUT6" or canalid =="CPLI2A" or canalid =="MUTI7" or canalid =="CPL2B"
                    or canalid =="CPL2C" or canalid =="CPL2D" or canalid =="BELIG1" or canalid =="BELIG2"
                    or canalid =="BELIG3" or canalid =="BELIG4" or canalid =="BELIG5" or canalid =="BELIG6" 
                    or canalid =="BELIG7" or canalid =="LIGBA1" or canalid =="LIGBA2" or canalid =="LIGBA3"
                    or canalid =="LIGBA4" or canalid =="MFUT1" or canalid =="MFUT2" or canalid =="MFUT3" 
                    or canalid =="MFUT4" or canalid =="MFUT5" or canalid =="MFUT9" or canalid =="MFUT7"
                    or canalid =="MFUT8" or canalid =="MUFUT9" or canalid =="CPEV" or canalid =="ARTHUR" 
                    or canalid =="USOP2" or canalid =="USOP3" or canalid =="USOP11" or canalid =="MULTI8"
                    or canalid =="MULTI6"):
                    
                    break
                
                chivatohf = 0       
            
                
        i =+ 1 
        
        if statusCode == 404: 
            
            break
        
        if statusCode == 200:
            if chivato == 0:
                fechaEPG = fechaEPG + timedelta(days=1)
            
    if statusCode == 200: 
                
        if (len(filist) > len(fflist) or len(hilist) > len(hflist)) and chivatohf > 0:
            
            hflist.append(datetime.strptime(ultimahora, "%H:%M").time())                    
            fflist.append(fechaEPG)
                    
    return statusCode                        
############################################################
############################################################
def fuente2(canalid, cadena, idlist,filist,hilist,fflist,hflist,titlist,generolist,urlfichalist,statusCode):

    ################
    #Variable con la hora actual en formato time
    hoy = datetime.now()
    fechaEPG = hoy
    
    #################
    # Numero de dias a descargar
    i = 15  
    
    #Variable para controlar cuando de forma consecutiva figura la misma ficha. 
    ultimaficha = "uh"
    ficha = "oh"
    
    #Variable para control en Parrilla
    contador = 0
    #Variable que cuando valor > 0 ya no comprobamos mas si la hora de la parrilla es mayor o igual que la hora actual
    chivatoh = 0        
    
    #Variable con la hora actual en formato time
    hoy = datetime.now()
    hora_actual = time(hoy.hour, hoy.minute, hoy.second)
    #hora_actual = time(9,36,32)
    dhaux2 = datetime.combine(hoy, hora_actual)       
    
    #Variable para poder asignar la hora final a cada entrada de la parrilla, de la cual, solo obtenemos la hora inicial. 
    ultimahora = "00:00"
    hora = ""
    
    #Bucle para Descargar EPG - Días Disponibles
    for j in range(i):
   
        
        #Variable para controlar la fecha y hora final del primer y ultimo elemento de la parrilla de cada canal    
        chivato = 0 
        
        if cadena == 'Crimen + Investigación':
            
            cadenaParametros = 'Crimen+++Investigación'
            
        elif cadena == 'Nick Jr.':
            
            cadenaParametros = 'NICK+JR'
            
        elif cadena == 'A&E':
            
            cadenaParametros = 'A&E'
            
        else:
        
            cadenaParametros = cadena.replace(' HD','').replace(' ','+')
        
        #Parametros para obtener la parrilla de cada canal
        parametros = {"valores_cadenas[0][0][id]": canalid, "valores_cadenas[0][0][cad]": cadenaParametros, "max_canales": "10", "dia_pases": fechaEPG.strftime("%Y-%m-%d")}
         
        #Enviamos la peticion Post                   
        req = requests.post(urlParrilla2, parametros, timeout=None)

        #print
        mensaje = "     ............... ****** DESCARGANDO EPG DEL CANAL: " + canalid + " | " + cadena + " FECHA: " + fechaEPG.strftime("%d-%m-%Y") + " ****** ..............."
        #print mensaje
        ficheroLog(pathRuta(), mensaje)
        #print
        
        #Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        html = BeautifulSoup(req.text, 'lxml')
    
        #Obtenemos body desde htm para poder capturar ('div',{'id':'container_parrilla_vacia'}), 
        bod = html.find('body')
        
        
         #Si obtenemos el div container_parrilla_vacia es que el Canal no tiene parrilla para la fecha o Canal no disponible
        #Por lo tanto, si no lo obtenemos, es que el Canal tiene parrilla para la fecha disponible 
        if not bod.find('div',{'id':'container_parrilla_vacia'}):
        
            #Obtenemos todos los Tags ul.
            uls = bod.find('ul',{'class':'fila_cadena'})
                                
            #Esta parte es para controlar que la parrilla empieza a las 08.00 de un dia y termina a las 08.00 del dia siguiente
            #Pero mantiene la misma fecha, tenemos que controlar los programas que empiezan antes de las 23.59 y terminan pasadas las 00.00,
            #y les ponemos la fecha correcta
            hocomp1 = time(21,30,00)
            hocomp2 = time(23,59,59)
            
            
            #Para cada Tags ul obtenemos los datos
            for parrilla in uls.find_all('li'):
                
                #Asterisco, no tienen la hora. Preguntamos si existe este Tag. Esta presente cuando el programa ya ha sido emitido o en determinados programas.
                asteris = parrilla.find('strong',{'class':'asterisco'})
                
                #Url ficha
                uf = parrilla.find('a', None)
                urlficha = uf.get('href', None)
                urlfichatext = uf.text
               
                                    
                #Cuando la url de la ficha tecnica viene mal
                if urlficha:
                    
                    if urlficha.find("=") >= 0:
                    
                        #Url de la Ficha Tecnica    
                        ficha = urlficha[int(urlficha.find("=")) + 1:]                   
                                            
                else:
                        
                    ficha = ""

                    
                #No lo incluimos en la parrilla. es el primero y viene con asterisco
                if asteris and contador == 0:
                    
                    pass
                                            
                #Para el resto de combinaciones de asteris y contador    
                else:
                                               
                    if (platform.system() == 'Windows'):
                    
                        locale = Locale("es","ES")
                     
                        fep = fechaEPG
                     
                        fepg = format_date(fep, "EEEE, d 'de' MMMM", locale='es_ES')
                        fepgg = str(fepg.encode('utf8'))
                     
                    else:
                     
                        fepgg = fechaEPG.strftime("%A, %d de %B").replace(", 0", ", ")

                    #Tenemos que buscar la hora en la ficha tecnica, porque las programaciones con * no tienen la hora en la parrilla
                    if asteris:
                                         
                        containerFicha = peticionURLFicha(ficha,urlDetalle2)
                        epiinssues = containerFicha.find_all('ul',{'class':'episodes_in_issues'})   
                        pases = containerFicha.find('ul',{'id':'pases'})
                        emisiondatebig = containerFicha.find('div',{'class':'emision_date big'})
                       
                                                         
                        if epiinssues:
                                                                                                
                           if not containerFicha.find('li',{'class':'noactive'}):
                               
                                for u in range(len(epiinssues)):
                            
                                    if epiinssues[u].find('li',{'class':'active'}):
                                        activeLi = epiinssues[u].find('li',{'class':'active'})
                                        break
                                    
                                activeLii = activeLi.find('li',{'class':'active'})
                                episodeactiveP = activeLii.find_all('p',{'class':'emision_date'})
                                
                                episodeCanalist = []
                                
                                for w in range(len(episodeactiveP)):
                                    
                                    canalNombre = str(canal[1])
                                    im = episodeactiveP[w].find('img')
                                    canalt = im.get('alt', None).encode('utf-8')
                                
                                    if canalNombre == canalt:
                                    
                                        episodeCanalist.append(episodeactiveP[w])
                                        
                                for p in range(len(episodeCanalist)):       
                                        
                                    epactiveP = episodeCanalist[p].text.replace('\n', "").replace('\t', "")
                                    epactivePP = epactiveP.split('-')
                                    epactivedia = str(epactivePP[0].encode('utf8')).rstrip()
                                                                       
                                    if epactivedia == fepgg:   
                                        
                                        horpd1 = epactivePP[1].strip().split(':')
                                        horpd2 = ultimahora.split(':')
                                        
                                        inthorpd1 = int(horpd1[0])
                                        inthorpd2 = int(horpd2[0])
                                        
                                        if inthorpd1 >= inthorpd2:
                                         
                                            hora = epactivePP[1].strip()
                                            break
                               
                        elif pases:
                            
                            #VAriable para controlar cuando una mismo programa semite mas de una vez al dia, al obtener las horas de los pases.
                            chivatopases = 0
                
                            pasesP = pases.find_all('p',{'class':'emision_date'})
                            
                            paseCanalist = []
                        
                            for w in range(len(pasesP)):
                                
                                canalNombre = str(canal[1].encode('utf-8'))
                                im = pasesP[w].find('img')
                                canalt = im.get('alt', None).encode('utf-8')
                                
                                if canalNombre == canalt:
                                    
                                    paseCanalist.append(pasesP[w])

                            for p in range(len(paseCanalist)):
                                
                                paseP = paseCanalist[p].text.replace('\n', "").replace('\t', "")
                                pasePP = paseP.split('-')
                                pasedia = str(pasePP[0].encode('utf8')).rstrip()
                                                                   
                                if pasedia == fepgg:
                                        
                                    horpd1 = pasePP[1].strip().split(':')
                                    horpd2 = ultimahora.split(':')
                                    
                                    inthorpd1 = int(horpd1[0])
                                    inthorpd2 = int(horpd2[0])
                                    
                                    if inthorpd1 >= inthorpd2:
                                                                                                                                 
                                        hora = pasePP[1].strip()
                                      
                                        break     
                                               
                                                                    
                        elif emisiondatebig:
                        
                            edbgP = emisiondatebig.find('p',{'class':'emision_proximo'})
                            edbgPP = edbgP.find('strong')
                            edbgPPP = edbgPP.text.replace('\n', "").replace('\t', "")
                            edbgPPPP = edbgPPP.split('-')
                                                                        
                            hora = edbgPPPP[1].strip()
                        
                        else:
                    
                            mensaje = "                        -- -- -- -- -- -- --         ERROR CAMBIO EN FICHAS TECNICAS MULTIPASES        -- -- -- -- -- -- --    "
                            print mensaje
                            ficheroLog(pathRuta(),mensaje) 
                        
                        #Cuando encontramos el primero y hemos obtenido la hora. Comprobamos si la ficha tecnica existe en la BD,sino, la insertamos.
                        #Antes que la parrilla, con esto evitamos tener que volver a consuntarla.
                        if hora:
                        
                            if ficha:
                                
                                rowFicha = buscarBDFicha(cursor,db,ficha,containerFicha)
                                                    
                                if not rowFicha:
                                
                                    insertarFichaTecnica(cursor,db,ficha, containerFicha)
                        
                    else: 
                                                                              
                        #Hora de inicio
                        h = parrilla.find('span')
                        hora = h.text
                     
                    #Si hemos obtenido hora. Para controlar los programas cuyo inicio es el dia siguiente aunque en la parrila vienen en el dia anterior.
                    if  hora and not hora == ultimahora:                                           
                                     
                        if chivato == 0:
                                                        
                            horc1 = hora.split(':')
                            horc2 = ultimahora.split(':')
                            inthorc1 = int(horc1[0])
                            inthorc2 = int(horc2[0])

                            if inthorc1 < 23 and inthorc1 < inthorc2 and fechaEPG <= (filist[len(filist) - 1]):

                                chivato += 1

                                fechaEPG = fechaEPG + timedelta(days=1)
                                
                        ###################################################        
                        if chivatoh < 1:
                        
                            #Variable con la hora de la parrilla en formato time
                            haux1 = datetime.strptime(hora + ":00", "%H:%M:%S").time()
                            dhaux1 = datetime.combine(fechaEPG, haux1)
                            
                            if dhaux1 >= dhaux2:
     
                                chivatoh = chivatoh + 1
                                
                        if ficha and chivatoh > 0:                         

                            #Titulo
                            tit = parrilla.find('strong')
                            titulo = tit.get('title',None)
                            
#                             if not asteris:
#                             
#                                 #Subtitulo
#                                 sub = parrilla.find('a',{'id':'subtitulo'})
#                                 
#                                 if sub.text.find("Episodio") < 0:
#                                     subtitulo = sub.text
#                                 else:
#                                     subtitulo = ""
                                                            
#                             #Imagen
#                             img = parrilla.find('a',{'class':'img_parrilla'})
#                             
#                             if img:
#                                                        
#                                 image = img.find('img')
#                                 imagen = "http://comunicacion.movistarplus.es" + image.get('src', None)
#                                 imagenlist.append(imagen)
#                                                               
#                                                         
#                             else:
#                                 
#                                 if (canalid =="A3" or canalid =="SEXTA" or canalid =="NEOX" or canalid =="NOVA"
#                                     or canalid =="MEGA" or canalid =="ATRESS"):
#                                     
#                                     busc = str(titulo.encode('utf-8')).replace("'","")
#                                     
#                                     buscar = "'%" + busc + "%'"
#                                     #cadena = "'" + str(titulo.encode('utf-8')) + "'"
#                                     
#                                     cursor.execute("SELECT * FROM ATRESMEDIA WHERE PROGRAMA LIKE "+ buscar)      
# 
#                                     rowATRESMEDIA = cursor.fetchone()
#                                     
#                                     if rowATRESMEDIA:
#                                     
#                                         imagen = rowATRESMEDIA[1]
#                                         imagenlist.append(imagen)
#                                         
#                                     else:
#                                         
#                                         imagenlist.append("")
#                                         
#                                 elif (canalid =="T5" or canalid =="C4" or canalid =="FDFIC" or canalid =="BOING"
#                                     or canalid =="ENERGY" or canalid =="BEMAD" or canalid =="DIVINI"):
#                                     
#                                     busc = str(titulo.encode('utf-8')).replace("'","")
#                                     
#                                     buscar = "'%" + busc + "%'"
#                                     #cadena = "'" + str(titulo.encode('utf-8')) + "'"
#                                     
#                                     cursor.execute("SELECT * FROM MEDIASET WHERE PROGRAMA LIKE "+ buscar)      
# 
#                                     rowMEDIASET = cursor.fetchone()
#                                     
#                                     if rowMEDIASET:
#                                     
#                                         imagen = rowMEDIASET[1]
#                                         imagenlist.append(imagen)
#                                         
#                                     else:
#                                         
#                                         imagenlist.append("")
#                                     
#                                 else:
#                                         
#                                     imagenlist.append("")
                                
                                
                            #Genero
                            gen = parrilla.find('span',{'class':'genero_parrilla'})
                            
                            if gen is None:
                         
                                genero = "Otros"
                                                      
                            else:
                    
                                genero = gen.text
                                 
                            generolist.append(genero)
                            
                            if(contador > 0):
                                
                                if (canalid =="CPPART" or canalid =="BELIGA" or canalid =="BELIG1" or canalid =="BELIG2"
                                    or canalid =="CHUEFA" or canalid =="BEMAX1") and fechaEPG > filist[len(filist) - 1]:
                                           
                                    hh = datetime.combine(filist[len(filist) - 1], hilist[len(hilist) - 1]) 
                                    hh= hh + timedelta(hours=2)
                                    fflist.append(hh.date())
                                    hflist.append(hh.time())                                         
                                        
                                else :
                                                                                
                                    fflist.append(fechaEPG)                                    
                                    hflist.append(datetime.strptime(hora + ":00", "%H:%M:%S").time())
                                                                             
                       
                            filist.append(fechaEPG)
                            #hilist.append(hora.encode('utf-8') + ":00")
                            hilist.append(datetime.strptime(hora + ":00", "%H:%M:%S").time())
                            titlist.append(titulo)
                            #sublist.append(subtitulo)
                            urlfichalist.append(urlficha.replace("." , "", 2))                
                            idlist.append(ficha)
                            
                            contador = contador + 1                             
                    #===================================================
                    # 
                    #         print "............................................................................................................................................." 
                    #         #mensaje = "hora: " + hora + " | fechaEPG: " + fechaEPG.strftime("%d-%m-%Y") + " | ficha: " + ficha + " | ultimaficha: " + ultimaficha + " | chivato: " + str(chivato) + " | chivatoh: " + str(chivatoh) + " | contador: " + str(contador)
                    #         mensaje = "hora: " + hora + " | fechaEPG: " + fechaEPG.strftime("%d-%m-%Y") + " | ficha: " + ficha + " | ultimaficha: " + ultimaficha
                    #         print mensaje
                    #         ficheroLog(pathRuta(), mensaje)
                    #         print "............................................................................................................................................." 
                    #===================================================
                                       
                            ultimaficha = ficha
                            ultimahora = hora
                    
                    else:
                        
                        #print "............................................................................................................................................." 
                        #mensaje = "hora: " + hora + " | fechaEPG: " + fechaEPG.strftime("%d-%m-%Y") + " | ficha: " + ficha + " | ultimaficha: " + ultimaficha + " | chivato: " + str(chivato) + " | chivatoh: " + str(chivatoh) + " | contador: " + str(contador)
                       # mensaje = "hora: " + hora + " | fechaEPG: " + fechaEPG.strftime("%d-%m-%Y") + " | ficha: " + ficha + " | ultimaficha: " + ultimaficha
                        #print mensaje
                        #ficheroLog(pathRuta(), mensaje)
                        #print "............................................................................................................................................."
                        
                        ultimaficha = ficha                                                                   
                        ultimahora = hora
                            
            
        #Canal sin parrilla para la fecha o Canal no disponible    
        else:

            vacio = bod.find('div',{'id':'mens'}).text 
            
            print                    
            print "        --------------------------------    CANAL SIN PARRILLA PARA LA FECHA: " + fechaEPG.strftime("%d-%m-%Y") + "  -----------------------------"
            print
            ficheroLog(pathRuta(),"        --------------------------------    CANAL SIN PARRILLA PARA LA FECHA: " + fechaEPG.strftime("%d-%m-%Y") + "  -----------------------------")
            print
            
            if not (canalid =="CPPART" or canalid =="BELIGA" or canalid =="BELIG1" or canalid =="BELIG2"
                    or canalid =="CHUEFA" or canalid =="BEMAX1"):
                break  

    #Bucle para    
    if(contador > 0):
        
        if (canalid =="CPPART" or canalid =="BELIGA" or canalid =="BELIG1" or canalid =="BELIG2"
            or canalid =="CHUEFA" or canalid =="BEMAX1") and fechaEPG > filist[len(filist) - 1]:
                   
            hh = datetime.combine(filist[len(filist) - 1], hilist[len(hilist) - 1]) 
            hh= hh + timedelta(hours=2)
            fflist.append(hh.date())
            hflist.append(hh.time())                                         
                
        else :
                                                        
            fflist.append(fechaEPG)                                    
            hflist.append(datetime.strptime("08:00:00", "%H:%M:%S").time())
    
    

############################################################
############################################################
#Funcion conectar con URL metodo GET,obtener una Ficha Tecnica y extraer los datos.
def peticionURLFicha(ficha,urlDetalle2):
    
    urlDetalle2 = urlDetalle2 + ficha
    reqficha = peticionURLGet(urlDetalle2, ficha)
            
    statusCodeFicha = reqficha.status_code  
    
    #Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(reqficha.text, 'lxml')
    
    #Obtenemos el div containerFicha.
    container = html.find('div',{'id':'containerFicha'})   
            
    return container
############################################################
#Funcion para buscar en la BD una Ficha Tecnica
def buscarBDFicha(cursor, db, fichatecnica, containerFicha):
    
    #Comnprobamos si la ficha tecnica ya existe en la BD,para no volverla a descargar
    cursor.execute("SELECT * FROM FICHA_TECNICA WHERE FICHA=? ORDER BY ROWID ASC", (fichatecnica,))
    #cursor.execute("SELECT * FROM FICHA_TECNICA WHERE FICHA=1281469 ORDER BY ROWID ASC")
    #Comnprobamos si la ficha tecnica ya existe en la BD,para no volverla a descargar
    #cursor.execute("SELECT * FROM FICHA_TECNICA WHERE FICHA=? ORDER BY ROWID ASC", (ficha[0],))
    
    rowFicha = cursor.fetchone()    

    if rowFicha:
        
        if not rowFicha[8]:
            
            if containerFicha:
                
                imgfich = containerFicha.find('img',{'id':'imagenPrograma'})
            
                if imgfich:
                    
                    urlimgfic = imgfich.get('src', None)
                    
                    if urlimgfic.find("http://") >= 0:
                    
                        imagenficha = urlimgfic  
                        
                    else:
                        
                        imagenficha = "http://comunicacion.movistarplus.es" + imgfich.get('src', None)                               
                                            
                else:
                    
                    imagenficha =""
                    
                if imagenficha <> "":
                    
                    cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagenficha,ficha))
            
                    db.commit()
    imgfich = ""    
    imagenficha =""
    
    return rowFicha 
############################################################
#Funcion para insertar Ficha Tecnica BD
def insertarFichaTecnica(cursor,db,ficha,containerFicha):
    
    fichaargumento = containerFicha.find('div',{'id':'argumento'})
                                                    
    argum = fichaargumento.text.replace('\n', "").replace('\t', "").replace('ARGUMENTO', "").replace('Argumento', "")
    
    argum = argum.strip()
    
                    
    fichatecnica = containerFicha.find('div',{'class':'ficha_tecnica'})

    fip = fichatecnica.find('p',{'class':'age_allowed p_nr_18'})
    
    imgfich = containerFicha.find('img',{'id':'imagenPrograma'})
    
    if imgfich:
        
        urlimgfic = imgfich.get('src', None)
        
        if urlimgfic.find("http://") >= 0:
        
            imagenficha = urlimgfic  
            
        else:
            
            imagenficha = "http://comunicacion.movistarplus.es" + imgfich.get('src', None)                               
                                
    else:
        
        imagenficha =""
    
    if fip is None:
        
        calificacion = "Sin calificar."
        
    else:
    
        calificacion = fip.text.lower().capitalize()+ "."
        if calificacion == "Sin clasificar.":
            calificacion.replace("Sin clasificar.","Sin calificar.")
            
        
    dllist = []
    tupmgenero = ()
    generolist = []
    paislist = []
    anyolist = [] 
    
    dll = fichatecnica.find_all('dl')
    
    #temporada = ""
    #episodio = ""
    duracion = ""
    genero = ""
    pais = ""
    anyo = ""
    descripcion = ""
    titulorig = ""
    idiomas = ""
    subtitulos = ""
    #tipodepase = ""
    codigo = 0
    otros = ""
    #director = ""
    #actor = ""

        
    for dl in range(len(dll)):
            
        fidl = dll[dl]

        for pepon in list(zip(fidl.find_all('dt'), fidl.find_all('dd'))): 
            
                  
            dt = pepon[0].text.capitalize()
                    
            #if(dt == "Temporada:"):
                
                #temporada = "T.(" + pepon[1].text + ")"
                
            #elif(dt == "Episodio:"):
                
                #episodio = "Ep.(" + pepon[1].text + ")"
                
            if(dt == u'Duración:'):
                
                durac = pepon[1].text
                duracion = durac.replace("hora y","h.").replace("minutos","m.").replace("horas y","h.").replace(" ","")

                
            elif (dt == u'Nacionalidad:'):
                
                pais = pais + pepon[1].text
                
            elif(dt == u'Año:'):
                 
                pais = pais + '(' + pepon[1].text + ')'

            elif(dt == u'Título original:'):
                                  
                titulorig = pepon[1].text
                
            elif(dt == u'Versiones:'):
                                  
                idiomas = pepon[1].text
                
            #elif(dt == u'Subtítulos:'):
                                  
                #subtitulos = pepon[1].text
                
#             elif(dt == u'Tipo de pase:'):
#                                   
#                 tipodepase = pepon[1].text
                
#             elif(dt == u'Director:'):
#                                   
#                 director = pepon[1].text
#                 
#             elif(dt == u'Actor:'):
#                                   
#                 actor = pepon[1].text
                                
            elif(dt == u'Género:'):
                
                genero = pepon[1].text  
         
                try:
                    
                    cursor.execute("SELECT * FROM CATEGORIAS_MOVISTAR WHERE CATEGORIA=? ORDER BY ROWID ASC", (genero,))

                    generosrow = cursor.fetchone()
                    
                    if not generosrow:
                        
                        g = pepon[1].text                         
                        
                        gg = g.split("/")
                        
                        buscar = gg[0].strip()
                                                                        
                        for desct in range(len(descatgtvh)):
                            
                            encontrar = str(descatgtvh[desct],)
                             
                            if buscar.encode('utf-8') == encontrar:
                                                             
                                 codigo = idcatgtvh[desct]
                                                                
                                 break
                                                                               
                        #codigo = '61' 
                                              
                        tupmgenero = (g,codigo)
                            
                        cursor.execute('''INSERT INTO CATEGORIAS_MOVISTAR(CATEGORIA, ID_CATEG_TVHEADEND) 
                            VALUES(?,?)''',tupmgenero)
                    
                    else:
                        
                        codigo = generosrow[2]
                        

                except sqlite3.IntegrityError:
        
                    pass
    
            elif not (dt == u'Subtítulos:' or dt == "Temporada:" or dt == "Episodio:"
                      or dt == u'Versiones:' or dt == u'Tipo de pase:'):
                 
                if pepon[0].text:
                     
                    if len(dllist) == 0:                    
                        dllist.append("|")   
                         
                                                  
                    dllist.append(pepon[0].text.capitalize())
                    dllist.append(pepon[1].text + ".") 
        
    for d in range(len(dllist)):
    
        otros = otros + " " + dllist[d]
       
    if not duracion: duracion = "" 
    
    duracio = ""

    for du in range(len(duracion)):
        
        duracio = duracio + " " + duracion[du]
                      
   
    tupmt = (ficha,argum,calificacion,duracio,codigo, genero,pais,otros,imagenficha,titulorig,idiomas) 
                         
    
    try:
        
        cursor.execute('''INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION, DURACION, ID_CATEG_TVHEADEND,GENERO,PAIS,OTROS,
            IMAGENFICHA,TITULO_ORIGINAL,IDIOMAS) 
            VALUES(?,?,?,?,?,?,?,?,?,?,?)''',tupmt)
        
        db.commit()
        
        # cursor.execute("INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION ,DESCRIPCION) VALUES('"  fich  "', '"  argum  "', '"  fip.text  "', "  descripcion  "')")

    except sqlite3.IntegrityError:

        pass 
    
############################################################
def  pipfuncion():
    
    try:
        
        import os, sys, platform, errno, commands
        from os.path import isfile 
        
    except ImportError as e:
        
        mensaje = "Ud. no tiene instalado el modulo: {0}".format(e.message[16:])
        print mensaje
        
    os.system("wget -c -q https://bootstrap.pypa.io/get-pip.py")
                
    piplisti = ["pip","Babel","beautifulsoup4", "BeautifulSoup", "bs4","lxml","pytz","requests","tzlocal","html5lib"]
    piplist = []
    
    
    try:
    
        os.system("python get-pip.py")
        
        print
        mensaje = "          ------------------------------------------------------------------------------------------------------------"
        print mensaje
        print
        ficheroLog(pathRuta(),mensaje)
        
    except:
        
        print
        mensaje = "\t\t\t\tERROR EN INSTALACION DE PIP"
        ficheroLog(pathRuta(),mensaje)
        print mensaje
        barramenu()
        print
        ficheroLog(pathRuta(),mensaje)
        sys.exit(1)
            
    import pip
       
    menucabecera()
        
    filepip = pathRuta() + '/pip.txt'
    commands.getoutput('rm ' + filepip)
    commands.getoutput('pip list >> pip.txt')
    
    piplist  = []
    
    pipi = open(filepip, 'r')
    
    numpipi = pipi.readlines()
    
    pipi.close()
    
    for npi in numpipi:
        
        ln = npi.split(' ')
        rln = ln[0]
        piplist.append(rln)
    
        
#     for package in pip.get_installed_distributions():
#             #print(package.location) # you can exclude packages that's in /usr/XXX
#             piplist.append(package.key)
           
    k = 0       
    
    while k in range(len(piplisti)):
            
        if not (piplisti[k]) in piplist:
            
            mensaje = "\t\tINSTALANDO -- " + piplisti[k]
            ficheroLog(pathRuta(),mensaje)
                        
            try:
                
                commands.getoutput("pip install " + piplisti[k])
                
                print mensaje
                mensaje = "\t\t-------------------------------------------------------------"
                print mensaje
                print
                ficheroLog(pathRuta(),mensaje)
                
            except:
                
                mensaje = "ERROR EN INSTALACION DE LIBRERIA" + piplisti[k]
                ficheroLog(pathRuta(),mensaje)
                print mensaje
                barramenu(0)
                print
                ficheroLog(pathRuta(),mensaje)
                sys.exit(1)
                        
        k = k + 1
############################################################
def menucabecera(): 
    
    print 
    mensaje = "\t#############################################################################"
    print mensaje
    print
    if contmenucabecera == 0: ficheroLog(pathRuta(),mensaje)
       
    mensaje = "\t  ############    INSTALACION -- G U I N I G U A D A -- EPG    ############"
    print mensaje
    if contmenucabecera == 0: ficheroLog(pathRuta(),mensaje)
    print
    
    mensaje = "\t\t    -------------     %s --  %s  --------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S"))
    print mensaje
    if contmenucabecera == 0: ficheroLog(pathRuta(),mensaje)
    print
############################################################
def barramenu(contbarramenu):
    
    mensaje = "\t#############################################################################"
    print mensaje 
    if contbarramenu == 0: ficheroLog(pathRuta(),mensaje)
    print

############################################################

############################################################
#Variables Globales

# URLs para obtener los datos
urlParrilla="http://www.movistarplus.es/guiamovil"
urlDetalle="http://www.movistarplus.es/ficha/"
urlParrilla2="http://comunicacion.movistarplus.es/guiaProgramacion/index"
urlDetalle2="http://comunicacion.movistarplus.es/programa/ficha?nf="
statusCodeFicha = 0
containerFicha = ""

# URLs para obtener los datos
urlImgFilmAf="http://www.filmaffinity.com/es/search.php?stext="
urlImgFilmAfBA="http://www.filmaffinity.com/es/advsearch.php?stext="
titul = ""
statusCodeFicha = 0
containerFicha = "" 
contmenucabecera = 0
contmenudatos = 0
contbarramenu = 0
############################################################
#Lista de equivalencias para asignar codigo de Tvheadend a categorias Movistar
descatgtvh =('Infantil','Juvenil','Cocina','Cortometraje','Series','Cine','Telefilme','Film','Tiempo','Meteorología','Información','Informativo','Noticias','Entretenimiento','Concursos','Juegos','Futbol','Fútbol','Deportes','Música',
            'Musica','Naturaleza','Caza','Pesca','Ciencia','Documentales','Cultura','Cultural','Toros','Ocio y Aficiones','Otros','Sin clasificar')
idcatgtvh =('28','28','66','47','1','1','1','1','11','11','10','10','10','50','15','15','22','22','19','34',
            '34','54','54','54','53','13','40','40','40','61','61','61')
#------------------------------------------ print len(idcatgtvh),len(descatgtvh)
        
############################################################
#Comprobamos que estan instaladas las librerias necesarias

try:
        
    import pip
        
except ImportError as e:
        
    pipfuncion()
    
try:
    
    try:
            
        #Importamos las librerias
        from bs4 import BeautifulSoup
        from os.path import isfile    
        from datetime import datetime, time, timedelta, date
        from babel import Locale
        from babel.dates import format_date, format_datetime, format_time
              
        import os, sys, platform, errno, requests, sqlite3, html5lib
        import time as t
        import tzlocal, pytz, locale, unicodedata
        import re
        import commands   
    
    except ImportError as e:
      
        pipfuncion()

    #Copiamos fichero log anterior para no borrarlo
    file = pathRuta() + '/GUINIGUADA-EPG.log'
    filer = pathRuta() + "/GUINIGUADA-EPG.old.log"
    
    if isfile(file):
        
        os.rename(file,filer)
 
    #Mensaje que estan instaladas las librerias necesarias
    #ficheroLog(pathRuta(),"Import: OK\n")

##############################################################################################
        
    #Informacion sobre el sistema
    so() 
    
    #Zona Local UTC Host
    zona_local = tzlocal.get_localzone()
    ficheroLog(pathRuta(),"Zona Local UTC: %s" % zona_local)
    
    #Zona Local UTC URL Descarga
    zona_local_url = pytz.timezone("Europe/Madrid")                      
    ficheroLog(pathRuta(),"Zona Local URL UTC: %s" % zona_local_url)
    
    #locales segun el SO
    if (platform.system() == 'Linux'):
            
        locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
                
    elif (platform.system() == 'Windows'):

        locale = Locale("es","ES")
    
    #Fecha actual en formatado date
    hoy = datetime.now()
    #print
    mensaje = "          ############################################################################################################"
    #print mensaje
    ficheroLog(pathRuta(),mensaje)
    mensaje = "          ##########################                   G U I N I G U A D A -- EPG              #######################"
    ficheroLog(pathRuta(),mensaje)
    mensaje = "          ############################################################################################################"
    ficheroLog(pathRuta(),mensaje)
    #print mensaje
    #print
    mensaje = "          --------------------------------   Inicio Descarga: %s -- %s  --------------------------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S"))
    #print mensaje
    #print
    ficheroLog(pathRuta(),mensaje)
       
    try:
        
        #Conexion a la Base de Datos
        db = sqlite3.connect(pathRuta() + '/guiniguadamv.sqlite') 
        db.text_factory = str       
        #Creamos cursor BD
        cursor = db.cursor()        
        #Compactamos la BD
        cursor.execute("VACUUM")
        
        #Comprobamos si existe el archivo canalesmovistar.txt y actualizamos la descarga activa
        if isfile(pathRuta() + '/canalesmovistar.txt'):
                    
            canalesmov = open(pathRuta() + '/canalesmovistar.txt', 'r')
            
            numcanalesmov = canalesmov.readlines()
            
            canalesmov.close()
                  
            for l in numcanalesmov:
                
                cade = l.replace('\n','')
        
                cadena = cade.split(',')
                         
                cursor.execute('UPDATE CANALES SET DESCARGA_ACTIVA=? WHERE ID_CANAL=?',(cadena[2],cadena[0],))

                db.commit()
        
        
        #Obtenemos de la Tabla Canales los que tienen Descarga Activa=1
        canalesRows = obtenerCanalesActivos(cursor)
        
        #Borramos la parrilla y las fichas que no repiten.
        borrarParrilla(cursor, db)
        
        #Bucle para Descargar EPG de cada canal
        for canal in canalesRows:
              
            #################
            #Creamos una lista para cada elemento de la parrilla
            idlist = []
            filist = []
            fflist = []
            hilist = []
            hflist = []
            titlist = []
            urlfichalist = []                
            generolist = []
            parrillalist = []
            
            chivf1 = 0
            

            #Canalid y Cadena en formato String
            canalid = str(canal[0],)
            cadena = str(canal[1],)
            
            statusCode = 0
                        
            statusCode = fuente1(canalid, cadena, idlist,filist,hilist,fflist,hflist,titlist,generolist,urlfichalist,statusCode)
                                    
            if statusCode == 404:
                
                fuente2(canalid, cadena, idlist,filist,hilist,fflist,hflist,titlist,generolist,urlfichalist,statusCode)
                
                chivf1 = 2
            else:
                
                chivf1 = 1   
                        
            #print len(idlist), len(filist), len(hilist), len(fflist), len(hflist), len(titlist), len(generolist), len(urlfichalist)
            
             #Preparamos los datos para insertar en BD
            #for i in range(len(idlist)):
                
                #print idlist[i],filist[i],hilist[i],fflist[i],hflist[i],titlist[i],generolist[i],urlfichalist[i]
                
            #print contador, len(idlist), len(filist), len(hilist), len(fflist), len(hflist), len(titlist), len(generolist), len(urlfichalist)
            
            #Preparamos los datos para insertar en BD
            for i in range(len(filist)): 
                
                if not hilist[i] == hflist[i]:
                    
                    #print i,hilist[i].strftime("%H:%M:%S"),hflist[i].strftime("%H:%M:%S"),filist[i].strftime("%Y-%m-%d"),fflist[i].strftime("%Y-%m-%d")
    
                    parrillalist.append(idlist[i])
                    
                    parrillalist.append(canalid)
                    parrillalist.append(cadena)            
                     
                    parrillalist.append(filist[i].strftime("%Y-%m-%d"))
                    parrillalist.append(hilist[i].strftime("%H:%M:%S"))   
 
                    tupmi = datetime.combine(filist[i], hilist[i])
                    zli = zona_local_url.localize(tupmi)
                    utci = zli.strftime('%z')
                    parrillalist.append(utci)          
                    
                    parrillalist.append(fflist[i].strftime("%Y-%m-%d"))
                    parrillalist.append(hflist[i].strftime("%H:%M:%S"))  
                    
                    #Obtenemos UTC para  FF-HF                              
                    tupmf = datetime.combine(fflist[i], hflist[i])              
                    zlf = zona_local_url.localize(tupmf)                    
                    utcf = zlf.strftime('%z')                    
                    parrillalist.append(utcf)                             
                    
                    parrillalist.append(urlfichalist[i])
                                                          
                    parrillalist.append(titlist[i])
  
                    parrillalist.append(generolist[i])
                    
                #else:
                    #print i,hilist[i].strftime("%H:%M:%S"),hflist[i].strftime("%H:%M:%S"),filist[i].strftime("%Y-%m-%d"),fflist[i].strftime("%Y-%m-%d")   
                    
            #Insertamos los datos en BD Parrilla
            N = 12
            sparrilist = [parrillalist[n:n+N] for n in range(0, len(parrillalist), N)]
            
            for i in range(len(sparrilist)):                    
                
            
                try:
    
                    cursor.execute('''INSERT INTO PARRILLA(FICHA, ID_CANAL, NOMBRE_CANAL ,FECHAINICIO ,HORAINICIO,UTCI, FECHAFINAL, HORAFINAL, UTCF, URLFICHA, TITULO, GENERO) 
                                      VALUES(?,?,?,?,?,?,?,?,?,?,?,?)''', sparrilist[i])
                    
                    db.commit()
                    
                except sqlite3.IntegrityError:
        
                    pass 
                        
            #####################################
            #Obtenemos las fichas para cada entrada en la parrilla          
            cursor.execute("SELECT * FROM PARRILLA WHERE ID_CANAL=? ORDER BY ROWID ASC", (canalid,))        
        
            parricanallist = cursor.fetchall()
            
            # Si obtenemos datos    
            if len(parricanallist) > 0:  
                
                #print
                mensaje = "     ............... ******     OBTENIENDO FICHAS TECNICAS DEL CANAL: " + canalid + " | " + cadena + "     ****** ..............."
                #print mensaje
                #print
                ficheroLog(pathRuta(), mensaje) 
                mensaje = "          ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                #print mensaje
                #print
                ficheroLog(pathRuta(), mensaje)  

                
                #Obtenemos la Ficha Tecnica de cada parrilla.
                for parrilla in parricanallist:          
                    
                    ficha = str(parrilla[0].encode('utf8'))
                    
                    #Comnprobamos si la ficha tecnica ya existe en la BD,para no volverla a descargar
                    cursor.execute("SELECT * FROM FICHA_TECNICA WHERE FICHA=? ORDER BY ROWID ASC", (ficha,))
                                      
                    rowFicha = cursor.fetchone()
                    
                    if not rowFicha and chivf1 == 1:
                
                        url = str(parrilla[9].encode('utf8'))
                        req = peticionURLGet(url, ficha)
                        statusCode = req.status_code
                        
                        if statusCode == 200:
                       
                            html = BeautifulSoup(req.text,'lxml')
                                                            
                            
                            #Obtenemos body desde htm para poder capturar ('div',{'id':'container_parrilla_vacia'}), 
                            bod = html.find('body')
                        
                            codigo = 0
                            
                            pargume = ""
                            califi = ""
                            duraci = ""
                            codigo = ""
                            pgenre = ""
                            ppaisa = ""
                            otros = ""
                            imgficha = ""
                            pgamm = ""
                            pidioma = ""
                            
                       
                            diveeinfo = bod.find('div',{'class':'ee-info'})
                            #Imagen
                            if  diveeinfo.find('img'):
                                                   
                                imgcover = diveeinfo.find('img')
                                imgficha = imgcover.get('src', None)
                                
                                #print imgficha
                                
                            #Duracion
                            durac = diveeinfo.find('span',{'class':'time'})
                            duraci = durac.text
                            
                            #print duraci
                            
                            #Argumento
                            divshowcontent = bod.find('div',{'class':'show-content'})
                            pargum = divshowcontent.find_all('p')
                            
                            pargume = ""
                            
                            for parg in pargum:
                                
                                pa = str(parg.text.encode('utf8'))
                                
                                if not pa == "Ver más": 
                                
                                    pargume = pargume + pa.replace('\n', "").replace('\t', "")
                                
                            #print pargume
                            
                            #HD y VO
                            diveeinfo2 = bod.find('div',{'class':'ee-info-2'})
                            
                            if  diveeinfo2.find('ul',{'class':'list-info-movie'}):
                                
                                ullim = diveeinfo2.find('ul',{'class':'list-info-movie'})
                                
                                lim = ullim.find_all('li')
                                
                                for li in lim:                           
                                
                                    imglim = li.find('img')
                                    imglima = imglim.get('alt', None)
                                    
                                    if imglima == "Disponible en HD":
                                        
                                        imglima = "Disponible HD"
                                        
                                    else:
                                        
                                        imglima = "Disponible V.O."
                                   
                                    #print imglima
                                    
                                    
                            #Genero
                            divgidesk = diveeinfo2.find('div',{'class':'gi desk-one-third'})                        
                            
                            if divgidesk.find('p',{'itemprop':'genre'}):
                                
                                pgenre = diveeinfo2.find('p',{'itemprop':'genre'})
                                pg = str(pgenre.text.encode('utf8'))
                                #print pg
                                                            
                                #if ficha == '52167751':
                                    
                                   # print
                                
                                try:
                        
                                    cursor.execute("SELECT * FROM CATEGORIAS_MOVISTAR WHERE CATEGORIA=? ORDER BY ROWID ASC", (pgenre.text,))
                
                                    generosrow = cursor.fetchone()
                                    
                                    if not generosrow:        
                                        
                                        tupmgenero = ()         
                                        
                                        gg = pg.split("/")
                                        
                                        buscar = gg[0].strip()
                                                                                        
                                        for desct in range(len(descatgtvh)):
                                            
                                            encontrar = str(descatgtvh[desct],)
                                             
                                            if buscar.encode('utf-8') == encontrar:
                                                                             
                                                 codigo = idcatgtvh[desct]
                                                                                
                                                 break
                                                                                               
                                        #codigo = '61' 
                                                              
                                        tupmgenero = (pgenre.text,codigo)
                                            
                                        cursor.execute('''INSERT INTO CATEGORIAS_MOVISTAR(CATEGORIA, ID_CATEG_TVHEADEND) 
                                            VALUES(?,?)''',tupmgenero)
                                        
                                        db.commit()
                                    
                                    else:
                                        
                                        codigo = generosrow[2]
                                        
                
                                except sqlite3.IntegrityError:
                        
                                    pass
                                
                                except sqlite3.OperationalError as e:
                
                                    mensaje = "OperationalError: " + e.args[0]
                                    ficheroLog(pathRuta(), mensaje)
                                    #print "OperationalError: " , e    
                                
                                except sqlite3.Error as e:
                                
                                    ficheroLog(pathRuta(),"Error %s:" % e.args[0])    
                                    #print "Error %s:" % e.args[0]
                                    sys.exit(1)
                                                            
                            #Titulo original    
                            cadena4 = "Cine"
                            cadena5 = "Cine / Programa"
                                
                            if cadena4 in pg and not cadena5 in pg:
                                
                                if bod.find('div',{'class':'title-especial'}):
                                    
                                    titlespec = bod.find('div',{'class':'title-especial'})
                                    
                                    if titlespec.find('p',{'class':'h-gamma'}):
                                        
                                        pgamma = titlespec.find('p',{'class':'h-gamma'})
                                        pgamm = pgamma.text
                                        #print "Título Original: " + str(pgamm)
                                        
                                        
                            #Pais y Año     
                            if divgidesk.find('p',{'itemprop':'datePublished'}):
                                
                                ppaisano = diveeinfo2.find('p',{'itemprop':'datePublished'})
                                ppaisa = ppaisano.text
                                #print ppaisa                    
                            
                            #Idiomas y Subtitulos
                            if divgidesk.find('p',{'itemprop':None}): 
                                
                                pdivgidesk = divgidesk.find('p',{'itemprop':None})
                            
                                pidioma = str(pdivgidesk.text.encode('utf8'))
                                
                                pidioma = pidioma.lstrip()
                            
                                #print pidioma
                            
                            #Calificacion
                            if diveeinfo2.find('div',{'class':'moral'}):
                                
                                divmoral = diveeinfo2.find('div',{'class':'moral'})   
                                divm = divmoral.find('img')
                                divmo = divm.get('alt', None)
                                califi = str(divmo.encode('utf8'))
                                califi = califi.replace('No recomendado para','NR').replace('Apto para todos los públicos','TP').replace('años','a.')
                                califi = califi.replace('siete','7').replace('doce','12').replace('dieciséis','16').replace('dieciocho','18')
                                #print califi
                            
                            if not califi:
                                califi = "Sin calificar."
                           
                            #Director, Reparto y Otros
                            if bod.find('section',{'class':'g brick-content'}):
                                
                                divgilaponeh = bod.find('section',{'class':'g brick-content'})
                                
                                divgilapone = divgilaponeh.find_all('div',{'class':'gi lap-one-half'})
                                
                                for divgla in divgilapone:
                                    
                                    h3tec = divgla.find('h3',{'class':'heading'})
                                    
                                    try:
                                        
                                        if h3tec.text:
                                            
                                            h3text = str(h3tec.text.encode('utf8'))
                                            h3text = h3text.rstrip()
                                            ptec = divgla.find('p',None)
                                            ptectext = str(ptec.text.encode('utf8'))
                                            ptectext = ptectext.lstrip()
                                            ptectext = ptectext.rstrip()
                                            
                                            cadenatext = h3text + ":" + ptectext + "."
                                    
                                            #print cadenatext
                                            
                                    except:
                                        
                                        continue  
                                    
                                    otros = otros +  cadenatext                         
              
                           # else:
                                
                                #print "No tiene datos tecnicos"
                                
                                
                            tupmt = (ficha,pargume,califi,duraci,codigo,pgenre.text,ppaisa,otros,imgficha,pgamm,pidioma) 
                             
        
                            try:
                                
                                cursor.execute('''INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION, DURACION, ID_CATEG_TVHEADEND,GENERO,PAIS,
                                                                            OTROS,IMAGENFICHA,TITULO_ORIGINAL,IDIOMAS) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',tupmt)
                                
                                db.commit()
                                                
                            except sqlite3.IntegrityError:
                        
                                pass     
                            
                            
                    elif not rowFicha and chivf1 == 2:
                         
                        containerFicha = peticionURLFicha(ficha,urlDetalle2)
                        
                        if containerFicha:
                            
                            insertarFichaTecnica(cursor, db,ficha,containerFicha)
                            
                            containerFicha =""
                        
                        #Si tiene ficha pero no podemos obtenerla. Insertamos una ficha con los datos de la parrilla    
                        else:
                            
                            argum = "Ficha Tecnica sin datos"
                            temporada = ""
                            episodio = ""
                            duracion = ""
                            genero = "Otros / Otros"
                            pais = ""
                            anyo = ""
                            otros = ""
                            titulorig = ""
                            versiones = ""
                            subtitulos = ""
                            tipodepase = ""
                            codigo = 61
                            calificacion = "Sin calificar"
                            imagenficha = ""
                            director = ""
                            actor = ""
                            
                            tupmt = (ficha,argum,calificacion,temporada,episodio,duracion,codigo, genero,pais,anyo,otros,imagenficha,titulorig,versiones,subtitulos,tipodepase,director,actor) 
                         
    
                            try:
                                
                                cursor.execute('''INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION, TEMPORADA, EPISODIO, DURACION, ID_CATEG_TVHEADEND,GENERO,PAIS,
                                    ANYO,OTROS,IMAGENFICHA,TITULO_ORIGINAL,VERSIONES,SUBTITULOS,TIPODEPASE,DIRECTOR,ACTOR) 
                                    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''',tupmt)
                                
                                db.commit()
                        
                            except sqlite3.IntegrityError:
                        
                                pass 
                            
                            argum = ""
                            temporada = ""
                            episodio = ""
                            duracion = ""
                            genero = ""
                            pais = ""
                            anyo = ""
                            otros = "" 
                            titulorig = ""
                            versiones = ""
                            subtitulos = ""
                            tipodepase = ""
                            codigo = 0
                            calificacion = ""
                            imagenficha =""
                            director = ""
                            actor = ""
                            containerFicha =""
                                   
                mensaje = "          ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
                #print mensaje
                #print
                ficheroLog(pathRuta(), mensaje)
                
        
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. ****************  GENERANDO FICHAS TECNICAS ~ PARRILLA SIN FICHA ~ BD  ************** ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
    
        #Buscamos las parrillas sin ficha e intentamos crearlas con datos de otros canales.
        cursor.execute("SELECT * FROM PARRILLASINFICHAS_GROUPTITULO")
        
        rowsParSFGROUPTITULO = cursor.fetchall()
    
        ultimogrouptit = ""
        buscar = ""
    
        if rowsParSFGROUPTITULO:
            
            v = 0
            
            #salto = 0
            
            while v < len(rowsParSFGROUPTITULO):
                
                #print  '.',              
                #t.sleep(0.1)  
                #sys.stdout.flush()
                #salto = salto + 1
                #if salto > 75:
                    #print '\n'
                    #salto = 0
                          
                chivatoficha = 0
               
                z = 0
        
                try:                                
                    
                    cursor.execute("SELECT * FROM PARRILLA WHERE TITULO=? ORDER BY ROWID ASC",(rowsParSFGROUPTITULO[v][0],))
                    
                    rowsParrillaTitulo = cursor.fetchall()
                    
                    if rowsParrillaTitulo:
                        
                        for w in rowsParrillaTitulo:
                            
                            pargume = ""
                            califi = ""
                            duraci = ""
                            codigo = ""
                            pgenre = ""
                            ppaisa = ""
                            otros = ""
                            imgficha = ""
                            pgamm = ""
                            pidioma = ""
                            
                            cursor.execute("SELECT * FROM FICHA_TECNICA WHERE FICHA=?",(w[0],))
                            
                            rowFicha = cursor.fetchall()
                            
                            if rowFicha:
                                
                                cursor.execute("SELECT * FROM PARIILASINFICHA WHERE TITULO=? ORDER BY ROWID ASC",(rowsParSFGROUPTITULO[v][0],))
                                
                                rowsParSF = cursor.fetchall()
                                
                                rowParSF = rowsParSF[0]
                                
                                for r in rowsParSF:
                                    
                                    fica = r[0]
                                    pargume = rowFicha[0][1]
                                    califi = rowFicha[0][2]
                                    duraci = rowFicha[0][3]
                                    codigo = rowFicha[0][4]
                                    pgenre = rowFicha[0][5]
                                    ppaisa = rowFicha[0][6]
                                    otros = rowFicha[0][7]
                                    imgficha = rowFicha[0][8]
                                    pgamm = rowFicha[0][9]
                                    pidioma = rowFicha[0][10]
                                    
                                    tupmt = (fica,pargume,califi,duraci,codigo,pgenre,ppaisa,otros,imgficha,pgamm,pidioma)
                                    
                                    cursor.execute('''INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION, DURACION, ID_CATEG_TVHEADEND,GENERO,PAIS,
                                                                            OTROS,IMAGENFICHA,TITULO_ORIGINAL,IDIOMAS) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',tupmt)
                                
                                    db.commit()
        
                                    fica = ""
                                    pargume = ""
                                    califi = ""
                                    duraci = ""
                                    codigo = ""
                                    pgenre = ""
                                    ppaisa = ""
                                    otros = ""
                                    imgficha = ""
                                    pgamm = ""
                                    pidioma = ""
                                    chivatoficha = 1
                                    
                                del rowsParSFGROUPTITULO[z] 
                                    
                                if len(rowsParSFGROUPTITULO) == 0:
                                    break
                                                         
                            else:
                            
                                pargume = ""
                                califi = ""
                                duraci = ""
                                codigo = ""
                                pgenre = ""
                                ppaisa = ""
                                otros = ""
                                imgficha = ""
                                pgamm = ""
                                pidioma = ""
                                
                                busc = str(w[10],).split(' (' )
                                
                                buscar = "'%" + busc[0] + "%'"
                                                                
                                cursor.execute("SELECT * FROM FICHA_TECNICA_PARRSINFICHA WHERE FICHA LIKE " + buscar)
                                
                                rrowFicha = cursor.fetchall()
                                
                                if rrowFicha:
                                
                                    cursor.execute("SELECT * FROM PARIILASINFICHA WHERE TITULO LIKE " + buscar)
                                                                      
                                    rrowsParSF = cursor.fetchall()
                                                                               
                                    for rrrowParSF in rrowsParSF:
                                        
                                        fica = rrrowParSF[0]
                                        pargume = rrowFicha[0][1]
                                        califi = rrowFicha[0][2]
                                        duraci = rrowFicha[0][3]
                                        codigo = rrowFicha[0][4]
                                        pgenre = rrowFicha[0][5]
                                        ppaisa = rrowFicha[0][6]
                                        otros = rrowFicha[0][7]
                                        imgficha = rrowFicha[0][8]
                                        pgamm = rrowFicha[0][9]
                                        pidioma = rrowFicha[0][10]
                                        
                                        tupmt = (fica,pargume,califi,duraci,codigo,pgenre,ppaisa,otros,imgficha,pgamm,pidioma)
                                        
                                        cursor.execute('''INSERT INTO FICHA_TECNICA(FICHA, ARGUMENTO, CALIFICACION, DURACION, ID_CATEG_TVHEADEND,GENERO,PAIS,
                                                                                OTROS,IMAGENFICHA,TITULO_ORIGINAL,IDIOMAS) VALUES(?,?,?,?,?,?,?,?,?,?,?)''',tupmt)
                                    
                                        db.commit()
                                                                                                                                                                   
                                        fica = ""
                                        pargume = ""
                                        califi = ""
                                        duraci = ""
                                        codigo = ""
                                        pgenre = ""
                                        ppaisa = ""
                                        otros = ""
                                        imgficha = ""
                                        pgamm = ""
                                        pidioma = ""
                                        chivatoficha = 1
                                     
                                while busc[0] in rowsParSFGROUPTITULO[v][0]: 
                             
                                    del rowsParSFGROUPTITULO[z] 
                                    
                                    if len(rowsParSFGROUPTITULO) == 0:
                                        break
                                    
                            if chivatoficha == 1:
                                
                                break
                                                    
                        #v = v + 1       
            
                except sqlite3.IntegrityError:
                                
                    pass
                
                except sqlite3.OperationalError as e:
        
                    mensaje = "OperationalError: " + e.args[0]
                    ficheroLog(pathRuta(), mensaje)
                    #print "OperationalError: " , e    
                
                except sqlite3.Error as e:
                
                    ficheroLog(pathRuta(),"Error %s:" % e.args[0])    
                    #print "Error %s:" % e.args[0]
         
                    sys.exit(1)
        
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. ***********  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ BEIN ~ BD ********** ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
                    
        #Buscamos fichas sin imagen de los canales Bein y si la encontramos la insertamos
        cursor.execute("SELECT * FROM FICHAS_SINIMAGEN_BEIN")
        
        rowsFSI_Bein = cursor.fetchall()
        
        if rowsFSI_Bein:     
            
            #salto = 0     
            
            for rb in rowsFSI_Bein:  
                
                #print  '.',              
                #t.sleep(0.1)  
                #sys.stdout.flush()
                #salto = salto + 1
                #if salto > 75:
                    #print '\n'
                    #salto = 0
                
                ficha = rb[0]
                
                cursor.execute("SELECT * FROM FICHAS_IMAG_BEIN WHERE TITULO=?",(rb[3],))
                
                rowsFIB_Bein = cursor.fetchone()
                
                if rowsFIB_Bein:
                    
                    imagenficha = rowsFIB_Bein[4]
                    
                    try:
                    
                        cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagenficha,ficha))
                        db.commit()
                    
                    except sqlite3.IntegrityError:
                                
                        pass
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. ***********  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ CINE ~ BD *********** ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
                    
        #Buscamos fichas sin imagen CINE y si la encontramos la insertamos
        cursor.execute("SELECT * FROM FICHAS_SINIMAGCINE")
        
        rowsFIB_CINE = cursor.fetchall()
        
        if rowsFIB_CINE:          
            
            salto = 0
            
            for rb in rowsFIB_CINE:  
                
                ficha = rb[0]            
                
                cursor.execute("SELECT * FROM FICHAS_IMAG_CINE WHERE TITULO=?",(rb[2],))
                
                rowsFSI_CINE = cursor.fetchall()
                
                #print  '.',              
                #t.sleep(0.1)  
                #sys.stdout.flush()
                #salto = salto + 1
                #if salto > 75:
                    #print '\n'
                    #salto = 0
                
                if rowsFSI_CINE:
                    
                    for cn in rowsFSI_CINE:
                        
                        imagenficha = cn[4]
                           
                        try:
                        
                            cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagenficha,ficha))
                            db.commit()
                            
                            #print  '.',              
                            #t.sleep(0.1)  
                            #sys.stdout.flush()
                            ##salto = salto + 1
                            #if salto > 75:
                                #print '\n'
                                #salto = 0
                        
                        except sqlite3.IntegrityError:
                                    
                            pass                              
        
        #print '\n'            
        
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. **************  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ CINE  ************* ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
           
        #print
        mensaje = "          --------------------------------   Inicio Descarga: %s -- %s  --------------------------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S"))
        #print mensaje
        #print
        #print "      ..................................................................................................................."
        #print
        ficheroLog(pathRuta(),mensaje)
    
        #rFichasSINIMAGCINE
        #Obtenemos las Fichas Tecnicas que no tiene imagen en la BD
        cursor.execute("SELECT * FROM FICHAS_SINIMAGCINE GROUP BY TITULO")
        rowsFichasSINIMAGCINE= cursor.fetchall()
        
        contador1 = len(rowsFichasSINIMAGCINE)
        contador2 = 0
        contador3 = 0
        
        if rowsFichasSINIMAGCINE:
            
            for fichsinimg in rowsFichasSINIMAGCINE:
                
                encontrado = 0
                
                ficha = str(fichsinimg[0],)
                titul = fichsinimg[2],
                
                ##############################################################################################
                #Por Titulo
                if fichsinimg[1]:
                    
                    titulo = formatearDatosUrl(fichsinimg[2], "1")
                                           
                    encontrado = filtrosbusquedaImagenWeb(titulo, ficha, "2")  
                        
                    if encontrado == 0:
                        
                        encontrado = filtrosbusquedaImagenWeb(titulo, ficha, "")
                        
                ###############################################################################################    
                #Por Titulo Original
            
                if encontrado == 0 and fichsinimg[3]:
                    
                    tituloo = formatearDatosUrl(fichsinimg[3], "1")
                    
                    encontrado = filtrosbusquedaImagenWeb(tituloo, ficha, "2")
                    
                
                if encontrado == 1:
                             
                    #print ("                      ----------------        Actualizada ficha = %s    -----------------                                     " %(ficha))
            
                    contador2 += 1
                    
                else:
                    contador3 += 1       
                    
                                
                #print "      ..................................................................................................................."
        
        
            #print        
            mensaje = ("              ----------------        T.Fichas: %d  *** T. Descargadas: %d  *** T. No Descargas: %d   -----------------                 " % (contador1,contador2,contador3))
            #print mensaje
            ficheroLog(pathRuta(), mensaje)
            #print           
                    
                    
        #print '\n'
        
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. *********  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ SERIES ~ BD ********* ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
        
        
        #Buscamos fichas sin imagen SERIE y si la encontramos la insertamos
        cursor.execute("SELECT * FROM FICHAS_SINIMAGSERIE")
        
        rowsFIB_SERIE = cursor.fetchall()
        
        if rowsFIB_SERIE:          
            
            salto = 0
            
            for rb in rowsFIB_SERIE:             
                
                cursor.execute("SELECT * FROM FICHAS_IMAG_SERIES WHERE TITULO=?",(rb[1],))
                
                rowsFSI_SERIE = cursor.fetchone()
                
                #print  '.',              
                #t.sleep(0.1)  
                #sys.stdout.flush()
                #salto = salto + 1
                #if salto > 75:
                    #print '\n'
                    #salto = 0
                
                if rowsFSI_SERIE:
                    
                    for cn in rowsFSI_SERIE:
                        
                        imagenficha = cn[3]
                    
                        ficha = rb[0]
                        
                        try:
                        
                            cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagenficha,ficha))
                            db.commit()
                            
                            #print  '.',              
                           # t.sleep(0.1)  
                          # sys.stdout.flush() 
                           # salto = salto + 1
                           # if salto > 75:
                            #    print '\n'
                            #    salto = 0
                        
                        except sqlite3.IntegrityError:
                                    
                            pass
            
        
       # print '\n'
        
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. *********  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ SERIES ~ BD ********* ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
    
        #Buscamos fichas en SINIMAGSERIE_SUBSTRING. Si obtenemos resultados
        cursor.execute("SELECT * FROM FICHAS_SINIMAGSERIE_SUBSTRING")
        
        rowsFIBB_SERIE = cursor.fetchall()
        
        if rowsFIBB_SERIE:          
            
            for rbb in rowsFIBB_SERIE:           
                
                cursor.execute("SELECT * FROM FICHAS_IMAG_SERIES WHERE f_TITULO=?",(rbb[1],))
                
                rowsFSII_SERIE = cursor.fetchone()
                
                #print  '.',              
                #t.sleep(0.1)  
                #sys.stdout.flush()
                
                if rowsFSII_SERIE:
                    
                    ficha = rbb[0] 
                                          
                    imagenficha = rowsFSII_SERIE[2]
                    
                    try:
                    
                        cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagenficha,ficha))
                        db.commit()
                        
                        #print  '.',              
                        #t.sleep(0.1)  
                        #sys.stdout.flush() 
                    
                    except sqlite3.IntegrityError:
                                
                        pass
                    
         
        #print
        #print "     ************************************************************************************************************************"
        #print
        mensaje = "       ............. ***********  OBTENIENDO IMAGENES DE FICHAS TECNICAS SIN IMAGEN ~ SERIES  *********** ............."
        #print mensaje
        #print
        #print "     ************************************************************************************************************************"
        ficheroLog(pathRuta(), mensaje)
           
        #print
        mensaje = "          --------------------------------   Inicio Descarga: %s -- %s  --------------------------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S"))
        #print mensaje
        #print "      ..................................................................................................................."
        #print
        ficheroLog(pathRuta(),mensaje)
    
        #rFichasSINIMAGSERIE
        #Obtenemos las Fichas Tecnicas que no tiene imagen en la BD
        cursor.execute("SELECT * FROM FICHAS_SINIMAGSERIE GROUP BY TITULO")
        rowsFichasSINIMAGSERIE = cursor.fetchall()
        
        contador1 = len(rowsFichasSINIMAGSERIE)
        contador2 = 0
        contador3 = 0
        
        if rowsFichasSINIMAGSERIE:
            
            for fichsinimg in rowsFichasSINIMAGSERIE:
                
                encontrado = 0
                
                ficha = str(fichsinimg[0],)
                titul = fichsinimg[2],
                
                 #Por Titulo
                if fichsinimg[1]:
                    
                    titulo = formatearDatosUrl(fichsinimg[2], "1")
                
                    if str(fichsinimg[2]) == "NCIS: Nueva Orleans":
                            
                        titulo = titulo.replace("Nueva","New")  
                                          
                    
                    titulo = titulo.replace("+(VOS)","")
                    
                    if str(fichsinimg[2]) == "Los Simpson":
                        
                        imagen = "http://pics.filmaffinity.com/the_simpsons_tv_series-146294444-mmed.jpg"
                        
                        cursor.execute('SELECT * FROM FICHA_SINIMAGSERIE WHERE TITULO=?',(fichsinimg[1],))
        
                        rowsFichasActualizar = cursor.fetchall()
                        
                        for fichsinimgact in rowsFichasActualizar:
                    
                            cursor.execute('UPDATE FICHA_TECNICA SET IMAGENFICHA=? WHERE FICHA=?',(imagen,fichsinimgact[0],))
                    
                            db.commit()
                        
                        encontrado = 1
                        
                    else:
                           
                        encontrado = filtrosbusquedaImagenWeb(titulo, ficha, "1")  
                        
                    if encontrado == 0:
                        
                        encontrado = filtrosbusquedaImagenWeb(titulo, ficha, "")
        
                if encontrado == 1:
                             
                    #print ("                      ----------------        Actualizada ficha = %s    -----------------                                     " %(ficha))
            
                    contador2 += 1
                    
                else:
                    contador3 += 1       
                    
                                
                #print "      ..................................................................................................................."
        
        
        #print        
        mensaje = ("              ----------------        T.Fichas: %d  *** T. Descargadas: %d  *** T. No Descargas: %d   -----------------                 " % (contador1,contador2,contador3))
        #print mensaje
        ficheroLog(pathRuta(), mensaje)
        #print           

        #Borramos las fichas que NO ESTAN EN PARRILLA.              
        borrarFichasHuerfanas(cursor, db)    
        
        #Generamos la EPG
        #os.chmod(pathRuta() + '/GUINIGUADA-EPG.log',0777)
        
        
        
    except sqlite3.OperationalError as e:
            
        mensaje = "OperationalError: " + e.args[0]
        ficheroLog(pathRuta(), mensaje)
        #print "OperationalError: " , e    
        
    except sqlite3.Error as e:
        
        ficheroLog(pathRuta(),"Error %s:" % e.args[0])    
        #print "Error %s:" % e.args[0]
        sys.exit(1)
        
    finally:

        if db:
            
            #Cerramos la conexion con BD
            db.close()
    
################################################################################################
##############################################################################################

except IOError as e:        
    #print("Error OS: {0}".format(e))
    ficheroLog(pathRuta(),"Error %s:" % e.args[0])

except ValueError as e:
    #print('Non-numeric data found in the file.', e )
    ficheroLog(pathRuta(),"Error %s:" % e.args[0])
    
except ImportError as e:    
    mensaje = "Ud. no tiene instalado el modulo: {0}".format(e.message[16:])
    ficheroLog(pathRuta(), mensaje)    
    #print "Ud. no tiene instalado el modulo: {0}".format(e.message[16:])
    mensaje = "                        -- -- -- -- -- -- --         FIN PROGRAMA         -- -- -- -- -- -- --    "
    #print mensaje
    ficheroLog(pathRuta(),mensaje)
    #print
        
except EOFError as e:
    #print('Why did you do an EOF on me?', e )
    ficheroLog(pathRuta(),"Error %s:" % e.args[0])

except KeyboardInterrupt as e:
    #print('You cancelled the operation.', e )
    ficheroLog(pathRuta(),"Error %s:" % e.args[0])

#===============================================================================
# except:
#     #print("Error inesperado")
#     ficheroLog(pathRuta(),"Error inesperado")
#===============================================================================

finally:
        
    
    #Fecha actual en formatado date
    hoy = datetime.now()
    #print
    mensaje = ("        --------------------------------   Descarga Finalizada: %s -- %s  --------------------------------" % (hoy.strftime("%d-%m-%Y"), hoy.strftime("%H:%M:%S")))
    #print mensaje
    #print
    ficheroLog(pathRuta(),mensaje)
    commands.getoutput('chmod 0777 ' + pathRuta() + '/GUINIGUADA-EPG.log')
    #commands.getoutput('chown 1024 '+ pathRuta() + '/GUINIGUADA-EPG.log')                                
    #commands.getoutput('chgrp 100 ' + pathRuta() + '/GUINIGUADA-EPG.log')
################################################################################################      