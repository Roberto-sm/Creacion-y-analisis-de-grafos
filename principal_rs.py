def busca_indice(g,v): #g = lista de nodos clase grapho, v = nodo de origen ingresado por el usuario
    for i,n in enumerate(g): # enumerate devuelve pares (tuplas) con la forma: [indice, elemento], esta viene junta, pero si declaramos dos variables la primera almacena el indice y la segunda el elemento
        if(v==n.valor): #si el nodo ingresado es igual al nodo en la lista de clase grapho
            return i #retorna el valor i y sale de la funcion/ciclo inmediatamente          
def imprimir_grafo(grafo):
    print("Nodos ",grafo.nodos)
    print("Aristas",grafo.aristas,"\n")
    grafo.grado_nodo()
    for n in grafo.nodos:
        print("Conexiones nodo",n.valor," ",n.conexiones)
op=1
import grafo1_rs      
import pandas as pd
ClaseGrafo = grafo1_rs.grapho()


construir_grafo = input("Desea construir un grafo desde 0?\n(y/n): ")  
if construir_grafo == "y":
    #ConstruccionGrafo = grafo1_rs.grapho()

    while(op!=4):
        print("\n--- MENU DE GRAFOS ---")
        print("1.- Crear Grafo")
        print("2.- Imprimir Grafo ")
        print("3.- Trayectoria")
        print("4.- Salir")
        op=int(input("Teclea una opcion: ")) #1
        
        if(op==1):
            num_nodos=int(input("Cuantos nodos tiene el grafo: ")) #1
            num_aristas=int(input("Cuantas aristas tiene el grafo: "))#1

            for i in range(0,num_nodos,1):
                valor_nodo=input("Teclea el valor del nodo: ") #1
                ClaseGrafo.agregar_nodo(valor_nodo) #Pasa el valor del nodo a la funcion "agregar_nodo" del archivo 'grafo1_rs.py'

            for i in range(0,num_aristas,1):
                valor_origen=input("Teclea el valor del origen ")
                indice_origen=busca_indice(ClaseGrafo.nodos,valor_origen) #indice_origen = guarda el valor de i retornado por la funcion busca_indice, este valor representa la posicion del nodo origen ingresado por el usuario dentro de la lista nodos de la clase grapho 
                valor_destino=input("Teclea el valor del destino ")
                indice_destino=busca_indice(ClaseGrafo.nodos,valor_destino)
                ClaseGrafo.agregar_arista(ClaseGrafo.nodos[indice_origen],ClaseGrafo.nodos[indice_destino]) #accede a la lista nodos en la posicion donde se detuvo el indice_origen y el indice_destino
            ClaseGrafo.actualizar_conexiones()

        elif(op==2):
            print("Nodos ",ClaseGrafo.nodos)
            print("Aristas",ClaseGrafo.aristas,"\n")
            for n in ClaseGrafo.nodos:
                print("Conexiones nodo",n.valor," ",n.conexiones)

        elif(op==3):
            valor_origen=input("Teclea el valor del nodo origen de la trayectoria ")
            indice_origen=busca_indice(ClaseGrafo.nodos,valor_origen)
            valor_destino=input("Teclea el valor del node fin de la  trayectoria ")
            indice_destino=busca_indice(ClaseGrafo.nodos,valor_destino)
            aver=ClaseGrafo.trayectoria(ClaseGrafo.nodos[indice_origen],ClaseGrafo.nodos[indice_destino])
            print(aver)
                
        elif(op==4):
            print("hasta la vista")

else:
    while op != 4:
        import catalogo_grafos
        print("\n--- MENU CATALOGO DE GRAFOS ---")
        print("1.- Grafo simple")
        print("2.- Grafo baile")
        print("3.- Grafo puente")
        print("4.- Salir")
        op = int(input("Selecciona una opcion: "))

        if op == 1:
            GrafoCatalogo = catalogo_grafos.grafo1() 
            imprimir_grafo(GrafoCatalogo)

        elif op == 2:   
            GrafoCatalogo = catalogo_grafos.grafo2()
            imprimir_grafo(GrafoCatalogo)
            tr = input("Desea determinar la trayectoria (y/n)?")
            if tr == "y":
                trayectoria_origen=input("Teclea el valor del nodo origen de la trayectoria ")
                indice_origen=busca_indice(GrafoCatalogo.nodos,trayectoria_origen)
                trayectoria_destino=input("Teclea el valor del node fin de la  trayectoria ")
                indice_destino=busca_indice(GrafoCatalogo.nodos,trayectoria_destino)
                trayectoria=GrafoCatalogo.trayectoria_grado(GrafoCatalogo.nodos[indice_origen],GrafoCatalogo.nodos[indice_destino])
                print(trayectoria)

        elif op == 3:
            GrafoCatalogo = catalogo_grafos.grafo3() 
            #Grafo = grafo1_rs.grapho() 
            imprimir_grafo(GrafoCatalogo)
            rutas = ClaseGrafo.calcular_permutaciones(GrafoCatalogo) #nodos inicio-fin
            bfs = ClaseGrafo.evaluar_rutas(GrafoCatalogo, rutas) #se construyen las rutas con bfs
            datos_finales = ClaseGrafo.generar_dataset(bfs) #se genera el dataset
            df = pd.DataFrame(datos_finales)
            df.to_excel("dataset_grafos.xlsx", index=False) #pasamos el dataset a excel 

            
            #se imprime el dataset ordenadamente
         
            


            # imprimir_grafo(GrafoCatalogo)
            # rutas = Temp_numero_de_rutas.calcular_permutaciones(GrafoCatalogo) #rutas = lista de listas de nodo inicio y fin
            # rutas_construidas = Temp_numero_de_rutas.evaluar_rutas(GrafoCatalogo,rutas)
            # for i,j in enumerate(rutas_construidas):  
            #     print (i," ",j)          
            
            # contador = 1
            # for i,n in rutas:
            #     print (f"Numero de ruta: {contador}")
            #     trayectoria =GrafoCatalogo.trayectoria_grado(i,n)
            #     contador +=1
            

            # tr = input("Desea determinar la trayectoria (y/n)?")
            # if tr == "y":
            #     trayectoria_origen=input("Teclea el valor del nodo origen de la trayectoria ")
            #     indice_origen=busca_indice(GrafoCatalogo.nodos,trayectoria_origen)
            #     trayectoria_destino=input("Teclea el valor del node fin de la  trayectoria ")
            #     indice_destino=busca_indice(GrafoCatalogo.nodos,trayectoria_destino)
                
            #     trayectoria =GrafoCatalogo.trayectoria_grado(GrafoCatalogo.nodos[indice_origen],GrafoCatalogo.nodos[indice_destino])                
            #     print(f"\n{trayectoria}")

        elif(op==4):
            print("hasta la vista")
        