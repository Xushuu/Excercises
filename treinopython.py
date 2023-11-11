'''Caluladora IMC
Como chegamos ao número à esquerda: o índice de massa corporal de um adulto é o seu peso em quilos (por exemplo, 80 kg), 
dividido por sua altura ao quadrado (vamos imaginar, 1,80 m x 1,80 m).


Acima de 40,0 Obesidade grau III 
Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.

Entre 35,0 e 39,9 Obesidade grau II
Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.

Entre 30,0 e 34,9 Obesidade grau I
Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.

Entre 25,0 e 29,9 Sobrepeso
Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.

Entre 18,6 e 24,9 Normal
Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.

18,5 ou menos Abaixo do normal
Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.
'''
while True:
    a = float(input('Digita a sua altura em metros: '))
    p = float(input('Digite o seu peso em kg: '))
    imc = p/(a**2)
    print ('Seu imc é {:.2f}'.format(imc))
    if imc > 40:
        print('Acima de 40,0 Obesidade grau III Aqui o sinal é vermelho, com forte probabilidade de já existirem doenças muito graves associadas. O tratamento deve ser ainda mais urgente.')
    elif imc > 35.0 < 40:
        print('Entre 35,0 e 39,9 Obesidade grau II Mesmo que seus exames aparentem estar normais, é hora de se cuidar, iniciando mudanças no estilo de vida com o acompanhamento próximo de profissionais de saúde.')
    elif imc > 30 < 35:
        print  ('Entre 30,0 e 34,9 Obesidade grau I Sinal de alerta! Chegou na hora de se cuidar, mesmo que seus exames sejam normais. Vamos dar início a mudanças hoje! Cuide de sua alimentação. Você precisa iniciar um acompanhamento com nutricionista e/ou endocrinologista.')  
    elif imc > 25 < 30:
        print('Entre 25,0 e 29,9 Sobrepeso Ele é, na verdade, uma pré-obesidade e muitas pessoas nessa faixa já apresentam doenças associadas, como diabetes e hipertensão. Importante rever hábitos e buscar ajuda antes de, por uma série de fatores, entrar na faixa da obesidade pra valer.')
    elif imc > 18.6 < 25:
        print('Entre 18,6 e 24,9 Normal Que bom que você está com o peso normal! E o melhor jeito de continuar assim é mantendo um estilo de vida ativo e uma alimentação equilibrada.')    
    else:
        print('18,5 ou menos Abaixo do normal Procure um médico. Algumas pessoas têm um baixo peso por características do seu organismo e tudo bem. Outras podem estar enfrentando problemas, como a desnutrição. É preciso saber qual é o caso.')

    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
    if reiniciar.lower() != "s":
        break