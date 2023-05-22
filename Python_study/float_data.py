# 실수형 float형
# 1 2 3 -> 정수형
# 1.123 2.50419 -> 실수형
# print(0.1 + 1.1 == 1.2)
# print(0.1 + 1.1)
# 0.1 초
# 100 밀리초

# 실수형 변환 함수
# float()
# float_value = float(input("실수 입력:"))
# print(float_value)

# import numpy as np

# a = [1,3]
# arr_1 = np.array(a) #list to ndarray
# # result = a.tolist() # ndarray to list
# print(arr_1*2)
result = []
def solution(num_list):
    result.append(num_list.reverse())
    return result
