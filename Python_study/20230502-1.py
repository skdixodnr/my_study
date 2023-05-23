# def add_all4(*args):
#     temp=0
#     for i in range(len(args)):
#         if type(args[i]) == list:
#             for j in args[i]:
#                 temp +=j
#         else:
#             temp +=args[i]
#     return temp
# print(add_all4([1,2,3,4,5]))
# print(add_all4(1,2,3,4,5))

# 팩토리얼을 구하시오
# 1부터 시작하여 어떤 범위에 있는 모든 정수를 곱하는 것.

# 재귀적으로 하지 않은 것.
# def fact(n):
#     f = 1 #곱을 계산할 변수의 초깃값
#     for i in range(1, n+1): # 1부터 n까지 반복
#         f = f*i # 곱셈연산
#     return f

# print(fact(4))

# # 재귀적으로 하는 것.
# def fact(n):
#     if n <= 1: # n이 1 이하이면 종료조건
#         return 1
#     return n*fact(n-1)

# print(fact(4))

# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는 함수를 짜보자.
# 끊는 단위는 따로 정하지 않으면 2로 설정해보자.
# 힌트 : input을 string과 unit = 2로 받고,while을 사용하고,
# 길이는 len 함수를 사용하도록 하자.
# def func(string, unit=2):
#   i=0
#   while i<len(string):
#     print(string[i:i+unit])
#     i +=unit
# func("테스트를 위한 문장입니다.")

# 빵집에서 사람들에게 먼저 온 순서대로 번호표를 나누어주려고 한다.
# 번호표를 나누어 주는 함수를 작성해보자
# 함수는 사람이름으로 되어있는 리스트를 받아서 "대기번호 x번 : 사람이름"
# 을 화면에 출력하고(번호표, 사람이름)을 원소로 이루어진 리스트를 반환한다
# people = ["펭수", "뽀로로", "뚝딱이", "텔레토비"]
# def func1(line):
#     new_lines = []
#     i = 1 # 대기번호를 트래킹하는 변수 i
#     for x in line:
#         print("대기번호 %d번 : %s" %(i, x))
#         new_lines.append((i, x))
#         i += 1 # 별도로 업데이트를 해줘야 함
#     return new_lines
# print()

# lst = ["a", "b", "c"]
# for x in enumerate(lst):
#     print(x)

# lst1 = "abcd"
# for x in enumerate(lst1):
#     print(x)

# people = ["펭수", "뽀로로", "뚝딱이", "텔레토비"]
# def func1(line):
#     new_lines = []
#     for idx,val in enumerate(line):
#         print("대기번호 %d번 : %s" %(idx, val))
#         new_lines.append((idx+1, val))
#     return new_lines

# print(func1(people))

# str_list = ["one", "two", "three", "four"]
# num_list = [1, 2, 3, 4]

# for i in zip(num_list, str_list):
#     print(i)

# def plus_two(num):
#     return num + 2

# a = 2
# b = plus_two(a)
# print(b)

# lambda x : x + 2

func2 = lambda x : x + 2
c = func2(2)
print (c)


# map(함수 자료형)
# items = [1, 2, 3, 4, 5]

# squared = []
# for i in items:
#     squared.append(i*i)

# print(squared)

# squared_map = list(map(lambda x : x**2, items))

# print(squared_map)

# lambda와 map을 이용하여 items의 요소들을 string(문자)로 바꾸는 것을 짜봅시다.
# items = [1, 24, 3, 6, 7]

# str_items = list(map(lambda x : str(x), items))
# print(str_items)


# list comprehension
# 0 ~ 9까지를 순서대로 가지고 있는 리스트를 만드세요.
# # 1)
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# # 2)
# list_2 = []
# for x in range(10):
#     list_2.append(x)
# print(list_2)
# # 3)
# lc_1 = [x for x in range(10)]
# print(lc_1)

# 구구단2단을 list comprehension을 이용하여 구현하고 리스트를 화면에 출력해보자.
# 1)
# tables = [2 * x for x in range(1, 10)]
# print(tables)

# 2) 코로나 바이러스
# sentence = "코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다."

# len_sent = [len(s) for s in sentence.split()]
# print(len_sent)

# for 문 + if 문
# 10 부터 20 까지의 숫자들 중에서 짝수만을 담은 리스트를 만들어보자.
# # 1)
# list3 = []
# for x in range(10, 21):
#     if x % 2 == 0:
#         list3.append(x)
# print(list3)

