def calcular_paridade(bits):
    """  
    Calcula paridade  PAR.
    Retorna 0 se a quantidade de bits '1' for par,
    retorna 1 se for ímpar.
    """ 
    return bits.count("1") % 2


def criar_quadro(dados):
    """ 
    Cria um quadro no formato:
    FLAG|DADOS|PARIDADE|FLAG
    """ 
    paridade = calcular_paridade(dados)
    quadro = f"FLAG|{dados}|{paridade}|FLAG"
    return quadro

