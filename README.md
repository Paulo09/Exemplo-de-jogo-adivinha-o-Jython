Aqui está um exemplo simples de um jogo de adivinhação escrito em Jython (que é uma implementação do Python para a JVM, permitindo que você combine código Java com Python):

python
Copiar código
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
Como funciona:
Importação de bibliotecas: Importamos a função random.randint() para gerar um número aleatório entre 1 e 100.
Estrutura do jogo:
O jogador é solicitado a adivinhar o número.
O programa informa se o palpite foi muito alto ou muito baixo.
O jogo continua até que o jogador acerte o número.
Contagem de tentativas: O programa rastreia o número de tentativas feitas pelo jogador.
Executando o código Jython:
Para executar esse código em Jython, você precisará instalar o Jython (que roda em cima da JVM), e então poderá executar o script da mesma maneira que faria com o Python:

bash
Copiar código
jython nome_do_arquivo.py
Esse exemplo simples pode ser expandido com mais funcionalidades, como limitar o número de tentativas ou permitir níveis de dificuldade.
