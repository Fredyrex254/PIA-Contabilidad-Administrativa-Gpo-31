#MATRIZ DE 1.- Presupuesto de ventas.
mtzArticulos = []
dicArticulo =  dict(CodArticulo = "", NomArticulo = "")
lstValArticulo = []

#MATRIZ DE 2.- Determinación del saldo de Clientes y Flujo de Entradas.
mtzVenta = []
dicPventa = dict(CodArticulo = "", UnitVender = "", PVenta = "", Semestre = 0)

#MATRIZ DE 3.- Presupuesto de Producción.
dicPProduccion = dict(CodArticulo = "",UnidVender = 0 , InvInicial = 0, InvFinal = 0, Semestre = 0)
mtzPProduccion = []

#MATRICES DE 4.- Presupuesto de Requerimiento de Materiales.
ACABADO4 = 0
dicMateriales = dict(CodArticulo="", UndProducir=0, MaterialA="",MaterialB="",MaterialC="",Semestre=0)
mtzMateriales=[]
dicReq = dict(CodArticulo="", TotMatA = 0, TotMatB = 0, TotMatC = 0, Semestre = 0)
mtzReq=[]
dicReqTotal = dict(CodArticulo="", Total2016A=0, Total2016B = 0, Total2016C= 0 )
mtzReqTotal = []
dicTotalPorSem = dict(CodArticulo="",Semestre=0,TotalASem1=0,TotalBSem1=0, TotalCSem1=0, TotalASem2=0,TotalBSem2=0, TotalCSem2=0)
mtzTotalPorSem =[]

#MATRICES DE 5.-

listMatName =  ["'A'","'A'","'B'","'B'","'C'","'C'"]
dictPCMat = dict(Nombre= "",Semestre = 0, InventarioFin = 0, InventarioInic = 0,PrecioCompra = 0, Requerimiento=0)
mtzPCMat = []

#MATRICES DE 7.
dicMod = dict(CodArticulo = "", UnidProd = 0, HrReq = 0, CuotaHr = 0, Semestre = 0)
mtzMod = []

#MATRICES DE 8.
dicGIF= dict(Depreciacion= 0, Seguros= 0, Mantenimiento= 0, Energeticos= 0, Varios= 0,Semestre= 0)
mtzGIF= []

#MATRICES DE 9.
dicGastosOp= dict(Depreciacion= 0,SueldosYSalarios= 0, Varios= 0, IntPrestamo=0,Semestre= 0)
mtzGastosOp=[]

# MATRICES DEL 10
dicDcuCosto = dict(CodArticulo = "" , MatACosto = 0 , MatBCosto = 0  , MatCCosto = 0, MoCosto = 0,GifCosto = 0)
mtzDcuCosto = []


dicDcuCantidad = dict(CodArticulo = "" , MatACant = 0, MatBCant = 0, MatCCant = 0,MoCant = 0,GifCant = 0)
mtzDucCantidad = []

A1Sem1=0.0
A1Sem2=0.0
A2Sem1=0.0
A2Sem2=0.0
A3Sem1=0.0
A3Sem2=0.0
dicArticulo["CodArticulo"] = "1"
dicArticulo["NomArticulo"] = "CL"
mtzArticulos.append(dicArticulo.copy())

dicArticulo["CodArticulo"] = "2"
dicArticulo["NomArticulo"] = "CE"
mtzArticulos.append(dicArticulo.copy())

dicArticulo["CodArticulo"] = "3"
dicArticulo["NomArticulo"] = "CR"
mtzArticulos.append(dicArticulo.copy())

Opcion = 0
while (Opcion != 12):
    print ("Sistema de contabilidad FACPYA ==\n1.- Presupuesto de ventas. \n2.- Determinación del saldo de Clientes y Flujo de Entradas.")
    print ("3.- Presupuesto de Producción. \n4.- Presupuesto de Requerimiento de Materiales.\n5.- Presupuesto de Compra de Materiales.")
    print ("6.- Determinación del saldo de Proveedores y Flujo de Salidas.\n7.- Presupuesto de Mano de Obra Directa.\n8.- Presupuesto de Gastos Indirectos de Fabricación.")
    print ("9.- Presupuesto de Gastos de Operación.\n10.- Determinación del Costo Unitario de Productos Terminados.\n11.- Valuación de Inventarios Finales.")
    print ("12.- SALIR.")
    Opcion = int(input("\nIngrese la opcion a realizar: "))    

