# coding:utf-8

class FizzBuzz:
    def __init__(self, rules={}):
        self.rules = rules # rules: {num:string, ...}
    
    def show(self, count): # count: 上限値 (1~countまでのFizzBuzzを表示)
        fizzbuzz = list(map(self._fizzbuzz, [ i for i in range(1, count + 1)]))
        print "\n".join(fizzbuzz)

    def _fizzbuzz(self, x): # rulesに応じて整数xがnumの倍数ならstring(公倍数なら連結)を返す
        result = [ i[1] for i in sorted(self.rules.items()) if x % i[0] == 0]
        return "".join(result) if result else str(x)

def main():
    # 3の倍数ならFizz、5の倍数ならBuzz、両方とも当てはまるならFizzBuzzを返す
    fizzbuzz = FizzBuzz({3:"Fizz", 5:"Buzz"})
    fizzbuzz.show(31)

if __name__ == "__main__":main()
