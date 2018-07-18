# coding=utf-8

# (1). BMIを計算して表示
height = int(raw_input("身長[cm]を入力: "))
weight = int(raw_input("体重[kg]を入力: "))

height *= 0.01
bmi = 1.0 * weight / height**2

print("BMI: " + str(bmi))


# (2). 肥満かどうか判定し出力
result = "肥満"
if bmi < 18.5:
    result = "低体重"
elif bmi < 25:
    result = "普通体重"

print(result + "です.")


# (3). 標準体重も出力
if result != "普通体重":
    bmi_standard = 22.0 # 標準体重となるBMI
    w_standard = bmi_standard * height**2
    print("標準体重は" + str(w_standard) + "です")

