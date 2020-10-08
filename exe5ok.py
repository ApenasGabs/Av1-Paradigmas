#Uma pessoa quis se inscrever em uma competição de xadrez. A divisão em categorias é feita conforme a idade, considerando:

#Categoria A - de 13 a 17 anos
#Categoria B - de 18 a 34 anos
#Categoria C - de 35 em diante.

#Elabore um código em Python que pergunta o nome e a idade e mostre uma mensagem com o nome da pessoa e a categoria na qual ela será inscrita. Considere que ela não pode se inscrever se tiver 12 anos ou menos. (Lembre-se de comentar os pontos principais do seu código) (25 Pontos)
nome = input('Me diga teu nome ') #atribui a nome o o nome da pessoa

idade = int(input('Quantos anos voce tem ? ')) #atribui a idade o numeor que a pessoa digitar 

if 13 <= idade <= 17:#verifica se idade é maior que 13 e menor que 17
    print(f'{nome} como voce tem {idade} anos, sua categoria é a A')

elif 18 <= idade <= 34:#verifica se idade é maior que 13 e menor que 17

    print(f'{nome} como voce tem {idade} anos, sua categoria é a B')
if 35 <= idade: #verifica se é igual ou maior que 35

    print(f'{nome} como voce tem {idade} anos, sua categoria é a C')

if 12 >= idade:
    print('Voce ainda não tem idade suficiente para se increver')