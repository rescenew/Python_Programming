# 연산자

# 산술 연산자
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333333333333335
print(a // b)  # 3, 몫
print(a % b)  # 1, 나머지
print(a**b)  # 1000

# 복합 대입 연산자
a += 5  # a = a + 5
print(a)  # 15
a -= 3  # a = a - 3
print(a)  # 12
a *= 2  # a = a * 2
print(a)  # 24

# 증감 연산자 없음
# b = a++
a += 1  # a = a + 1
print(a)  # 25
a -= 1  # a = a - 1
print(a)  # 24

# 비교 연산자
print(3 == 3.0)  # True, 타입이 달라도 값은 같음
print(3 != 4)  # True
print(3 > 2)  # True
print(3 < 4)  # True
print(3 >= 3)  # True
print(3 <= 4)  # True
print("apple" < "apble")  # True, 문자열 비교는 사전순으로 비교
print(1 < 2 < 3)  # True, 1 < 2 and 2 < 3, 연쇄비교가능, 파이썬만 가능

# 논리 연산자(and, or, not)
a = True
b = False

print(a and b)  # false
print(a or b)  # true
print(not a)  # false

# short circuit evaluation
a = 10
b = 5
c = 0

print(a and b)  # 5, a가 True이므로 b를 반환
print(a and c)  # 0, a가 True이므로 c를 반환
print(a or b)  # 10, a가 True이므로 a를 반환
print(a or c)  # 10, a가 True이므로 a를 반환

# print(a / b)

if a > 0 and b > 0:
    print("yes")
else:
    print("no")
