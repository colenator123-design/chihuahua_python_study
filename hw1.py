#2.	請寫一個 Python 程序，輸出整數 1 至 10 的和。
sum = 0
for i in range(1, 11):
    sum += i
print(sum)
#3.	請寫一個 Python 程序，輸入一個字符串，然後輸出其長度。
str = input("請輸入一個字符串：")
print("該字符串的長度為：", len(str))
#4.	請寫一個 Python 程序，輸入一個列表，然後輸出列表中的最大值和最小值。
lst = [3, 8, 1, 6, 2, 9, 5, 7, 4]
print("最大值：", max(lst))
print("最小值：", min(lst))
#5.	請寫一個 Python 程序，輸入一個整數 n，然後輸出 1 至 n 的平方數。
n = int(input("請輸入一個整數："))
for i in range(1, n+1):
    print(i**2, end=' ')
#6.	請寫一個 Python 程序，輸入一個整數 n，然後輸出所有小於 n 的質數
n = int(input("請輸入一個整數："))
for i in range(2, n):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i, end=' ')
#7.	請寫一個 Python 程序，輸入一個列表和一個元素，然後輸出該元素在列表中出現的次數。
lst = [1, 2, 3, 4, 5, 2, 2, 3, 4, 2]
x = int(input("請輸入一個整數："))
count = lst.count(x)
print("該元素在列表中出現的次數為：", count)
#8.	請寫一個 Python 程序，輸入一個字符串和一個字符，然後輸出該字符在字符串中出現的次數。
str = input("請輸入一個字符串：")
char = input("請輸入一個字符：")
count = str.count(char)
print("該字符在字符串中出現的次數為：", count)
#9.	請寫一個 Python 程序，輸入一個列表，然後輸出該列表中所有不重複的元素。
lst = [1, 2, 3, 2, 4, 1, 5, 6, 3]
unique_lst = list(set(lst))
print("該列表中所有不重複的元素為：", unique_lst)
#10.	請寫一個 Python 程序，輸入一個字典，然後輸出該字典中所有的鍵和值
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
for key, value in dict.items():
    print(key, value)

