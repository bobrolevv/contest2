# работа из дома
d = int(input())
res = d
stroka = ""
while res != 1:
    if res % 2:
        stroka = (stroka + "1")
        #print(f'=={res % 2}=={stroka}')
    else:
        stroka = (stroka + "0")
        #print(f'=={res % 2}=={stroka}')

    if res == 2:
        stroka = (stroka + "1")
		break
    res = res // 2
    #print(f'=={res % 2}=={stroka}')
print(stroka[::-1])