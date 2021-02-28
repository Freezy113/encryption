def playfer():
    alpha = [
            ["a","w","c","y","e"],
            ["k","t","h","r","f"],
            ["p","m","n","o","l"],
            ["q","i","s","g","u"],
            ["v","b","x","d","z"]
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
    answer = ''
    for i in range(1, len(s),2):
        answer+=crypt(s[i-1],s[i],alpha)
    print(answer)

def crypt(a,b,alpha):
    x1=0
    y1=0
    x2=0
    y2=0
    for i in range(5):
        for j in range(5):
            if alpha[i][j]==a:
                x1=i
                y1=j
            if alpha[i][j]==b:
                x2=i
                y2=j
    #x - строка y - столбец
    if x1==x2:
        s=caseone(x1,y1,x2,y2,alpha)
    elif y1==y2:
        s=casetwo(x1,y1,x2,y2,alpha)
    else:
        s=casethree(x1,y1,x2,y2,alpha)
    return s

def caseone(x1,y1,x2,y2,alpha):
    if y1<4:
        y1+=1
    else:
        y1=0

    if y2<4:
        y2+=1
    else:
        y2=0
    s = alpha[x1][y1] + alpha[x2][y2]
    return s

def casetwo(x1,y1,x2,y2,alpha):
    if x1<4:
        x1+=1
    else:
        x1=0

    if x2<4:
        x2+=1
    else:
        x2=0
    s=alpha[x1][y1] + alpha[x2][y2]
    return s

def casethree(x1,y1,x2,y2,alpha):
    s=alpha[x1][y2]+alpha[x2][y1]
    return s


def decompile():
    return 0