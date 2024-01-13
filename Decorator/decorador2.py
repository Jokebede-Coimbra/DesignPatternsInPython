def decorador_com_parametros(parametro):
    def decorador_real(funcao_original):
        def nova_funcao(*args, **kwargs):
            print(f"Decorador com parâmetro: {parametro}")
            funcao_original(*args, **kwargs)
        return nova_funcao
    return decorador_real

@decorador_com_parametros("Minha Mensagem")
def funcao_alvo():
    print("Esta é a função original.")

funcao_alvo()
