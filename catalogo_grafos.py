import grafo1_rs

def grafo1():
    G = grafo1_rs.grapho()

    a = G.agregar_nodo("A")
    b = G.agregar_nodo("B")
    c = G.agregar_nodo("C")

    G.agregar_arista(a, b)
    G.agregar_arista(b, c)
    G.agregar_arista(c, a)

    G.actualizar_conexiones()
    return G

def grafo2():
    G = grafo1_rs.grapho()
    #(Rosa = A) (Fernando = B) (Lorena = C ) (Rafael = D) (Angelica = E) (Luis = F) (Maria = G) (Filiberto = H)
    a = G.agregar_nodo("A")
    b = G.agregar_nodo("B")
    c = G.agregar_nodo("C")
    d = G.agregar_nodo("D")
    e = G.agregar_nodo("E")
    f = G.agregar_nodo("F")
    g = G.agregar_nodo("G")
    h = G.agregar_nodo("H")

    G.agregar_arista(a, b) 
    G.agregar_arista(a, d)   
    G.agregar_arista(b, c)
    G.agregar_arista(b, e)
    G.agregar_arista(c, d)   
    G.agregar_arista(c, f)
    G.agregar_arista(d, e)
    G.agregar_arista(e, f) 
    G.agregar_arista(g, h)   
    
    G.actualizar_conexiones()
    return G

def grafo3():
    G = grafo1_rs.grapho()
    a = G.agregar_nodo("A")
    b = G.agregar_nodo("B")
    c = G.agregar_nodo("C")
    d = G.agregar_nodo("D")
    e = G.agregar_nodo("E")
    f = G.agregar_nodo("F")
    g = G.agregar_nodo("G")
    h = G.agregar_nodo("H")

    G.agregar_arista(a, b) 
    G.agregar_arista(a, c)   
    G.agregar_arista(a, d)
    G.agregar_arista(a, g)
    G.agregar_arista(b, c)   
    G.agregar_arista(c, d)
    G.agregar_arista(c, e)
    G.agregar_arista(e, f) 
    G.agregar_arista(e, h)
    G.agregar_arista(e, g)
    G.agregar_arista(f, g)
    G.agregar_arista(g, h)
    

    G.actualizar_conexiones()
    return G