# 1.- Presupuesto de ventas.
    if (Opcion==1):
        Opcion2 = "" 

        while True :
            print ("\n==Presupuesto de venta.\n")
            Opcion2 = input("Deseas agregar informacion de un producto? (S/N): ")

            if Opcion2.upper() == "S": 
                print ("(Catalago de articulos)")

                for Diccionario in mtzArticulos:
                    print ((Diccionario["CodArticulo"]) + ' - ' + (Diccionario["NomArticulo"]))
                    lstValArticulo.append(Diccionario["CodArticulo"])       

                while True:
                    Codigo = (input("Ingrese el codigo articulo a cargar: "))

                    if (Codigo in lstValArticulo):
                        for Cont in range(0,2):
                            for campo in dicPventa:
                                if (campo == "CodArticulo"):
                                    dicPventa[campo] = Codigo
                                elif campo == "Semestre":
                                    dicPventa[campo] = (Cont + 1)
                                else:
                                    dicPventa[campo] = float(input(f"ingrese la cantidad de {campo} para el semestre {Cont+1}° semestre: "))
                            mtzVenta.append(dicPventa.copy())

                        DictCount = -1
                        Counter = 0

                        for Dict in mtzVenta:
                            DictCount +=1
                            for Element in Dict:
                                if Element == "CodArticulo":
                                    Articulo = (mtzVenta[DictCount][Element])
                                if Element == "UnitVender":
                                    UnitVender = float(mtzVenta[DictCount][Element]) 
                                if Element == "PVenta":
                                    PVenta = float(mtzVenta[DictCount][Element])
                                    Counter += 1  
                            if Counter == 1:
                                Total1Semestre = (UnitVender*PVenta)
                                print("_"*105)
                                print(f'{"|":^}{"":^41}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"CANTIDAD":^20}{"|":^}')
                                print(f'{"|":^}{"Unidades a vender":^40} {"|":^}{Articulo:^20}{"|":^}{"PRIMER SEMESTRE":^20}{"|":^}{UnitVender:^20}{"|":^}')
                                print(f'{"|":^}{"Precio de venta":^40} {"|":^}{Articulo:^20}{"|":^}{"SEGUNDO SEMESTRE":^20}{"|":^}{PVenta:^20}{"|":^}')
                                print("_"*105)
                                print(f'{"|":^}{"":^20} TOTAL DEL PRIMER SEMESTRE DEL ARTICULO {Articulo} : {Total1Semestre}{"|":^64}')
                                if Articulo == "1":
                                    A1Sem1 = Total1Semestre
                                if Articulo == "2":
                                    A2Sem1 = Total1Semestre
                                if Articulo == "3":
                                    A3Sem1 = Total1Semestre
                            elif Counter == 2:
                                Total2Semestre = (UnitVender*PVenta)
                                print("_"*105)
                                print(f'{"|":^}{"":^41}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"CANTIDAD":^20}{"|":^}')
                                print(f'{"|":^}{"Unidades a vender":^41}{"|":^}{Articulo:^20}{"|":^}{"2":^20}{"|":^}{UnitVender:^20}{"|":^}')
                                print(f'{"|":^}{"Precio de venta":^41}{"|":^}{Articulo:^20}{"|":^}{"2":^20}{"|":^}{UnitVender:^20}{"|":^}')
                                print("_"*105)
                                print(f'{"|":^}{"":^20} TOTAL DEL SEGUNDO SEMESTRE DEL ARTICULO {Articulo} : {Total2Semestre}{"|":^62}')
                                GranTotal = (Total1Semestre + Total2Semestre)
                                print(f'{"|":^}{"":^20} El total anual del producto {Articulo} = {GranTotal}{"|":^85}')
                                Counter = 0
                                if Articulo == "1":
                                    A1Sem2 = Total2Semestre
                                if Articulo == "2":
                                    A2Sem2 = Total2Semestre
                                if Articulo == "3":
                                    A3Sem2 = Total2Semestre
                        SEMESTRE1 = float((A1Sem1+A2Sem1)+A3Sem1)
                        SEMESTRE2 = float((A1Sem2+A2Sem2)+A3Sem2)
                        TOTAL = float(SEMESTRE1+SEMESTRE2)
                        print(f"El total del primer semestre DE TODOS LOS PRODUCTOS fue de {SEMESTRE1}")
                        print(f"El total del segundo semestre DE TODOS LOS PRODUCTOS fue de {SEMESTRE2}")
                        print(f"Y el total de todo el año y todos los productos es de {TOTAL}")
                        break

                    else:
                        print(f"El codigo {Codigo} no es valido...")

            if Opcion2.upper() == "N":
                print("Regresando al menu principal")
                break

# 2.- Determinación del saldo de Clientes y Flujo de Entradas.
    if (Opcion==2):
        print("== Determinación del saldo de Clientes y Flujo de Entradas")
        SaldoClientes2015 = int(input("Dame el saldo de clientes al 31-Diciembre-2015: "))
        porcentaje15 = float(input("\nCuanto porcentaje se cobro del 2015? (EN DECIMAL, EJ: 20% = PONER(.20) : "))
        porcentaje16 = float(input("\nCuanto porcentaje se cobro del 2016? (EN DECIMAL, EJ: 20% = PONER(.20) : "))
        TotalClientes2016 = float(SaldoClientes2015+TOTAL)
        TotalEntradas2016 = float((SaldoClientes2015*porcentaje15)+(TOTAL*porcentaje16))
        SaldoClientes2016 = float(TotalClientes2016 - TotalEntradas2016)
        print("_"*93)
        print(f'{"|":^}{"DESCRIPCION":^50}{"|":^}{"IMPORTE":^20}{"|":^}{"TOTAL":^20}{"|":^}')
        print(f'{"|":^}{"Saldo de clientes 31-Dic-2015":^50}{"|":^}{"":^20}{"|":^}{SaldoClientes2015:^20}{"|":^}')
        print(f'{"|":^}{"Ventas 2016":^50}{"|":^}{"":^20}{"|":^}{TOTAL:^20}{"|":^}')
        print(f'{"|":^}{"ENTRADAS DE EFECTIVO":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}')
        print(f'{"|":^}{"Por cobranza 2015":^50}{"|":^}{SaldoClientes2015*porcentaje15:^20}{"|":^}{porcentaje15:^20}{"|":^}')
        print(f'{"|":^}{"Por cobranza 2016":^50}{"|":^}{TOTAL*porcentaje16:^20}{"|":^}{porcentaje16:^20}{"|":^}')
        print(f'{"|":^}{"Total enetradas 2016":^50}{"|":^}{"":^20}{"|":^}{TotalEntradas2016:^20}{"|":^}')
        print(f'{"|":^}{"SALDO CLIENTES 2016":^50}{"|":^}{"":^20}{"|":^}{SaldoClientes2016:^20}{"|":^}')
        print("_"*93)

