import random
import openpyxl

# エクセルファイルのロード
book = openpyxl.load_workbook('特化一覧.xlsx')

# シートのロード
sheet = book['Sheet2']



#何列目
print('前半期待値','49列')

# セルの値取得
c1 = sheet['C49'].value
d1 = sheet['D49'].value
e1 = sheet['E49'].value
f1 = sheet['F49'].value
g1 = sheet['G49'].value
h1 = sheet['H49'].value
i1 = sheet['M49'].value
j1 = sheet['J49'].value

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
    if tur == 1 and pre == 0:
        res = (per/100)*dam*mat*cou*mag
        print(res) #簡易表示
        sheet['N49'] = round(res,3)
        break
    while x > 0:
        if x == pre:
            break
        number = random.choice(num)
        if number <= per:
            a += dam*mat*mag
            x -= tur + pre #発動ターン+準備ターン+〇ターン続く
        else:
            x -= 1         #不発ターン
    f.append(a)
if n == time - 1:
    print("sum(f)=",sum(f),"\nlen(f)=",len(f))
    avg = sum(f)/len(f)
    print(avg)
    sheet['N49'] = round(avg,3)

# 保存する
book.save('特化一覧.xlsx')
