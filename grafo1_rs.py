#Se usa "self" referirse al objeto actual dentro de una clase, si no se usa self seria una variable local que muere al salir del metodo
from collections import deque

class grapho:
    def __init__(self):
         self.nodos=[]      
         self.aristas=[]

    class Nodo:
        def __init__(self, valor):
            self.valor = valor
            self.conexiones = []
        def __repr__(self): # Esta funcion imprime un objeto y debe retornar un string. Imprime el valor cierto atributo en concreto
            return self.valor 
               
    class Arista:
        def __init__(self, origen, destino):
            self.origen = origen
            self.destino = destino 
        def __repr__(self):
            return self.origen.valor + "-" + self.destino.valor
        
    def __repr__(self):
            return "Nodos " + self.nodos +" " + "Aristas "+ self.aristas
        
    def agregar_nodo(self, valor): #recibe la variable  valor_nodo
            nodo = self.Nodo(valor)
            self.nodos.append(nodo)
            return nodo
        
    def agregar_arista(self, origen, destino):
            arista = self.Arista(origen, destino)
            self.aristas.append(arista)
            
    def actualizar_conexiones(self): 
            for i,n in enumerate(self.nodos):
                for a in self.aristas:
                    if(n==a.origen or n==a.destino):
                            self.nodos[i].conexiones.append(a) #Se agrega la conexión (origen → destino) a la lista de conexiones del objeto Nodo que se está recorriendo en ese momento (A, B o C).

