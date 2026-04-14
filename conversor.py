historico = []

def real_para_dolar(valor):
    resultado = valor / 5
    historico.append(f"R$ {valor} -> $ {resultado}")
    return resultado

def real_para_euro(valor):
    resultado = valor / 6
    historico.append(f"R$ {valor} -> € {resultado}")
    return resultado

def mostrar_historico():
    return historico