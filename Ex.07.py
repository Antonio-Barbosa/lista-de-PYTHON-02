metros=int(input('Quantos metros quadrados da área?')) 

if metros % 54 == 0:
   latas= metros / 54
   print(f'Vai ser preciso {latas} latas de tinta para pintar a área, e o valor a ser pago será R${latas*80}')
    
else:
    latas=int(metros/54) + 1
    print(f'Vai ser preciso {latas} latas de tinta para pintar a área, e o valor a ser pago será R${latas*80}')
    
