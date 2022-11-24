import random
import openpyxl

# エクセルファイルのロード
book = openpyxl.load_workbook('特化一覧.xlsx')

# シートのロード
sheet = book['Sheet2']

#何列目
print('総合期待値','62列目')

# セルの値取得
c1 = sheet['C62'].value
d1 = sheet['D62'].value
e1 = sheet['E62'].value
f1 = sheet['F62'].value
g1 = sheet['G62'].value
h1 = sheet['H62'].value
i1 = sheet['I62'].value
j1 = sheet['J62'].value

num = list(range(1,101))
per = d1              #発動率(百分率)
lv = e1                #レベル*〇%
dam = c1 + lv * 50   #ダメージ
mat = f1               #行列数
tur = g1               #〇ターン続く(無い場合は1)
pre = h1               #〇ターン準備
f = []
cou = i1
mag = j1
time = 10000000      #試行回数

for n in range(time):
    x = cou
    a = 0
    num1 = [1,2,3]
    number1 = random.choice(num1)
    while x > 0:
        if number1 <= 2 and x > 4:
            number = random.choice(num)
            if number <= per:
                a += (dam+60)*mat*mag
                x -= 1 + pre #発動ターン+準備ターン
            else:
                x -= 1
            
        if x == pre:
            break
        number = random.choice(num)
        if number <= per:
            a += dam*mat*mag
            x -= 1 + pre #発動ターン+準備ターン
        else:
            x -= 1         #不発ターン
    f.append(a)
if n == time - 1:
    print("sum(f)=",sum(f),"\nlen(f)=",len(f))
    avg = sum(f)/len(f)
    print(avg)
    sheet['R62'] = round(avg,3) #普通K,他R

# 保存する
book.save('特化一覧.xlsx')
