import random
R =''
for i in range (4):
    r =str(round(random.uniform(0, 9)))
    if r in R:
        while r in R:
            r =str(round(random.uniform(0, 9)))
    R += r

while True:
    h = 0
    p = 0
    S = input('Введите 4 не повторяющихся числа без пробелов:\n')
    if len(S) == 4:
        for i in range(len(S)):
            if S[i] >= '0' and S[i] <= '9':
                p += 1
            else:
                break
    for i in range(len(S)-1):
        for j in range(i+1,len(S)):
            if S[i] ==S[j]:
                h +=1
    if h!= 0:
        continue
    else:
        bull = 0
        cow = 0
        if len(S) == 4 and p == 4:
            for i in range(len(S)):
                if S[i] in R and S[i] == R[i]:
                    bull += 1
                if S[i] in R and S[i] != R[i]:
                    cow += 1
            print("Коров:" + str(cow) + "\nБыков:" + str(bull))
        elif S =='0':
            print(R)
        else:
            print("Вводите только числа.\n")
