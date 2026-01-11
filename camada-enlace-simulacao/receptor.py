from utils import calcular_paridade

def receber_quadro(quadro):
    print(f"\n📥 Receptor recebeu: {quadro}")

    partes = quadro.split("|")

    dados = partes[1]
    paridade_recebida = int(partes[2])

    paridade_calculada = calcular_paridade(dados)

    if paridade_calculada == paridade_recebida:
        print("✅ Quadro correto. Enviando ACK.")
        return "ACK"
    else:
        print("❌ Erro detectado. Enviando NACK.")
        return "NACK"
