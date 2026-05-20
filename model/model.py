import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo=nx.MultiGraph()
        self._idMapArtist= {}
        artist = DAO.getAllArtist()
        for a in artist:
            self._idMapArtist[a.ArtistId] = a


    def getGeneri(self):
        return DAO.getGeneri()

    def creaGrafo(self,genere):
        lista = DAO.getArtistGenre(genere)
        self.grafo.clear()
        nodi= []
        for el in lista:
            artist= self._idMapArtist[el[0]]
            artist.Popolarita=el[1]
            nodi.append(artist)
        self.grafo.add_nodes_from(nodi)


    def getArtist(self,id):
        return self._idMapArtist[id].Name

