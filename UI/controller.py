import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def fillDDGenre(self):
        generi = self._model.getGeneri()

        genriDD= list(map(lambda x: ft.dropdown.Option(x), generi))
        self._view._ddGenre.options= genriDD
        self._view.update_page()


    def handleCreaGrafo(self, e):
        genere = self._view._ddGenre.value
        self._model.buildGraph(genere)
        nodi=self._model.getNodes()
        archi=self._model.getARchi()

        listaTop=self._model.getOutput()

        influ= self._model.getInf()

        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {archi}"))
        self._view.txt_result.controls.append(ft.Text(f"Artista più influente: {influ[0]} con influenza {influ[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Top 5 archi:", color= "red"))
        for el in listaTop:
            self._view.txt_result.controls.append(ft.Text(f"{el[0]}-->{el[1]}:{el[2]}"))

        self._view.update_page()


    def handleCammino(self,e):
        pass