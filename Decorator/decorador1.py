def meu_decorador(funcao_original):
    def nova_funcao():
        print("Alguma coisa está acontecendo antes da execução da função original.")
        funcao_original()
        print("Alguma coisa está acontecendo depois da execução da função original.")
    return nova_funcao

@meu_decorador
def funcao_alvo():
    print("Esta é a função original.")

funcao_alvo()
