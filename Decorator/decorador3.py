def validar_argumentos(funcao):
    def wrapper(*args, **kwargs):
        if all(isinstance(arg, int) for arg in args):
            return funcao(*args, **kwargs)
        else:
            raise ValueError("Todos os argumentos devem ser inteiros.")
    return wrapper

@validar_argumentos
def multiplicacao(a, b):
    return a * b
