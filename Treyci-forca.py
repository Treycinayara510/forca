# O comando import rondom, está importando uma biblioteca para sortear uma palavra aleatória.
import random

# Foi atribuida à variável palavras, uma lista de palvras que irão ser sortedas para o jogo.
palavras = []
# Nessa variável as letras que o jogador digitar e não conter na palavra, ficam salvas nessa variável.
letrasErradas = ''
# Nessa variável as letras que o jogador digitar e conter na palavra, ficam salvas nessa variável.
letrasCertas = ''
FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def receberPalavra():
    while True:
        receber = input('Qual palavra você deseja sortear?')
        palavras.append(receber)
        if receber == '':
            break
    
    
def principal(): # def - Define funções. Nesse caso está definindo a principal função do jogo.
    """
    Função Princial do programa
    """
    receberPalavra()
    print('F O R C A') # print imprimi na tela o argumento passado à ele.

    palavraSecreta = sortearPalavra() # Essa variável recebe a função do sortearPalavra. 
    palpite = '' # Variáriavel atribuida para a letra escolhida pelo jogador.
    desenhaJogo(palavraSecreta,palpite)

    while True: # Enquanto for verdade vai sempre ficar rodando essa condição
        palpite = receberPalpite() # Variável palpite recebe a função receberPalpite.
        desenhaJogo(palavraSecreta,palpite)
        # if é um comando condicional.
        if perdeuJogo(): 
            print('Voce Perdeu!!!')
            break
        # break é a condição para, se fizer a condição anterior parar o jogo.
        if ganhouJogo(palavraSecreta):
            print('Voce Ganhou!!!')
            break            
        
def perdeuJogo(): # Aqui está definindo a função perdeuJogo.
    global FORCAIMG # torna global a variável, para dizer que ela é a mesma usada anterior.
    if len(letrasErradas) == len(FORCAIMG): # len - lê o número de caracteres.
        return True # Forma de retornar dados quando a condição for verdadeira.
    else: # É execultado se o if anterior for falso.
        return False # Forma de retornar dados quando a condição for falsa.
    
def ganhouJogo(palavraSecreta): # Aqui está definindo a função ganhouJogo.
    global letrasCertas # dizer que letrasCartas é a mesma que já foi mensionada antes. 
    ganhou = True # para dizer se a o que diz na variável é verdade.
    for letra in palavraSecreta: # for gera um loop dentro de uma lista e o in indica em qual lista ocorrerá.
        if letra not in letrasCertas: # letra não está dentro da lista letrasCartas.
            ganhou = False # para dizer se o que diz na variável é falso.
    return ganhou # Forma para retornar à variável ganhou.       
        


def receberPalpite(): # Aqui está definindo a função receberPalpite.
    
    palpite = input("Adivinhe uma letra: ") # Pedir para o jogador digitar uma letra.
    palpite = palpite.upper() # colocar palpite em maiúsculo.
    if len(palpite) != 1: # dizer que se palpite tiver mais de uma letra, imprimir na tela que é para digitar apenas uma letra.
        print('Coloque um unica letra.') 
    elif palpite in letrasCertas or palpite in letrasErradas: # se a letra já tiver sido digitada, imprimi na tela que o jogador já disse essa letra.
        print('Voce ja disse esta letra.')
    elif not "A" <= palpite <= "Z": # se o jogador não digitar letras que estiver entre o A e o Z, pedir para ele digitar apenas letras.
        print('Por favor escolha apenas letras')
    else:
        return palpite # retornar para a variável palpite.
    
    
def desenhaJogo(palavraSecreta,palpite): # definir a função desenhaJogo.
    # dizer que essas variáveis são as mesmas comentadas acima.
    global letrasCertas 
    global letrasErradas
    global FORCAIMG

    print(FORCAIMG[len(letrasErradas)]) # imprimir na tela o que está dento dessas variáveis.
    
     
    vazio = len(palavraSecreta)*'-' # colocar um _ para cada letra da palavra sorteada.
    
    if palpite in palavraSecreta: # se a letra digitada estiver correta adicionar ela na variável letrasCertas.
        letrasCertas += palpite
    else:
        letrasErradas += palpite # se a letra digitada estiver errada adicionar ela na variável letrasErradas.

    for letra in letrasCertas:
        for x in range(len(palavraSecreta)):
            if letra == palavraSecreta[x]:
                vazio = vazio[:x] + letra + vazio[x+1:]
                
    print('Acertos: ',letrasCertas ) # Imprime na tela as letras que forem certas.
    print('Erros: ',letrasErradas) # Imprime na tela as letras que forem erradas.
    print(vazio)
     

def sortearPalavra():
    global palavras
    return random.choice(palavras).upper() # Retorna no random com a função choice e escolhe uma palavra da lista da variável palavra. Upper deixa em maiúsculo.

    
principal()
