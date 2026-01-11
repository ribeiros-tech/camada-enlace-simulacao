from utils import criar_quadro
from receptor import receber_quadro

def transmitir(dados):
    quadro = criar_quadro(dados)

    while True:
        print(f"\n📤 Transmissor enviando: {quadro}")
        resposta = receber_quadro(quadro)

        if resposta == "ACK":
            print("📨 Transmissão concluída com sucesso!")
            break
        else:
            print("🔁 Retransmitindo o quadro...")


if __name__ == "__main__":
    mensagem = "10110101"
    transmitir(mensagem)
