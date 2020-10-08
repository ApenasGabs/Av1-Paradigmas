#Elabore um código em Python que recebe nome e idade de uma pessoa e mostra uma mensagem de parabéns para cada ano de vida que a pessoa possui. 
# Não se esqueça de inserir o nome da pessoa nessa mensagem. 
# (Lembre-se de comentar os pontos principais do seu código)
nome = input('Me diga teu nome') #atribui a nome o o nome da pessoa
idade = int(input('Quantos anos voce tem ? ')) #atribui a idade o numeor que a pessoa digitar 
for n in range(1,idade + 1):#faz um laço com o tamanho do numero que a pessoa digitar, esse +1 é para ir até o numeero digitado e não para antes dele
    print(f'Parabens {nome}voce ja esta a {idade} anos no mundo ')#exibe a mensagem de acordo com o numeor que  pessoa digitou 