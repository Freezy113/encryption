def compile(alpha):
    print("Введите сдвиг")
    n = int(input())
    print("Введите послание (eng)")
    s = input().strip()
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) + n) % len(alpha)]
    print("Зашифрованное послание")
    print('Result: "' + res + '"')

def decompile(alpha):
    print("Введите сдвиг")
    n = int(input())
    print("Введите зашифрованное послание (eng)")
    s = input().strip()
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) - n) % len(alpha)]
    print("Расшифрованное послание")
    print('Result: "' + res + '"')

def caesar(alpha):
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile(alpha)