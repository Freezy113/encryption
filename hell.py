def hell(alpha):
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile(alpha)

def compile(alpha):
    print("Введите ключ")
    n = int(input())
    print("Введите послание (eng)")
    s = input().strip()
    text = []
    for c in n:
        text.append(int((alpha.index(c)) % len(alpha)))
    return 0

def decompile(alpha):
    return 0