# 3.- Presupuesto de Producción.
    if (Opcion==3):
        Opcion3 = "" 
        print ("\n==PRESUPUESTO DE PRODUCCION.\n")
         
        for Dict in mtzVenta:
            for Element in Dict:
                if Element == "CodArticulo":
                    dicPProduccion["CodArticulo"] = int(Dict["CodArticulo"])
                if Element == "UnitVender":
                    dicPProduccion["UnidVender"] = int(Dict["UnitVender"])
                if Element == "Semestre":
                    dicPProduccion["Semestre"] = int(Dict["Semestre"])
                    Sem = int(Dict["Semestre"])
                    Art = int(Dict["CodArticulo"])
                    InvInic = input(f"Dame el inventario INICIAL del semestre {Sem} del articulo {Art}: ")
                    InvFin = input(f"Dame el inventario FINAL del semestre {Sem} del articulo {Art}: ")
                    dicPProduccion["InvInicial"] = InvInic
                    dicPProduccion["InvFinal"] = InvFin
                    mtzPProduccion.append(dicPProduccion.copy())
            DictCount = -1
            Counter = 0

            for Dict in mtzPProduccion:
                DictCount +=1
                for Element in Dict:
                    if Element == "CodArticulo":
                        Articulo = (mtzPProduccion[DictCount][Element])
                    if Element == "UnidVender":
                        UnidVender = float(mtzPProduccion[DictCount][Element])
                    if Element == "InvInicial":
                        InvInicial = float(mtzPProduccion[DictCount][Element]) 
                    if Element == "InvFinal":
                        InvFinal = float(mtzPProduccion[DictCount][Element])
                        Counter += 1  
                if Counter == 1:
                    TotalUnidades = (UnidVender + InvFinal)
                    UnidProducir = (TotalUnidades - InvInicial)
                    print("_"*105)
                    print(f'{"|":^}{"":^40}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"CANT DE INVENTARIO":^20}{"|":^}')
                    print(f'{"|":^}{"Unidades a Vender":^40}{"|":^}{Articulo:^20}{"|":^}{"PRIMER SEMESTRE":^20}{"|":^}{UnidVender:^20}{"|":^}')
                    print(f'{"|":^}{"Inventraio Final":^40}{"|":^}{Articulo:^20}{"|":^}{"PRIMER SEMESTRE":^20}{"|":^}{InvFinal:^20}{"|":^}')
                    print(f'{"|":^}{"TOTAL DE UNIDADES":^40}{"|":^}{Articulo:^20}{"|":^}{"":^20}{"|":^}{TotalUnidades:^20}{"|":^}')
                    print(f'{"|":^}{"Inventraio Inicial":^40}{"|":^}{Articulo:^20}{"|":^}{"PRIMER SEMESTRE":^20}{"|":^}{InvFinal:^20}{"|":^}')
                    print("_"*105)
                    print(f'{"|":^}{"":^20} UNIDADES A PRODUCIR DEL PRIMER SEMESTRE DEL ARTICULO {Articulo} : {UnidProducir}{"|":^42}')
                    if Articulo == "1":
                        A1Sem1 = UnidProducir
                    if Articulo == "2":
                        A2Sem1 = UnidProducir
                    if Articulo == "3":
                        A3Sem1 = UnidProducir
                        
                elif Counter == 2:
                    
                    TotalUnidades2 = (UnidVender + InvFinal)
                    UnidProducir2 = (TotalUnidades2 - InvInicial)
                    print("_"*105)
                    print(f'{"|":^}{"":^40}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"CANT DE INVENTARIO":^20}{"|":^}')
                    print(f'{"|":^}{"Unidades a Vender":^40}{"|":^}{Articulo:^20}{"|":^}{"SEGUNDO SEMESTRE":^20}{"|":^}{UnidVender:^20}{"|":^}')
                    print(f'{"|":^}{"Inventraio Final":^40}{"|":^}{Articulo:^20}{"|":^}{"SEGUNDO SEMESTRE":^20}{"|":^}{InvFinal:^20}{"|":^}')
                    print(f'{"|":^}{"TOTAL DE UNIDADES":^40}{"|":^}{Articulo:^20}{"|":^}{"":^20}{"|":^}{TotalUnidades:^20}{"|":^}')
                    print(f'{"|":^}{"Inventraio Inicial":^40}{"|":^}{Articulo:^20}{"|":^}{"SEGUNDO SEMESTRE":^20}{"|":^}{InvInicial:^20}{"|":^}')
                    print("_"*105)
                    print(f'{"|":^}{"":^20} UNIDADES A PRODUCIR DEL SEGUNDO SEMESTRE DEL ARTICULO {Articulo} : {UnidProducir2}{"|":^40}')
                    GranTotal3 = (UnidProducir + UnidProducir2)
                    print(f'{"|":^}{"":^20} EL TOTAL ANUAL DEL PRODUCTO {Articulo} = {GranTotal3}{"|":^90}')
                    Counter=0

