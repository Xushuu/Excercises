'''
Medidor de Velocidade
Levando em consideração a velocidade máxima permitida de 80km em uma detyerminada rua. Crie um programa que recebe do usuário um valor que representa a velocidade e com base 
nessa velocidade diga se ele tomou uma multa leve, grave ou gravissima. Levando em consideração que se a pessoa estiver abaixo da velocidade maxima seu programa deve exibir "não 
houve multa", caso esteja até 10km acima, deve exibir: "Levou multa leve", caso esteja entre 11 a 20km acima da velocidade máxima,exibir: "levou multa grave" e caso esteja acima 
de  20km acima da velocidade máxima, exiba: "Levou multa gravissima"

'''
while True:
    
    max = 80
    velocidade = int(input('Qual a velocidade? '))
    if velocidade < max:
        print('Não houve multa')
    elif velocidade > max and velocidade <= max + 10:
        print('Levou multa Leve')
    elif velocidade > max + 11 and velocidade <= max +20:
        print('Levou multa grave')
    elif velocidade > max + 20:
        print('Levou multa gravissima')
                   
    '''velocidade = int(input('Qual a velociade? '))
    if velocidade > 100:
        print('Levou multa gravissima')
    elif velocidade > 90 <= 100:
        print('levou multa grave')
    elif velocidade > 80 < 90:
        print  ('Levou multa leve')  
    else:
        print('não houve multa') '''   

    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
    if reiniciar.lower() != "s":
        break