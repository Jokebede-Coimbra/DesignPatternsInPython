from log_file import LogFile


class Logger:
    # Variável de instância privada para armazenar a única instância do logger
    _instance = None

    # Construtor privado
    def __init__(self, log_file):
        self.log_file = log_file

    # Método estático para acessar a instância única do logger
    @classmethod
    def get_instance(cls, log_file):
        if cls._instance is None:
            cls._instance = cls(log_file)
        return cls._instance

    # Método para registrar eventos
    def log_event(self, message):
        log_content = f"{message}\n"
        log_file = LogFile(self.log_file)
        log_file.write(log_content)

