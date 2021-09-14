a=int(input('lado A: '))
b=int(input('lado B: '))
c=int(input('lado C: '))
if a>b+c and b>c+a and c>b+a :
    if a == b == c :
        print ('Equilátero')
    elif a == b or a == c or b == c:
        print ('Isósceles')
    else:
        print ('Escaleno')
else:
    print ('Não e um triângulo')
