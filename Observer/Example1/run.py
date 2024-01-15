from src.alarme import Alarme
from src.pessoa import Pessoa


al = Alarme()
pessoa1 = Pessoa()
pessoa2 = Pessoa()
pessoa3 = Pessoa()

al.addPessoa(pessoa1)
al.addPessoa(pessoa2)
al.addPessoa(pessoa3)
al.tocar()

print(pessoa3.esta_acordada())

