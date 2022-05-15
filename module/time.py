from functools import lru_cache
import time

# .time(): 1970/1/1 秒数が表示
print(time.time())
print(time.time()/(60*60*24*365))

@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)


before = time.time()
#処理
print(fib(35))
after = time.time()
print(f"recursive fibonacci took {after - before:.5f} sec.")

# .ctime(): 今のローカル時間を文字列で返す
print(time.ctime())
# .localtime() 構造化データで返す
localtime = time.localtime()
print(localtime)
print(f"今日は{localtime.tm_year}年 {localtime.tm_mon}月 {localtime.tm_mday}日")