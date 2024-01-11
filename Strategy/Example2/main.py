from habilidades.cura import Curar
from habilidades.luta_arco import UsoArco
from habilidades.luta_espada import LutaEspada
from guereiro import Guerreiro


cavaleiro = Guerreiro(LutaEspada(6))
arqueiro = Guerreiro(UsoArco(9))
curandeiro = Guerreiro(Curar(7))


cavaleiro.acao()
arqueiro.acao()
arqueiro.attributos()
curandeiro.attributos()
