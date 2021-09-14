peso=float(input('Peso dos peixes pescados: '))
excesso=peso-50
multa=excesso*4
if peso > 50:
    print(f'Excesso de {excesso:.2f}')
    print(f'Multa a ser paga R${multa:.2f}')
elif peso <= 50:
        print('Você não excedeu o peso, sua multa será R$ 0')
    