# 4.- Presupuesto de Requerimiento de Materiales.       
    if (Opcion==4):
        for Dict in mtzPProduccion:
            for Element in Dict:
                if Element == "CodArticulo":
                    dicMateriales["CodArticulo"] = int(Dict["CodArticulo"])
                if Element == "Semestre":
                    dicMateriales["Semestre"] = int(Dict["Semestre"])
                    Sem = int(Dict["Semestre"])
                    Art = int(Dict["CodArticulo"])
                    UnidProducir = float((Dict["UnidVender"]) + float(Dict["InvFinal"]) - float(Dict["InvInicial"]))
                    dicMateriales["UndProducir"] = UnidProducir
                    MatA = float(input(f"Ingresa el requerimiento del material A del semestre {Sem} del articulo {Art}: "))
                    MatB = float(input(f"Ingresa el requerimiento del material B del semestre {Sem} del articulo {Art}: "))
                    MatC = float(input(f"Ingresa el requerimiento del material C del semestre {Sem} del articulo {Art}: "))
                    dicMateriales["MaterialA"] = MatA
                    dicMateriales["MaterialB"] = MatB
                    dicMateriales["MaterialC"] = MatC
                    mtzMateriales.append(dicMateriales.copy())
                    print(mtzMateriales)
        
        for Dict in mtzMateriales:
            for Element in Dict:
                if Element == "CodArticulo":
                    dicReq["CodArticulo"] = int(Dict["CodArticulo"])
                if Element == "Semestre":
                    dicReq["Semestre"]= int(Dict["Semestre"])
                    TotA = float((Dict["MaterialA"])*(Dict["UndProducir"]))
                    TotB = float((Dict["MaterialB"])*(Dict["UndProducir"]))
                    TotC = float((Dict["MaterialC"])*(Dict["UndProducir"]))
                    dicReq["TotMatA"] = TotA
                    dicReq["TotMatB"] = TotB
                    dicReq["TotMatC"] = TotC
                    mtzReq.append(dicReq.copy())
        
        
        PrimSemA = 0
        SeguSemA = 0
        PrimSemB = 0
        SeguSemB = 0
        PrimSemC = 0
        SeguSemC = 0
        for Cont in range(0,len(mtzMateriales)):
            if Cont == 0 or not (Cont%2) == 0 and not Cont == 1:
                if (mtzMateriales[Cont]["CodArticulo"]) == "1":
                    Nombre = "CL"
                elif (mtzMateriales[Cont]["CodArticulo"]) == "2":
                    Nombre = "CE"
                else:
                    Nombre = "CR"

                UNITProd1 = mtzMateriales[Cont]["UndProducir"]
                ReqMatA1 = mtzMateriales[Cont]["MaterialA"]
                ReqMatB1 = mtzMateriales[Cont]["MaterialB"]
                ReqMatC1 = mtzMateriales[Cont]["MaterialC"]
                TotMatA1 = mtzReq[Cont]["TotMatA"]
                TotMatB1 = mtzReq[Cont]["TotMatB"]
                TotMatC1 = mtzReq[Cont]["TotMatC"]
                PrimSemA += TotMatA1
                PrimSemB += TotMatB1
                PrimSemC += TotMatC1
                    
            else:
                UNITProd2 = mtzMateriales[Cont]["UndProducir"]
                ReqMatA2 = mtzMateriales[Cont]["MaterialA"]
                ReqMatB2 = mtzMateriales[Cont]["MaterialB"]
                ReqMatC2 = mtzMateriales[Cont]["MaterialC"]
                TotMatA2 = mtzReq[Cont]["TotMatA"]
                TotMatB2 = mtzReq[Cont]["TotMatB"]
                TotMatC2 = mtzReq[Cont]["TotMatC"]
                SeguSemA += TotMatA2
                SeguSemB += TotMatB2
                SeguSemC += TotMatC2
                print("_"*95)
                print(f"{'|':^}{'PRODUCTO':^30}{'|':^}{'PRIMER SEMESTRE':^20}{'|':^}{'SEGUNDO SEMESTRE':^20}{'|':^}{'TOTAL 2016':^20}{'|':^}")
                print(f"{'|':^}{Nombre:^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Unidades a producir':^30}{'|':^}{UNITProd1:^20}{'|':^}{UNITProd2:^20}{'|':^}{UNITProd1+UNITProd2:^20}{'|':^}")
                print(f"{'|':^}{'':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Material A en METROS':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Requerimiento Material':^30}{'|':^}{ReqMatA1:^20}{'|':^}{ReqMatA2:^20}{'|':^}{ReqMatA1:^20}{'|':^}")
                print(f"{'|':^}{'TOTAL MAT. A REQUERIDO ':^30}{'|':^}{TotMatA1:^20}{'|':^}{TotMatA2:^20}{'|':^}{TotMatA1+TotMatA2:^20}{'|':^}")
                print(f"{'|':^}{'':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Material B en METROS':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Requerimiento Material':^30}{'|':^}{ReqMatB1:^20}{'|':^}{ReqMatB2:^20}{'|':^}{ReqMatB1:^20}{'|':^}")
                print(f"{'|':^}{'TOTAL MAT. B REQUERIDO':^30}{'|':^}{TotMatB1:^20}{'|':^}{TotMatB2:^20}{'|':^}{TotMatB1+TotMatB2:^20}{'|':^}")
                print(f"{'|':^}{'':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Material C en METROS':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}")
                print(f"{'|':^}{'Requerimiento Material':^30}{'|':^}{ReqMatC1:^20}{'|':^}{ReqMatC2:^20}{'|':^}{ReqMatC1:^20}{'|':^}")
                print(f"{'|':^}{'TOTAL MAT. C REQUERIDO':^30}{'|':^}{TotMatC1:^20}{'|':^}{TotMatC2:^20}{'|':^}{TotMatC1+TotMatC2:^20}{'|':^}")
                print("_"*95)
        print("_"*95)
        print(f"{'|':^}{'TOTAL DE REQUERIMIENTOS':^30}{'|':^}{'':^20}{'|':^}{'':^20}{'|':^}{'TOTAL 2016':^20}{'|':^}")
        print(f"{'|':^}{'Material A Metros':^30}{'|':^}{PrimSemA:^20}{'|':^}{SeguSemA:^20}{'|':^}{PrimSemA+SeguSemA:^20}{'|':^}")
        print(f"{'|':^}{'Material B Metros':^30}{'|':^}{PrimSemB:^20}{'|':^}{SeguSemB:^20}{'|':^}{PrimSemB+SeguSemB:^20}{'|':^}")
        print(f"{'|':^}{'Material C Metros':^30}{'|':^}{PrimSemC:^20}{'|':^}{SeguSemC:^20}{'|':^}{PrimSemC+SeguSemC:^20}{'|':^}")
        print("_"*95)
        ACABADO4 = 1

