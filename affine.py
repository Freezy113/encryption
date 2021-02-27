def compile(alpha):
    print("Введите первый ключ")
    n1 = int(input())
    print("Введите второй ключ")
    n2 = int(input())
    print("Введите послание (eng)")
    s = input().strip()
    res = ''
    for c in s:
        res += alpha[((alpha.index(c)*n1) + n2) % len(alpha)]
    print("Зашифрованное послание")
    print('Result: "' + res + '"')

def decompile(alpha):
    print("Введите первый ключ")
    n1 = int(input())
    print("Введите второй ключ")
    n2 = int(input())
    print("Введите зашифрованное послание (eng)")
    s = input().strip()
    res = ''
    for c in s:
        res += alpha[((alpha.index(c) - n2) // n1) % len(alpha)]
    print("Расшифрованное послание")
    print('Result: "' + res + '"')

def affine(alpha):
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile(alpha)