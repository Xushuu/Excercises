# importa o modulo sys para utilizar o comando sys.exit() para encerrar o programa 
import sys
# solicita inserção de dados pelo usuário caso nada seja inserido encerra o programa
nome = input('Digite o nome do alteta (O programa será encerrado caso não insira um nome): ')
if not nome: 
    print('Encerrando...')
    sys.exit()
# cria a lista que recebera as informações do usuário
saltos = [] 
# cria um laço para receber 5 dados que serão digitados pelo usuário
for i in range(1,6):
# recebe as informações digitadas pelo usuários e adiciona a lista
    distancia = float(input(f'Insra a distancia do salto {i}: '))
    saltos.append(distancia)
# realiza o calculo da media somando os valores armazenados na lista e dividindo pela quantidade de itens na lista
media = sum(saltos) / len(saltos)    
#exibe os resultados para o usuário
print('Resultados')
print('Nome do atleta: ', nome)
print('Saltos: ', saltos)
print('Média dos saltos: ', media)
print('----------------------------')

    