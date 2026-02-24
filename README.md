Una solución robusta en Python para la modelación, análisis y búsqueda de trayectorias en grafos no dirigidos. El proyecto permite la construcción dinámica de grafos, la aplicación de algoritmos de búsqueda (BFS y Heurística por Grado) y la generación automática de datasets exportables a Excel para análisis de datos masivos.

Características Principales
Construcción Dinámica: Crea grafos desde cero definiendo nodos y aristas
Catálogo de Grafos: Incluye grafos preconfigurados para pruebas rápidas.

Algoritmos de Búsqueda:
BFS (Breadth-First Search): Encuentra el camino más corto en términos de número de nodos.
Heurística por Grado: Implementación de búsqueda voraz (Greedy) basada en el grado restante de los nodos vecinos.

Análisis Avanzado:
Cálculo de grados de cada nodo.
Determinación de vecinos comunes entre pares de nodos.
Cálculo de un "Score" de conectividad basado en topología.
Generación de Datasets: Realiza permutaciones de todos los pares de nodos posibles (Inicio-Fin) y exporta los resultados, incluyendo trayectorias y métricas, directamente a archivos .xlsx (Excel).


Librerías de Terceros:
pandas: Para la manipulación de datos y estructura de datasets.
openpyxl: Motor para la exportación a archivos de Excel.
Estructuras Internas: collections.deque para optimización de colas en BFS.