# 5.- Presupuesto de Compra de Materiales
    if(Opcion==5) and (ACABADO4) == 1:
        listMater = [PrimSemA,SeguSemA,PrimSemB,SeguSemB,PrimSemC,SeguSemC]
        Cont1=-1
        Cont2=-2
        Count =-1
        for element in listMater:
            Cont1+=1
            Cont2+=1 
            Count+=1
            if Cont1 == 0:
                NombreMat = (listMatName[Count])
                dictPCMat["Semestre"]=1
                dictPCMat["InventarioFin"]=float(input(f"Dame el inventario final del material {NombreMat} del primer semestre: "))
                dictPCMat["InventarioInic"]=float(input(f"Dame el inventario inicial del material {NombreMat} del primer semestre: "))
                dictPCMat["PrecioCompra"]=float(input(f"Dame el Precio de compra del material {NombreMat}"))
                dictPCMat["Requerimiento"]=(listMater[Count])
                dictPCMat["Nombre"]=NombreMat
                mtzPCMat.append(dictPCMat.copy())
                Cont1=-2
            
            if Cont2 == 0:
                NombreMat = (listMatName[Count])
                dictPCMat["Semestre"]=2
                dictPCMat["InventarioFin"]=float(input(f"Dame el inventario final del material {NombreMat} del segundo semestre: "))
                dictPCMat["InventarioInic"]=float(input(f"Dame el inventario inicial del material {NombreMat} del segundo semestre: "))
                dictPCMat["PrecioCompra"]=float(input(f"Dame ultimo el Precio de compra del material {NombreMat}"))
                dictPCMat["Requerimiento"]=listMater[Count]
                dictPCMat["Nombre"]=NombreMat
                mtzPCMat.append(dictPCMat.copy())
                Cont2 =-2

        print(mtzPCMat)
        Counter=-1 
        
        TotalDin1Acum = 0
        TotalDin2Acum = 0
        for Dict in mtzPCMat:
            Counter+=1
            if Counter == 0:
                Semestre1 = Dict["Semestre"]
                InventFin1 = Dict["InventarioFin"]
                InventInic1 = Dict["InventarioInic"]
                PreCompra1 = Dict["PrecioCompra"]
                Req1 = Dict["Requerimiento"]
                TotalMat1 = (InventFin1+Req1)
                MatCom1 = (TotalMat1-InventInic1)
                TotalDinero1 = (PreCompra1*MatCom1)
                TotalDin1Acum += TotalDinero1

            if Counter == 1:
                Name1 = Dict["Nombre"]
                Semestre2 = Dict["Semestre"]
                InventFin2 = Dict["InventarioFin"]
                InventInic2 = Dict["InventarioInic"]
                PreCompra2 = Dict["PrecioCompra"]
                Req2 = Dict["Requerimiento"]
                TotalMat2 = (InventFin2+Req2)
                MatCom2 = (TotalMat2-InventInic2)
                TotalDinero2 = (PreCompra2*MatCom2)
                TotalDin2Acum += TotalDinero2
                Counter = 2

            if Counter == 2:
                print("_"*105)
                print(f'{"|":^}{"":^40}{"|":^}{"1er. Semestre":^20}{"|":^}{"2do. Semestre":^20}{"|":^}{"TOTAL2016 ":^20}{"|":^}')
                print(f'{"|":^}{"Material"+str(Name1):^40}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}')
                print(f'{"|":^}{"Requerimiento de Mat":^40}{"|":^}{Req1:^20}{"|":^}{Req2:^20}{"|":^}{Req1+Req2:^20}{"|":^}')
                print(f'{"|":^}{"Inventario Final":^40}{"|":^}{InventFin1:^20}{"|":^}{InventFin2:^20}{"|":^}{InventFin1+InventFin2:^20}{"|":^}')
                print(f'{"|":^}{"Total De Materiales":^40}{"|":^}{TotalMat1:^20}{"|":^}{TotalMat2:^20}{"|":^}{TotalMat1+TotalMat2:^20}{"|":^}')
                print(f'{"|":^}{"Inventario Inicial":^40}{"|":^}{InventInic1:^20}{"|":^}{InventInic2:^20}{"|":^}{InventInic1+InventInic2:^20}{"|":^}')
                print(f'{"|":^}{"Material a Comprar":^40}{"|":^}{MatCom1:^20}{"|":^}{MatCom2:^20}{"|":^}{MatCom1+MatCom2:^20}{"|":^}')
                print(f'{"|":^}{"Precio de Compra":^40}{"|":^}{PreCompra1:^20}{"|":^}{PreCompra2:^20}{"|":^}{"":^20}{"|":^}')
                print(f'{"|":^}{"Total de material $":^40}{"|":^}{TotalDinero1:^20}{"|":^}{TotalDinero2:^20}{"|":^}{TotalDinero1+TotalDinero2:^20}{"|":^}')
                Counter = -1
        totalcost16 = TotalDin1Acum+TotalDin2Acum
        print("_"*105)
        print(f'{"|":^}{"Costos Totales":^40}{"|":^}{TotalDin1Acum:^20}{"|":^}{TotalDin2Acum:^20}{"|":^}{totalcost16:^20}{"|":^}')           

# 6.- Determinación del saldo de Proveedores y Flujo de Salidas.
    if (Opcion==6):
        TOTAL = totalcost16
        print("== Determinación del saldo de Proveedores y Flujo de Entradas")
        SaldoProveedores2015 = int(input("Dame el saldo de Proveedores al 31-Diciembre-2015: "))
        porcentaje15_6 = float(input("\nCuanto porcentaje se salio del 2015? (EN DECIMAL, EJ: 20% = PONER(.20) : "))
        porcentaje16_6 = float(input("\nCuanto porcentaje se salio del 2016? (EN DECIMAL, EJ: 20% = PONER(.20) : "))
        TotalProveedores2016 = float(SaldoProveedores2015+TOTAL)
        TotalEntradas2016 = float((SaldoProveedores2015*porcentaje15_6)+(TOTAL*porcentaje16_6))
        SaldoProveedores2016 = float(TotalProveedores2016 - TotalEntradas2016)
        print("_"*93)
        print(f'{"|":^}{"DESCRIPCION":^50}{"|":^}{"IMPORTE":^20}{"|":^}{"TOTAL":^20}{"|":^}')
        print(f'{"|":^}{"Saldo de Proveedores 31-Dic-2015":^50}{"|":^}{"":^20}{"|":^}{SaldoProveedores2015:^20}{"|":^}')
        print(f'{"|":^}{"Compras 2016":^50}{"|":^}{"":^20}{"|":^}{TOTAL:^20}{"|":^}')
        print(f'{"|":^}{"TOTAL CLIENTES 2016":^50}{"|":^}{"":^20}{"|":^}{TotalProveedores2016:^20}{"|":^}')
        print(f'{"|":^}{"SALIDA DE EFECTIVO:":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}')
        print(f'{"|":^}{"Por Proveedores 2015":^50}{"|":^}{SaldoProveedores2015*porcentaje15_6:^20}{"|":^}%{porcentaje15_6:^20}{"|":^}')
        print(f'{"|":^}{"Por Proveedores 2016":^50}{"|":^}{TOTAL*porcentaje16_6:^20}{"|":^}%{porcentaje16_6:^20}{"|":^}')
        print(f'{"|":^}{"Total salida 2016":^50}{"|":^}{"":^20}{"|":^}{TotalEntradas2016:^20}{"|":^}')
        print(f'{"|":^}{"SALDO PROVEEDORES 2016 ":^50}{"|":^}{"":^20}{"|":^}{SaldoProveedores2016:^20}{"|":^}')
        print("_"*93)

