# coding=utf-8

# 以下に示すリストaを作成し，各問のプログラムを作成

a = [2.7, 5.5, 3.9, 5, 9, 2.3, 2.5, 6.0]

# (1). forを使って要素の合計を求めるプログラム
a_sum = 0
for i in a:
    a_sum += i

print("合計: " + str(a_sum))

# (2). sum関数を使って合計を求めよう
print("合計: " + str(sum(a)))

# (3). 要素の平均を求めるプログラムを作ろう
a_ave = sum(a) / len(a)
print("平均: " + str(a_ave))

# (4). 要素の最大値とその要素が何番目のものかを求めるプログラムを作ろう
# a_max = max(a)
# a_max_id = a.index(a_max)
a_max = a[0]
a_max_id = 0

for index, value in enumerate(a):
    if a_max < value:
        a_max = value
        a_max_id = index

print("最大値: " + str(a_max) + " (" + str(a_max_id + 1) + "番目)")

