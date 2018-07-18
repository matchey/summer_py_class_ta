# coding=utf-8

# (1). ２つの整数を受け取り，受け取った2数の最大公約数を返す関数
def gcd(a, b):
    if a < b:
        small = a
        large = b
    else:
        small = b
        large = a

    while large % small: # ユークリッドの互除法
        large, small = small, large % small

    return small


# (2). ２つの整数を受け取り，互いに素かどうか判定
def is_coprime(a, b):
    if gcd(a, b) == 1:
        rtn = True
    else:
        rtn = False

    return rtn


# (3). 1~30のオイラー関数の値を求めて出力
def phi(n):
    for i in range(1, n+1):
        # print "(" + str(i) + ", " + str(get_totient(i)) + ")"
        print str(i) + ", " + str(get_totient(i))
        # print get_totient(i)
    

# n以下でnと互いに素な数の個数を返す
def get_totient(n):
    num = 0
    for i in range(1, n+1):
        if is_coprime(i, n):
            num += 1
    return num


# test
def main():
    phi(30)

if __name__ == "__main__":main()
