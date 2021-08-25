d = int(input())
res = d
stroka = ""
while res != 1:
    if res % 2:
        stroka = (stroka + "1")
    else:
        stroka = (stroka + "0")
    if res <= 3:
        stroka = (stroka + "1")

    res = res // 2
print(stroka[::-1])