# 7.- Presupuesto de Mano de Obra Directa.
    if(Opcion==7):
        for Dict in mtzPProduccion:
            for Element in Dict:
                if Element == "CodArticulo":
                    dicMod["CodArticulo"] = int(Dict["CodArticulo"])
                if Element == "UnidVender":
                    dicMod["UnidProd"] = int(Dict["UnidVender"])
                if Element == "Semestre":
                    dicMod["Semestre"] = int(Dict["Semestre"])
                    Sem = int(Dict["Semestre"])
                    Art = int(Dict["CodArticulo"])
                    HrRequeridas = input(f"Dame las HORAS REQUERIDAS del semestre {Sem} del articulo {Art}: ")
                    CuotaHora = input(f"Dame la CUOTA POR HORA del semestre {Sem} del articulo {Art}: ")
                    dicMod["HrReq"] = HrRequeridas
                    dicMod["CuotaHr"] = CuotaHora
                    mtzMod.append(dicMod.copy())
            DictCount = -1
            Counter = 0
            for Dict in mtzMod:
                DictCount +=1
                for Element in Dict:
                    #int(Dict["CodArticulo"])
                    if Element == "CodArticulo":
                        Articulo7 = (mtzPProduccion[DictCount][Element])
                    if Element == "UnidProd":
                        UnidProducir = float(mtzMod[DictCount][Element])
                    if Element == "HrReq":
                        HorasReq = float(mtzMod[DictCount][Element]) 
                    if Element == "CuotaHr":
                        CuotaHr = float(mtzMod[DictCount][Element])
                        Counter += 1  
                if Counter == 1:
                    TotalHorasReq = (UnidProducir * HorasReq)
                    ImporteMOD = (TotalHorasReq * CuotaHr)
                    print("")
                    print("_"*105)
                    print(f'{"|":^}{"":^40}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"Cant de Inventario ":^20}{"|":^}')
                    print(f'{"|":^}{"Unidades a Producir":^40}{"|":^}{Articulo7:^20}{"|":^}{"1° SEMESTRE":^20}{"|":^}{UnidProducir:^20}{"|":^}')
                    print(f'{"|":^}{"Hrs requeridas por unidad":^40}{"|":^}{Articulo7:^20}{"|":^}{"1° SEMESTRE":^20}{"|":^}{HorasReq:^20}{"|":^}')
                    print(f'{"|":^}{"TOTAL DE Horas requeridas":^40}{"":^}{"":^20}{"":^}{"":^22}{"|":^}{TotalHorasReq:^20}{"|":^}')
                    print(f'{"|":^}{"Cuota por hora":^40}{"|":^}{Articulo7:^20}{"|":^}{"1° SEMESTRE":^20}{"|":^}{CuotaHr:^20}{"|":^}')
                    print("_"*105)
                    print(f"IMPORTE DE M.O.D DEL SEGUNDO SEMESTRE DEL ARTICULO {Articulo7}: {ImporteMOD}")
                    if Articulo7 == "1":
                        A1Sem1 = UnidProducir
                    if Articulo7 == "2":
                        A2Sem1 = UnidProducir
                    if Articulo7 == "3":
                        A3Sem1 = UnidProducir
                        
                elif Counter == 2:
                    TotalHorasReq2 = (UnidProducir * HorasReq)
                    ImporteMOD2 = (TotalHorasReq2 * CuotaHr)
                    print("_"*105)
                    print(f'{"|":^}{"":^40}{"|":^}{"ARTICULO":^20}{"|":^}{"SEMESTRE":^20}{"|":^}{"Cant de Inventario ":^20}{"|":^}')
                    print(f'{"|":^}{"Unidades a Producir":^40}{"|":^}{Articulo7:^20}{"|":^}{"2° SEMESTRE":^20}{"|":^}{UnidProducir:^20}{"|":^}')
                    print(f'{"|":^}{"Hrs requeridas por unidad":^40}{"|":^}{Articulo7:^20}{"|":^}{"2° SEMESTRE":^20}{"|":^}{HorasReq:^20}{"|":^}')
                    print(f'{"|":^}{"TOTAL DE Horas requeridas":^40}{"":^}{"":^20}{"":^}{"":^22}{"|":^}{TotalHorasReq2:^20}{"|":^}')
                    print(f'{"|":^}{"Cuota por hora":^40}{"|":^}{Articulo7:^20}{"|":^}{"2° SEMESTRE":^20}{"|":^}{CuotaHr:^20}{"|":^}')
                    print("_"*105)
                    print(f"IMPORTE DE M.O.D DEL SEGUNDO SEMESTRE DEL ARTICULO {Articulo7}: {ImporteMOD2}")
                    GranTotal7 = (ImporteMOD + ImporteMOD2)
                    print(f"El total anual del producto {Articulo7} = {GranTotal7}\n\n")
                    TOTALHORAS= TotalHorasReq+TotalHorasReq2
                    Counter = 0

# 8.- Presupuesto de Gastos Indirectos de Fabricacion.
    if (Opcion==8):
        print("==Presupuesto de Gastos Indirectos de Fabricacion==\n")
        Cont= 0
        Dcont= -1

        for Contt in range(0,2):
            for Artt in dicGIF:
                if (Artt == "Semestre"):
                    dicGIF[Artt] = (Cont + 1)
                else:
                    dicGIF[Artt] = float(input(f"Ingrese el gasto de {Artt} para el semestre {Contt+1}°: "))
            mtzGIF.append(dicGIF.copy())

        for Dcc in mtzGIF:
            Dcont +=1
            for Artr in Dcc:
                if Artr == "Depreciacion":
                    Depreciacion = float(mtzGIF[Dcont][Artr])
                if Artr == "Seguros":
                    Seguros = float(mtzGIF[Dcont][Artr])
                if Artr == "Mantenimiento":
                    Mantenimiento = float(mtzGIF[Dcont][Artr]) 
                if Artr == "Energeticos":
                    Energeticos = float(mtzGIF[Dcont][Artr])
                if Artr == "Varios":
                    Varios = float(mtzGIF[Dcont][Artr])
                if Artr == "Semestre":
                    Semestre= float(mtzGIF[Dcont][Artr])                                             
                    Cont = Cont + 1

            if Cont == 1:
                TotalGIF1= Depreciacion+Seguros+Mantenimiento+Energeticos+Varios
                Dep1=Depreciacion
                print("_"*83)
                print(f'{"|":^}{"":^40}{"|":^}{"CANTIDAD":^20}{"|":^}{"SEMESTRE":^20}{"|":^}')
                print(f'{"|":^}{"Depreciacion":^40}{"|":^}{Depreciacion:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Seguros":^40}{"|":^}{Seguros:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Mantenimiento":^40}{"|":^}{Mantenimiento:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Energeticos":^40}{"|":^}{Energeticos:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Varios":^40}{"|":^}{Varios:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"TOTAL GIF PRIMER SEMESTRE":^40}{"|":^}{"":^20}{"|":^}{TotalGIF1:^20}{"|":^}')
                print("_"*83)                   
                
            elif Cont == 2:
                Dep2=Depreciacion
                TotalGIF2= Depreciacion+Seguros+Mantenimiento+Energeticos+Varios
                print("_"*83)
                print(f'{"|":^}{"":^40}{"|":^}{"CANTIDAD":^20}{"|":^}{"SEMESTRE":^20}{"|":^}')
                print(f'{"|":^}{"Depreciacion":^40}{"|":^}{Depreciacion:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Seguros":^40}{"|":^}{Seguros:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Mantenimiento":^40}{"|":^}{Mantenimiento:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Energeticos":^40}{"|":^}{Energeticos:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Varios":^40}{"|":^}{Varios:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"TOTAL GIF SEGUNDO SEMESTRE":^40}{"|":^}{"":^20}{"|":^}{TotalGIF2:^20}{"|":^}')
                print("_"*83)
                print("")
                TotalGIF= TotalGIF1+TotalGIF2
                print(f'{"|":^}{"TOTAL GIF 2016":^55} {TotalGIF:^25}{"|":^}')
                TotalDepGIF=Dep1+Dep2
                CostoGIFxHr= TotalGIF/TOTALHORAS
                print("_"*82)
                print(f'{"|":^}{"Coeficiente para determinar el costo por hora de Gastos Indirectos de Fabricación"}{"|":^}')
                print(f'{"|":^}{"Total GIF"}{TotalGIF:>72}{"|":^}')
                print(f'{"|":^}{"Total horas M.O.D Anual"}{TOTALHORAS:>58}{"|":^}')
                print(f'{"|":^}{"Costo por hora de GIF"}{CostoGIFxHr:>60}{"|":^}')
                print("_"*82)

