def compile(alpha):
    print("Введите ключ")
    n = input()
    print("Введите послание (eng)")
    s = input().strip()
    res = ''
    res+=str(n)
    for c in s:
        res += alpha[(alpha.index(c)-1) % len(alpha)]
        print(alpha.index(c))
    print("Зашифрованное послание")
    print('Result: "' + res + '"')

def decompile(alpha):
    print("Введите ключ")
    n = input()
    print("Введите зашифрованное послание (eng)")
    s = input().strip()
    res = ''
    for c in s:
        res += alpha[(alpha.index(c) +1) % len(alpha)]
    print("Расшифрованное послание")
    print('Result: "' + res[1:] + '"')

def autokey(alpha):
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile(alpha)