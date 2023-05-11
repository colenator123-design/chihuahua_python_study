#1 打印出一個範圍內的所有奇數，範圍從 1 到 10。
for i in range(1, 11, 2):
    print(i)
#2 計算一個範圍內的所有偶數的和，範圍從 1 到 20。
total = 0
for i in range(2, 21, 2):
    total += i
print(total)
#3 打印出一個範圍內的所有 5 的倍數，範圍從 10 到 50。
for i in range(10, 51, 5):
    print(i)
#4 創建一個包含 10 個整數的列表，這些整數的值從 0 到 9。可以使用 range() 函數和列表解析來完成此操作。
my_list = [i for i in range(10)]
print(my_list)