# 9.- Presupuesto de Gastos de Operacion   
    if(Opcion==9) :
        print("==Presupuesto de Gastos de Operacion==")
        contador= 0 
        dictcont= -1

        for Conta in range(0,2):
            for Dct in dicGastosOp:

                if (Dct == "Semestre"):
                    dicGastosOp[Dct] = (contador + 1)
                else:
                    dicGastosOp[Dct] = float(input(f"Ingrese el gasto de {Dct} para el semestre {Conta+1}°: "))
            mtzGastosOp.append(dicGastosOp.copy())
        for Dcct in mtzGastosOp:
            dictcont +=1
            for Atrib in Dcct:
                if Atrib == "Depreciacion":
                    Depreciacion = float(mtzGastosOp[dictcont][Atrib])
                if Atrib == "SueldosYSalarios":
                    SueldosYSalarios = float(mtzGastosOp[dictcont][Atrib])
                if Atrib == "Varios":
                    Varios = float(mtzGastosOp[dictcont][Atrib])
                if Atrib == "IntPrestamo":
                    IntPrestamo = float(mtzGastosOp[dictcont][Atrib])
                if Atrib == "Semestre":
                    Semestre= float(mtzGastosOp[dictcont][Atrib])                                             
                    contador = contador + 1

            if(contador == 1):
                TotalG1=Depreciacion+SueldosYSalarios+(SEMESTRE1*0.1)+Varios+IntPrestamo
                DepG1=Depreciacion
                print("_"*88)
                print(f'{"|":^}{"":^45}{"|":^}{"CANTIDAD":^20}{"|":^}{"SEMESTRE":^20}{"|":^}')
                print(f'{"|":^}{"Depreciacion":^45}{"|":^}{Depreciacion:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Sueldos y Salarios":^45}{"|":^}{SueldosYSalarios:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Comisiones":^45}{"|":^}{SEMESTRE1*0.1:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Varios":^45}{"|":^}{Varios:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Interés por préstamo":^45}{"|":^}{IntPrestamo:^20}{"|":^}{"1":^20}{"|":^}')
                print(f'{"|":^}{"Total de Gastos de Operacion del Semestre 1":^45}{"|":^}{"":^20}{"|":^}{TotalG1:^20}{"|":^}')
                print("_"*88)

            elif(contador==2):
                TotalG2=Depreciacion+SueldosYSalarios+(SEMESTRE2*0.1)+Varios+IntPrestamo
                DepG2= Depreciacion
                print("_"*88)
                print(f'{"|":^}{"":^45}{"|":^}{"CANTIDAD":^20}{"|":^}{"SEMESTRE":^20}{"|":^}')
                print(f'{"|":^}{"Depreciacion":^45}{"|":^}{Depreciacion:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Sueldos y Salarios":^45}{"|":^}{SueldosYSalarios:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Comisiones":^45}{"|":^}{SEMESTRE2*0.1:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Varios":^45}{"|":^}{Varios:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Interés por préstamo":^45}{"|":^}{IntPrestamo:^20}{"|":^}{"2":^20}{"|":^}')
                print(f'{"|":^}{"Total de Gastos de Operacion del Semestre 2":^45}{"|":^}{"":^20}{"|":^}{TotalG2:^20}{"|":^}')
                print("_"*88)           
                TotalDepGastosOp= DepG1+DepG2
                TotalGastos= TotalG1+TotalG2
                print("_"*83)
                print(f'{"|":^}{"TOTAL Gastos de Operacion 2016":^55} {TotalGastos:^25}{"|":^}')
                print("_"*83)

