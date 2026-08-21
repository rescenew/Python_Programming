# 변수
a = 2
b = 3
print(a, b)

# a = 2, b = 3
# a = (2, b) = 3

a = 2
b = 3  # 권장하지 않음
a, b = 2, 3  # 권장
print(a, b)

# 값 swap
a, b = b, a
print(a, b)

# 변수명 규칙 (C와 동일)
# 1. 알파벳, 숫자, 밑줄(_)만 사용 가능
# 2. 숫자로 시작할 수 없음
# 3. 예약어는 사용할 수 없음
# 4. 대소문자 구분함

name = "홍길동"

김건우 = "김건우"
print(name, 김건우)
_age = 23
print(_age)

# class = "클래스"

이름 = "뽀로로"
print(이름)

student_name = "크롱"  # snake
studentName = "크롱"  # camel

MAX_SCORE = 100
MAX_SCORE = 200
print(MAX_SCORE)  # 상수는 안변함
