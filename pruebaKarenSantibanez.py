import csv
lista=[]
def menucon:
    print("--- MENÚ PRINCIPAL ---")
    print("1.- AGREGAR PLAN")
    print("2.- LISTAR PLANES")
    print("3.- IMPRIMIR DATOS DE PLAN POR ID")
    print("4.- ELIMINAR PLAN POR ID")
    print("5.- GENERAR BBDD")
    print("6.- CARGAR BBDD")
    print("7.- ESTADISTICAS")
    print("0.- SALIR")
    print("--------------------")
    
    'agregar amenaza'
    def agregar():
        id=int(input("INGRESE ID DE LA AMENAZA"))
        nombre=int(input("INGRESE NOMBRE DE LA AMENAZA"))
        porcentaje=int(input("INGRESE PORCENTAJE DE LA AMENAZA"))
        if porcentaje>=1 and porcentaje<25:
            categoria="CATEGORÍA DE LA AMENAZA - Chiste"
        elif porcentaje>=26 and porcentaje<50:
            categoria="CATEGORÍA DE LA AMENAZA - Anécdota"
        elif categoria>=51 and categoria<75:
            categoria="CATEGORÍA DE LA AMENAZA - Peligro"
        elif categoria>=76 and categoria<99:
            categoria="CATEGORÍA DE LA AMENAZA - Atención"
        elif categoria>=100:
            categoria="CATEGORÍA DE LA AMENAZA - ESCLAVITUD"
        plan=[id,nombre,porcentaje,categoria]
        lista.append(plan)
        
        'listar amenazas'
    def listar():
        for x in lista:
            print("ID AMENAZA: ", x[0], "NOMBRE AMENAZA: ", x[1], "PORCENTAJE AMENAZA: ", x[2])
        
        'buscar plan por ID'
    def imprimir():
        encontrado==False
        id=int(input("INGRESE ID DE LA AMENAZA QUE QUIERE ELIMINAR"))
        for x in lista:
            id_amenaza=int(x[0])
            if id==id_amenaza:
                print("ID DE AMENAZA ENCONTRADO, CARGANDO DATOS")
                print("ID AMENAZA: ", x[0], "NOMBRE AMENAZA: ", x[1], "PORCENTAJE AMENAZA: ", x[2])
        
        'validar eliminación de plan por ID'
    def validar():
        pregunta=input("¿SEGURO QUE QUIERE ELIMINAR LA INFORMACIÓN DE ESTA AMENAZA? ingrese SI/NO :").lower()
        if pregunta=="si" or pregunta=="SI":
            lista.remove
        else:
            print("PLAN NO ELIMINADO")
            
        'generar archivo CSV'
    def generar():
        with open ("listadePlanes.csv", "w", newline="")as archivo:
            escribircsv=csv.writer(archivo)
            escribircsv.writerow(["ID AMENAZA","NOMBRE AMENAZA", "PORCENTAJE AMENAZA"])
            escribircsv.writerow(lista)
            print("INFORMACIÓN GUARDADA EXITOSAMENTE")
            
        'cargar datos CSV'
    def cargar():
        lista.clear()
        with open("listadePlanes.csv","r",newline="")as archivo:
            leercsv=csv.reader(archivo)
            for x in leercsv:
                lista.append(x)
        lista.pop(0)
        for x in lista:
            print("ID AMENAZA: ", x[0], "NOMBRE AMENAZA: ", x[1], "PORCENTAJE AMENAZA: ", x[2])
                
                
        'estadísticas de las Amenazas'
    def estadisticas():
        total=0
        mayor_efect=0
        for x in lista:
            porcentaje=int(x[2])
            total=total+porcentaje
            if porcentaje>porcentaje_efect:
                mayor_efect=porcentaje
        total=len(lista)
        promedio=porcentaje/porcentaje_efect
        print("PORCENTAJE DE EFECTIVIDAD PROMEDIO: ", promedio)
        print("VALOR DE PORCENTAJE DE EFECTIVIDAD MÁS ALTO: ",mayor_efect)
    
        
while True:
    menucon()
    op=int(input("INGRESE UNA OPCIÓN \n"))
    if op==1:
        print("")
        print("1.-AGREGAR PLAN")
        agregar()
        
    elif op==2:
        print("")
        print("2.- LISTAR PLANES")
        listar()
        
    elif op==3:
        print("")
        print("3.- IMPRIMIR DATOS DE PLAN POR ID")
        imprimir()
        
    elif op==4:
        encontrado=False
        print("4.- ELIMINAR PLAN POR ID")
        num=int(input("INGRESE ID DEL PLAN QUE DESEA ELIMINAR"))
        for x in lista:
            id=int(x[0])
            if num==id:
                print("PLAN ENCONTRADO CON ÉXITO")
                print("ID AMENAZA: ", x[0], "NOMBRE AMENAZA: ", x[1], "PORCENTAJE AMENAZA: ", x[2])
                encontrado=True
                validar()
        
    elif op==5:
        print("")
        print("5.- GENERAR BBDD")
        generar()
        
    elif op==6:
        print("")
        print("6.- CARGAR BBDD")
        cargar()
        
    elif op==7:
        print("")
        print("7.- ESTADISTICAS")
        estadisticas()
        
    elif op==0:
        print("SEGUIREMOS INVESTIGANDO, QUE TENGA BUEN DÍA")
        break
    
    else:
        print("INGRESE OPCIÓN VÁLIDA, NO PODEMOS PERDER TIEMPO")


    
    