# 10.- Determinación del costo unitario de Productos Terminados
    if(Opcion==10):
        print("=Determinación del costo unitario de Productos Terminados=")
        print("_"*115)
        print(f'{"|":^}{"":^50}{"|":^}{"PRODUCTO CL":^62}{"|":^}')
        print(f'{"|":^}{"":^50}{"|":^}{"_"*62:^52}{"|":^}')
        print(f'{"|":^}{"Descripcion":^50}{"|":^}{"Costo":^20}{"|":^}{"Cantidad":^20}{"|":^}{"Costo Unitario":^20}{"|":^}')
        print("_"*115)
        print(f'{"|":^}{"Material A":^50}{"|":^}{"12.00":^20}{"|":^}{"1.00":^20}{"|":^}{"12.0":^20}{"|":^}')
        print(f'{"|":^}{"Material B":^50}{"|":^}{"3.00":^20}{"|":^}{"0.5":^20}{"|":^}{"1.50":^20}{"|":^}')
        print(f'{"|":^}{"Material C":^50}{"|":^}{"2.00":^20}{"|":^}{"10.00":^20}{"|":^}{"20.00":^20}{"|":^}')
        print(f'{"|":^}{"Mano de Obra":^50}{"|":^}{"18.00":^20}{"|":^}{"3.0":^20}{"|":^}{"54.00":^20}{"|":^}')
        print(f'{"|":^}{"Gastos Indirctos de Fabricacion:":^50}{"|":^}{"1.20":^20}{"|":^}{"3":^20}{"|":^}{"3.59":^20}{"|":^}')
        print(f'{"|":^}{"Costo Unitario":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"91.09":^20}{"|":^}')
        print("_"*115)

        print("_"*115)
        print(f'{"|":^}{"":^50}{"|":^}{"PRODUCTO CE":^62}{"|":^}')
        print(f'{"|":^}{"":^50}{"|":^}{"_"*62:^52}{"|":^}')
        print(f'{"|":^}{"Descripcion":^50}{"|":^}{"Costo":^20}{"|":^}{"Cantidad":^20}{"|":^}{"Costo Unitario":^20}{"|":^}')
        print("_"*115)
        print(f'{"|":^}{"Material A":^50}{"|":^}{"12.00":^20}{"|":^}{"1.2":^20}{"|":^}{"14.40":^20}{"|":^}')
        print(f'{"|":^}{"Material B":^50}{"|":^}{"3.00":^20}{"|":^}{"0.6":^20}{"|":^}{"1.80":^20}{"|":^}')
        print(f'{"|":^}{"Material C":^50}{"|":^}{"2.00":^20}{"|":^}{"25.00":^20}{"|":^}{"50.00":^20}{"|":^}')
        print(f'{"|":^}{"Mano de Obra":^50}{"|":^}{"18.00":^20}{"|":^}{"1.00":^20}{"|":^}{"18.00":^20}{"|":^}')
        print(f'{"|":^}{"Gastos Indirctos de Fabricacion:":^50}{"|":^}{"1.20":^20}{"|":^}{"1.00":^20}{"|":^}{"1.20":^20}{"|":^}')
        print(f'{"|":^}{"Costo Unitario":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"85.40":^20}{"|":^}')
        print("_"*115)

        print("_"*115)
        print(f'{"|":^}{"":^50}{"|":^}{"PRODUCTO CR":^62}{"|":^}')
        print(f'{"|":^}{"":^50}{"|":^}{"_"*62:^52}{"|":^}')
        print(f'{"|":^}{"Descripcion":^50}{"|":^}{"Costo":^20}{"|":^}{"Cantidad":^20}{"|":^}{"Costo Unitario":^20}{"|":^}')
        print("_"*115)
        print(f'{"|":^}{"Material A":^50}{"|":^}{"12.00":^20}{"|":^}{"2.00":^20}{"|":^}{"24.00":^20}{"|":^}')
        print(f'{"|":^}{"Material B":^50}{"|":^}{"3.00":^20}{"|":^}{"1.00":^20}{"|":^}{"3.00":^20}{"|":^}')
        print(f'{"|":^}{"Material C":^50}{"|":^}{"2.00":^20}{"|":^}{"5.00":^20}{"|":^}{"10.00":^20}{"|":^}')
        print(f'{"|":^}{"Mano de Obra":^50}{"|":^}{"18.00":^20}{"|":^}{"1.05":^20}{"|":^}{"27.00":^20}{"|":^}')
        print(f'{"|":^}{"Gastos Indirctos de Fabricacion:":^50}{"|":^}{"1.20":^20}{"|":^}{"2.00":^20}{"|":^}{"1.80":^20}{"|":^}')
        print(f'{"|":^}{"Costo Unitario":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"65.80":^20}{"|":^}')
        print("_"*115)



# 11.- Valuación de Inventarios Finales
    if(Opcion==11):
        print("=Determinación del costo unitario de Productos Terminados=")
        
        print("_"*115)
        print(f'{"|":^}{"INVENTARIO FINAL DE MATERIALES":^113}{"|":^}')
        print("_"*115)
        print(f'{"|":^}{"Descripcion":^50}{"|":^}{"Unidades":^20}{"|":^}{"Costo Unitario":^20}{"|":^}{"Costo Total":^20}{"|":^}')
        print(f'{"|":^}{"Material A":^50}{"|":^}{"3000.00":^20}{"|":^}{"12.00":^20}{"|":^}{"36000.00":^20}{"|":^}')
        print(f'{"|":^}{"Material B":^50}{"|":^}{"2500.00":^20}{"|":^}{"3.00":^20}{"|":^}{"7500.00":^20}{"|":^}')
        print(f'{"|":^}{"Material C":^50}{"|":^}{"1800.00":^20}{"|":^}{"2.00":^20}{"|":^}{"3600.00":^20}{"|":^}')
        print(f'{"|":^}{"Inventario Final de Materiales":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"47100.00":^20}{"|":^}')
        print("_"*115)

        print("_"*115)
        print(f'{"|":^}{"INVENTARIO FINAL DE PRODUCTO TERMINADO":^113}{"|":^}')
        print("_"*115)
        print(f'{"|":^}{"Descripcion":^50}{"|":^}{"Unidades":^20}{"|":^}{"Costo Unitario":^20}{"|":^}{"Costo Total":^20}{"|":^}')
        print(f'{"|":^}{"Producto CL":^50}{"|":^}{"6500.00":^20}{"|":^}{"91.09":^20}{"|":^}{"592057.00":^20}{"|":^}')
        print(f'{"|":^}{"Producto CE":^50}{"|":^}{"7500.00":^20}{"|":^}{"85.40":^20}{"|":^}{"640500.00":^20}{"|":^}')
        print(f'{"|":^}{"Producto CR":^50}{"|":^}{"5000.00":^20}{"|":^}{"65.80":^20}{"|":^}{"339000.00":^20}{"|":^}')
        print(f'{"|":^}{"Inventario Final de Producto Termiando":^50}{"|":^}{"":^20}{"|":^}{"":^20}{"|":^}{"156155700.00":^20}{"|":^}')
        print("_"*115)


# SALIDA
    elif(Opcion==12):
        print("Saliendo del sistema...\n...\n..\n.")
        break
