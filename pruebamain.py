from archivo import Archivo
from repositorio import Repositorio
arch = Archivo("test.txt")
repo = Repositorio()
repo.hacer_commit("Initial commit")
repo.crear_rama("dev")
repo.cambiar_rama("dev")
repo.hacer_commit("Added new feature")
repo.cambiar_rama("main")
repo.merge("dev")
repo.mostrar_historial()
