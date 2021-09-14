a=int(input('Primeiro número: '))
b=int(input('Segundo número: '))
c=int(input('Terceiro número: '))
if a>b or a>c:
    print(f'Maior {a}')
elif b>a or b>c:
    print(f'Maior {b}' )
elif c>b or c>a:
    print(f'Maior {c}')
if a<b or a<c:
    print(f'Menor {a}')
elif c<b or c<a:
    print(f'Menor {c}')
elif b<a or b<c:
    print(f'Menor {b}')