# # 2)
# lc_2 = [ x for x in range(10, 21) if x % 2 ==0]
# print(lc_2)

# # 1부터 10의 제곱수 중, 50 이하인 수만 리스트에 저장하라.
# lc_2 = [x**2 for x in range(1,11) if x**2 < 50]
# print(lc_2)

# # 코로나 바이러스
# sentence = "코로나 바이러스를 예방하기 위해 사회적 거리두기를 실천합시다. 외출 시에는 마스크를 끼고, 손씻기를 생활화합시다."
# lc_3 = [s for s in sentence.split() if len(s) < 5]
# print(lc_3)

# for + if + else
# 1부터 10까지의 숫자들 중 홀수이면 어떤 제곱수를, 짝수이면 세제곱수를 담은 리스트를 만들어보자
# 1)
# list_4 = []
# for x in range(1, 11):
#     if x % 2 == 1:
#         list_4.append(x**3)
#     else:
#         list_4.append(x**2)
# print(list_4)

# # 2)
# lc_4 = [x**2 if x%2==0 else x**3 for x in range(1, 11)]
# print(lc_4)

# for문 + for문
# word1 = "hello"
# word2 = "world"

# result = [i + j for i in word1 for j in word2]
# print(result)

# 40 이하의 숫자는 5를 더하고, 40 초과의 숫자는 41로 바꾸어 리스트로 저장하고,리스트를 출력하라
# for x in range(10, 21):
#     if x % 2 == 0:
#         list3.append(x)
# print(list3)

# list_5 = []
# for x in range(1, 100):
#     if x <= 40:
#         list_5.append(x + 5)
#     else:
#         list_5.append(41)
# print(list_5)

# list_6 = [12,67,32,48,19,57,29,49]
# lc_6 = [x+5 if x<=40 else 41 for x in list_6]
# print(lc_6)

# 컷트라인이 60점일때, 사람이름과 통과여부를 리스트로 담아서 출력하라.
# 이름과 통과여부는 튜플로 묶어있는 자료이다.

# students = {"보라돌이":61, "뚜비":35, "나나":78, "뽀":88}

# result = [(name,True) if score>60 else (name, False) for name,score in students.items()]
# print(result)

# import numpy as np
# n = 1000000
# import time

# numpy_arr = np.arange(n)
# python_list = list(range(n))

# print_list = [x**3+10 for x in python_list]
# time()

# numpy_arr = numpy_arr**3 + 10

# import time
# start = time.time()
# python_list = [x ** 3 + 10 for x in python_list]
# print("time : ", time.time() - start)

# A = [1,2,3,4,]
# a = np.array(A, np.int)
# print(type(a))
# print(a)

# 벡터화
# 배열은 for문을 작성하지 않고 데이터를 일괄처리 하는 것.
import numpy as np
arr = np.array([[1,2,3],[4,5,6]])
# print(arr)
# print(arr + arr)
# print(arr / arr)

# # 브로드캐스팅
# # 다른 모양의 배열 간의 산술 연산을 수행할 수 있도록 해주는 numpy의 기능.

# print(10 - arr)
# print(arr * 3)
# print(arr / 3)
# arr2 = np.array([100, 200, 300])
# arr3 = np.array([100, 200])

# print(arr + arr3) # x

arr_1 = np.array([1,2,3,4])
print(arr_1 + arr_1)


# dtype
# 배열에 담긴 원소의 자료형(ndarray는 같은 자료형을 담음)

# size
# 배열에 있는 원소의 전체 갯수
# print(arr.size)

# ndim
# 배열의 차원의 갯수
# print(arr.ndim)

# print(arr.shape)
# print(arr.dtype)

# # 0차원(상수)
# import numpy as np
# a= np.array(10)
# print(a)
# print(a.ndim)

# # 1차원
# a = np.array([1,2,3])
# print(a)
# print(a.ndim)

# # 2 차원
# a = np.array([[1,2],[3,4]])
# print(a)
# print(a.ndim)



# import numpy as np
# arr2d = np.arange(20).reshape(4,-1)
# print(arr2d)

# print(arr2d[:3,:2])

# import random
# print(random.randint(-3,3,10))

# result1 = input().replace(" ", "")
# print(result1)






