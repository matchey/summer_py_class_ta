# coding:utf-8

# (1). リストを受け取ってそのリストの合計を返す関数
def my_sum(a):
    a_sum = 0

    for i in a:
        a_sum += i

    return a_sum


# (2). 身長・体重を受け取ってBMIを返す関数
def calc_bmi(height, weight):
    return 1.0 * weight / height**2


# (3). BMIを受け取って肥満であればTrue, 肥満でなければFalseを返す関数
def is_fatness(bmi):
    if bmi >= 25:
        rtn = True
    else:
        rtn = False
    return rtn


# (4). 要素が整数のリストを受け取ってFizzBuzzのリストに変換したものを返す関数
def get_fizzbuzz_list(a):
    fizzbuzz_list = list(map(get_fizzbuzz, a))
    
    return fizzbuzz_list

# 整数xを受け取って3の倍数ならFizz, 5の倍数ならBuzz, 15の倍数ならFizzBuzz, else str(x)を返す関数
def get_fizzbuzz(x):
    rtn = ""
    if x % 3 == 0:
        rtn += "Fizz"

    if x % 5 == 0:
        rtn += "Buzz"

    if rtn == "":
        rtn = str(x)

    return rtn


# test
def main():
    a = range(1, 32)

    print(my_sum(a))
    print(calc_bmi(178, 56))
    print(is_fatness(calc_bmi(178, 56)))
    print(get_fizzbuzz_list(a))

if __name__ == "__main__":main()
