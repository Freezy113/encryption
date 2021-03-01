def compile(alpha):
    print("Введите ключ")
    n = input()
    print("Введите послание (eng)")
    s = input().strip()
    res = ''
    key = []
    for c in n:
        key.append(int((alpha.index(c)) % len(alpha)))
    for c in s:
        res += alpha[((alpha.index(c)) + key[alpha.index(c) % len(key)]) % len(alpha)]
    print("Зашифрованное послание")
    print(res)

def decompile(alpha):
    print("Введите ключ")
    n = input()
    print("Введите послание (eng)")
    s = input().strip()
    res = ''
    key = []
    for c in n:
        key.append(int((alpha.index(c)) % len(alpha)))
    for c in s:
        res += alpha[((alpha.index(c)) - key[alpha.index(c) % len(key)]) % len(alpha)]
    print("Зашифрованное послание")
    print(res)

def viginer(alpha):
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile(alpha)