# dictionary(딕셔너리) 자료형
# key-value 형태
# key: value
person ={
    "이름": "이름",
    "나이": 18,
    "점수": {
        "영어": 80,
        "국어": 90,
        "수학": 100
        },
         1: "ㅎㅎ"
}
print(person["나이"])
print(person["점수"]["영어"])

# dict_1 = {1: 'a'}
# dict_1['b'] = 2 # 'b' : 2 key-value 쌍 추가
# dict_1[1] = 'c'
# del dict_1[1]
# print(dict_1)

dict_2 = {1:'a', 2:'b', 3:'c'}
# keys()
# 딕셔너리에서 key 값만 리스트형태로 돌려준다.
dict_keys = dict_2.keys()
print(dict_keys)
# values()
# 딕셔너리에서 value 값만 리스트 형태로 돌려준다.
dict_values = dict_2.values()
print(dict_values)
# items()
# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items = dict_2.items()
print(dict_items)


