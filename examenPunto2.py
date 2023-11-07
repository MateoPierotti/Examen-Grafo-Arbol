# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

from grafo import Grafo
from random import randint
grafo_StarWars = Grafo(dirigido=False)

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;
# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader,
# Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
star_wars_char = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C 3PO", "Princess Leia", "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2 D2", "BB 8"]

for i in star_wars_char:
    grafo_StarWars.insert_vertice(i)

j=0
for i in star_wars_char:
    position = grafo_StarWars.search_vertice(i)
    punto = grafo_StarWars.get_element_by_index(position)
    if punto[1].size() < 4:
        k = 0
        while j == 0:
            if k >= len(star_wars_char):
                j=1
            else:
                place = star_wars_char[k]
                positionb = grafo_StarWars.search_vertice(place)
                puntob = grafo_StarWars.get_element_by_index(positionb)
                checker = grafo_StarWars.is_adyacent(punto[0],puntob[0])
                grafo_StarWars.mark_as_not_visited()
                if puntob[1].size() < 3 and punto[0] != puntob[0] and checker == False:
                    value = randint(1, 20)
                    grafo_StarWars.insert_arist(punto[0], puntob[0], value)
                    if punto[1].size() == 3:
                        j=1
                k += 1
        j=0

grafo_StarWars.barrido()


# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 

tree_min = grafo_StarWars.kruskal()
i=0
max_value = 0
max_node = list
for tree in tree_min:
    print("Arbol Minimo")
    for node in tree.split(";"):
        value = node.split("-")
        print(node)
        if value[0]=="Yoda" or value[1]=="Yoda":
            i = 1
        if int(value[2])>max_value:
            max_node = value

    if i == 1:
        print()
        print("El arbol de expansion minimo contiene a Yoda")
        print()
        print(f"Esta es la arista de valor maximo {max_node[0]} y {max_node[1]} comparten {max_node[2]} episodios")