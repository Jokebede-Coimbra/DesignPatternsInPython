# Uso do Logger
from logger import Logger


logger_instance_1 = Logger.get_instance("app.log")
logger_instance_2 = Logger.get_instance("app.log")

# Verificando se ambas as variáveis referem-se à mesma instância
print(logger_instance_1 is logger_instance_2)  # Deveria imprimir True

# Registrando eventos usando a instância única do logger
logger_instance_1.log_event("Evento 1 registrado.")
logger_instance_2.log_event("Evento 2 registrado.")

# Verificando o conteúdo do arquivo de log
with open("app.log", 'r') as file:
    print(file.read())
