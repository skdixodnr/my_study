# 2 ~ 9사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요.
# 2 ~ 9사이의 숫자가 아닌 값이
# 입력된 경우, 잘못 입력되었다고
# 출력하고 다시 입력받으세요.
# n = int(input("몇 단?"))
# # 2 ~ 9 사이의 값이 아닐때 True
# if n < 2 or n > 10:
#     # 다시 입력받기
#     pass
# # 2 ~ 9 사이의 값일때 True
# if n >= 2 and n <= 9:
#     pass
# if 2 <= n < 9:
#     pass
#     # 구구단 출력하는 코드
# 2 <= n <= 9 ------> 2 ~ 9 사이라면 True
n = int(input("몇 단?"))
while not 2 <= n <= 9:
    print("2 ~ 9 사이의 숫자를 입력해주세요.")
    n = int(input("몇 단?"))

for i in range(1, 10):
    print(n, "*", i, "=", n*i)
#for i in range(9):
    # print(n * (i + 1))