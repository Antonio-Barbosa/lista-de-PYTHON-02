sh=float(input('Qual o salário hora? '))
ht=float(input('Horas trabalhadas: '))
sb=sh*ht
ir=sb*11/100
inss=sb*8/100
s=sb*5/100
sl=sb-ir-inss-s
print (f'Salário bruto: R${sb:.3f}')
print (f'Desconto IR: R${ir:.3f}')
print (f'Desconto INSS: R${inss:.3f}')
print (f'Desconto sindicato: R${s:.3f}')
print (f'Salário liquido: R${sl:.3f}')
