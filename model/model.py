import itertools

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.MultiDiGraph()
        self._idMapArtist= {}
        self._idMapGenre= {}
        artist = DAO.getAllArtist()
        for a in artist:
            self._idMapArtist[a.ArtistId] = a
        generi= DAO.getGeneri()
        for g in generi:
            self._idMapGenre[g.Name] = g.GenreId



    def getGeneri(self):
        return DAO.getGeneri()

    def buildGraph(self,n):
        genere= self._idMapGenre[n]
        lista = DAO.getArtistGenre(int(genere))
        self.grafo.clear()
        nodi= []
        for el in lista:
            artist= self._idMapArtist[el]
            nodi.append(artist)
        self.grafo.add_nodes_from(nodi)
        diz= dict()
        archi = DAO.getArchi(int(genere))

        for el in archi:
            if el[1] in diz.keys():
                diz[el[1]].append(el[0])

            else:
                diz[el[1]]= list(([el[0]]))

        popolarita= DAO.getPopolarita(genere)
        diz2=dict()

        for el in popolarita:
            diz2[el[0]]= el[1]

        print(diz2)

        for k,v in diz.items():
            listaC= []
            for el in v:
                listaC.append(el)
            if len(listaC)>1:
                myEdges= itertools.combinations(listaC,2)
                for c in myEdges:
                    if not self.grafo.has_edge(self._idMapArtist[c[0]],self._idMapArtist[c[1]]) and not self.grafo.has_edge(self._idMapArtist[c[1]], self._idMapArtist[c[0]]) :
                        if diz2[c[0]]>diz2[c[1]]:
                            self.grafo.add_edge(self._idMapArtist[c[0]],self._idMapArtist[c[1]], weight=(diz2[c[0]]+diz2[c[1]]))
                        elif diz2[c[0]] < diz2[c[1]]:
                            self.grafo.add_edge(self._idMapArtist[c[1]], self._idMapArtist[c[0]],
                                                weight=(diz2[c[0]] + diz2[c[1]]))
                        elif diz2[c[0]] == diz2[c[1]]:
                            self.grafo.add_edge(self._idMapArtist[c[0]], self._idMapArtist[c[1]],
                                                weight=(diz2[c[0]] + diz2[c[1]]))
                            self.grafo.add_edge(self._idMapArtist[c[1]], self._idMapArtist[c[0]],
                                                weight=(diz2[c[0]] + diz2[c[1]]))

    def getARchi(self):
        return len(self.grafo.edges)


    def getOutput(self):

        listaO= []
        for el1,el2,peso in self.grafo.edges(data=True):
            listaO.append([el1,el2,peso["weight"]])

        listaO.sort(key=lambda x: x[2], reverse=True)
        return listaO[0:5]


    def getInf(self):
        nodoS= max(self.grafo.nodes, key=lambda x: self.grafo.out_degree(x,weight="weight")-self.grafo.in_degree(x,weight="weight"))
        valore = self.grafo.out_degree(nodoS, weight="weight")-self.grafo.in_degree(nodoS,weight="weight")

        return nodoS, valore











    def getArtist(self,id):
        return self._idMapArtist[id].Name

    def getNodes(self):
        return len(self.grafo.nodes)