# ---Eursisticas---
    def grado_nodo (self):
        for n in self.nodos:
            grado = len(n.conexiones)
            print (f"Grado del nodo {n}: {grado}")
             
    def trayectoria(self, inicio, fin):
        if inicio == fin:
            return [inicio]
   
        camino = [inicio]
        actual = inicio
        usadas = set()   # Creando un conjunto nota: los conjuntos no aceptan repeticiones

        while actual != fin:
            avance = False

            for a in actual.conexiones:
                if a in usadas:
                    continue#Brincar a la siguiente iteraccion delciclo

                # como el grafo es no  dirigido, tomo el otro extremo
                if a.origen == actual:
                    siguiente = a.destino
                else:
                    siguiente = a.origen

                usadas.add(a)
                camino.append(siguiente)
                actual = siguiente
                avance = True
                break   # se toma la primera arista disponible

            if not avance:
                #return None
                return print("Trayectoria inconclusa ",camino)  #No hay trayectoria. ya no avanzo

        return camino
                                     
    def trayectoria_grado(self, inicio, fin, modo="max"): #inicio = nodo en el que inicia la ruta  fin= nodo al que quiero llegar
        if inicio == fin:
            return [inicio] 

        camino = [inicio] 
        actual = inicio
        usadas = set()  # aristas ya usadas (para no repetir)

        while actual != fin:
            # aristas disponibles desde el nodo actual
            candidatas=self.obtener_candidatas(actual,usadas)#candidatas = conexiones que no pertenecen al conjunto usadas
            if not candidatas:
                #print (f"Ruta, Inicio: {inicio}. Fin: {fin}")
                #print("Trayectoria inconclusa", camino)
                return camino, False
            # elegir la mejor arista según la heurística de grado
            mejor_arista = None
            mejor_valor = None  
            #print("CAN ",candidatas," USADAS ",usadas)     // Imprime las candidatas de cada nodo y el estado del conjunto "usadas" en ese momento

            for ar in candidatas:
                # grafo no dirigido: tomar el otro extremo
                #siguiente = ar.destino if ar.origen == actual else ar.origen
                siguiente = self.obtener_siguiente(ar,actual)   
                valor = self.grado_restante(siguiente,usadas)  # heurística
                mejor_arista,mejor_valor = self.mejor_arista(ar,valor,mejor_arista,mejor_valor) #ar
            # aplicar el paso elegido
            usadas.add(mejor_arista)
            siguiente = self.obtener_siguiente(mejor_arista,actual)
            #siguiente = self.obtener_siguiente(ar,actual)
            camino.append(siguiente)
            actual = siguiente

        #print (f"Ruta, Inicio: {inicio}. Fin: {fin}")
        #print (f"Trayectoria: {camino}")
        return camino, True
  #return sum(1 for ar in nodo.conexiones if ar not in usadas)
  
    def grado_restante(self,nodo,usadas): #nodo siguiente, conjunto usadas 
        contador = 0
        for arista in nodo.conexiones: 
            esta_usada = arista in usadas 
            if esta_usada == False:
                contador = contador + 1
        return contador
   
    def obtener_candidatas(self,nodo, usadas):
        candidatas = []
        for arista in nodo.conexiones:
            if arista not in usadas:
                candidatas.append(arista)
        return candidatas

    def obtener_siguiente(self, arista, actual):
    # 1. Verificar si el nodo actual es el origen de la arista
        if arista.origen == actual:
            siguiente = arista.destino
        else:
            siguiente = arista.origen
        return siguiente

    def mejor_arista(self,ar,valor,mejor_arista,mejor_valor,modo="max"):              
                if mejor_arista is None:
                    mejor_arista = ar
                    mejor_valor = valor
                else:
                    if modo == "max":
                        #print("\nvalor=",valor,"Mejor valor =",mejor_valor," ",ar," ",mejor_arista)
                        if valor > mejor_valor:
                            mejor_arista = ar
                            mejor_valor = valor
                    else:  # modo == "min"
                        if valor < mejor_valor:
                            mejor_arista = ar
                            mejor_valor = valor
                return mejor_arista,mejor_valor
    
    # ---- Construir Dataset ----

    def calcular_permutaciones(self, grafo):
        rutas=[] #lista de listas
        cont=0
        for i in grafo.nodos:
            for j in grafo.nodos:
                if(i==j):
                    continue
                rutas.append([i,j])
                cont += 1
        print (f"\n--POSIBLES RESULTADOS (inicio-fin)--\n{rutas}")
        print ("Total de permutaciones: ",cont)
        return rutas

    # Este metodo construye los caminos de las rutas dadas (inicios-fines)
    def evaluar_rutas(self, grafo, rutas):  #rutas = la lista de todos los nodos inicio-fin
        contador = 1
        resultado = []
        for inicio, fin in rutas:
            trayectoria, estado = grafo.trayectoria_bfs(inicio, fin) #Aqui podemos seleccionar el metodo de trayectoria
            fila = {
                "Num_Ruta": contador, "Nodo_Inicio": inicio.valor, "Nodo_Fin": fin.valor, "Grado_Inicio": len(inicio.conexiones), 
                "Grado_Fin": len(fin.conexiones), "Estado_Ruta": estado, "Cant_Nodos": len(trayectoria), 
                "Calificacion": 10 - len(trayectoria) , "Camino": trayectoria
                }
            resultado.append(fila)
            contador += 1
        return resultado

    #se genera e imprime el resultado
    def generar_dataset(self, datos):         
        print("\n" + "="*110)
        print(f"{'Num. ruta':<12} {'Inicio':<8} {'Fin':<8} {'G_Ini':<8} {'G_Fin':<8} {'Estado':<8} {'Nodos':<8} {'Calificacion':<14} {'Camino':<12}")
        print("="*110)              
        for fila in datos:
            print(f"{fila['Num_Ruta']:<12} {fila['Nodo_Inicio']:<8} {fila['Nodo_Fin']:<8} {fila['Grado_Inicio']:<8} {fila['Grado_Fin']:<8} {fila['Estado_Ruta']:<8} {fila['Cant_Nodos']:<8} {fila['Calificacion']:<14} {fila['Camino']}")
        print("="*110)
        return datos


    def trayectoria_bfs(self, inicio, fin):

        cola = deque() #FIFO. deque() declara una cola de doble extremo
        cola.append((inicio, [inicio])) 
        visitados = set()
        visitados.add(inicio)

        while cola: # mientras cola tenga elementos
            actual, camino = cola.popleft() # .popleft toma (tambien elimina) el elemento mas antiguo en la cola. (FIFO)

            if actual == fin:
                return camino, True

            for arista in actual.conexiones:
                if arista.origen == actual:
                    vecino = arista.destino
                else:   
                    vecino = arista.origen

                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append((vecino, camino + [vecino]))    
                    
        return camino, False
   