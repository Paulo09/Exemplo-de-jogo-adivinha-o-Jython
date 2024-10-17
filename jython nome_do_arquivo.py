import random

# Função principal do jogo
def jogo_adivinhacao():
    print("Bem-vindo ao jogo de adivinhação!")
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            # Solicita ao usuário para adivinhar o número
            palpite = int(input("Adivinhe um número entre 1 e 100: "))
            tentativas += 1
            
            # Verifica se o palpite está correto
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
                break
        except ValueError:
            print("Por favor, insira um número válido.")

# Chama a função para iniciar o jogo
if __name__ == "__main__":
    jogo_adivinhacao()
