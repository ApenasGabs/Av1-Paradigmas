#Um estudante estrangeiro precisava de troco em notas de 5 reais,
#  mas ainda não está acostumado com o dinheiro do Brasil. 
# Ao ir em um caixa eletrônico, digitou um valor aleatório, 
# mas precisa saber quantas notas de 5 ele conseguirá, sendo que o caixa só possui notas de 5.
#Elabore um código em Python que recebe o valor em Reais que se quer sacar e 
# mostra se o valor pode ser sacado inteiramente em notas de 5 ou não.
#  (Lembre-se de comentar os pontos principais do seu código)
bufunfa = float(input('Digite o valor a ser sacado, '))# atribui a bufunfa o numero a ser digitado 
n_cedulas =  round(bufunfa / 5) #faço a conta para ver quantas cedulas a pessoa vai sacar e uso round para tirar os numero de depois da virgula, como só vai ser mostrado se for um numero redondo nao tem problema ignorar eles
if bufunfa % 5==0:#
    print(f'Voce rcebera {n_cedulas} de R$5')#mostra a quantidade de cedulas 
    print(f'Efetuando saque de R${bufunfa}')#mostra quanto ele esta sacando
else:
    print(f'não é possivel sacar R${bufunfa}, digite um valor valido, lembre se que só é possivel sacar em notas de R$5')#avisa que não da pra sacar esse valor 
