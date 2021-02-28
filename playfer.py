def playfer():
    alpha = [
            ["a","b","c","d","e"],
            ["f","g","h","i","k"],
            ["l","m","n","o","p"],
            ["q","r","s","t","u"],
            ["v","w","x","y","z"]
            ]
    print('Зашифровать - 1, расшифровать - 2')
    choose = int(input())
    if choose == 1:
        compile(alpha)
    else:
        decompile()

def compile(alpha):
    print("Введите послание (eng)")
    s = input().strip()
    s = [x for x in s]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            s.insert(i, 'x')

    if len(s) % 2 != 0:
        s.append('x')

    for i in range(1, len(s),2):
        answer=crypt(s[i-1],s[i])

    return 0

def crypt(a,b):
    s=a+b
    return s




def decompile():
    return 0