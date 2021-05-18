
secreto = 'monitor'
digitadas = []
chances = 3

while True:
    if chances <= 0:  # Contador de chances, quando chances for menor ou = a 0 ele perde
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')  # Input do usuario

    if len(letra) > 1:  # Aqui é para o usuário digitar somente uma letra, por isso coloco o limite
        print('Ahhh isso não vale, digite apenas uma letra.')
        continue  # Se digitar mais de uma eu exibo o print uso o continue pra voltar la pro topo

    digitadas.append(letra)  #  As letras que o usuario mandou, vai ser adicionada a variavel digitadas

    if letra in secreto:  # Se letra(input) estiver dentro da variavel 'secreta'
        print(f'UHUULLL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''  #  Isso é para armanezar cada letra certa que o usuario mandar
    for letra_secreta in secreto:  # Para cada letra_secreta na variavel secreto
        if letra_secreta in digitadas:  # Se letra_secreta estiver em digitadas
            secreto_temporario += letra_secreta  # Então secreto_temporario = secreto_temporario + letra_secreta
        else:
            secreto_temporario += '*'  # Se não... secreto_temporario = secreto_temporario + '*'

    if secreto_temporario == secreto:  # Se secreto_temporario for igual a secreto (secreto_temporario são as letras corretas do usuario)
        print(f'Que legal, VOCÊ GANHOU!!! A palavra era {secreto_temporario}.')
        break
    else:
        print(f'A palavra secreta está assim: {secreto_temporario}')  # Se não... a palavra secreta está secreto_temporario (letras certas armazenadas
                                                                      # porém ainda incompleta a palavra)
    if letra not in secreto:  # Se a letra(input) não estiver em secreto... chances = chances - 1
        chances -= 1

    print(f'Você ainda tem {chances} chances.')  # Mostra o numero de chances restantes
    print()
