# https://curriculum.cosadama.com/python/2-1

# 자료형의 종류: 숫자 자료형, 문자 자료형, 논리 자료형
# 연산자: 산술연산자, 비교연산자, 할당연산자

# 산술연산자
# +	더하기
# -	빼기
# *	곱하기
# /	나누기
# **	제곱
# //	나눈 몫
# %	나눈 나머지

# 비교연산자
# <	왼쪽 값이 오른쪽 값보다 작으면 True 반환.
# <=	왼쪽 값이 오른쪽 값보다 작거나 같으면 True 반환.
# >	왼쪽 값이 오른쪽 값보다 크면 True 반환.
# >=	왼쪽 값이 오른쪽 값보다 크거나 같으면 True 반환.
# ==	왼쪽 값과 오른쪽 값이 같으면 True 반환.
# !=	왼쪽 값과 오른쪽 값이 같지 않으면 True 반환.

# 할당연산자
# =	왼쪽 변수에 오른쪽 값을 할당.	a = b → a = b
# +=	왼쪽 변수에 오른쪽 값을 더한 값을 할당.	a += b → a = a + b
# -=	왼쪽 변수에 오른쪽 값을 뺀 값을 할당.	a -= b → a = a - b
# *=	왼쪽 변수에 오른쪽 값을 곱한 값을 할당.	a *= b → a = a * b
# /=	왼쪽 변수에 오른쪽 값을 나눈 값을 할당.	a /= b → a = a / b
# **=	왼쪽 변수에 오른쪽 값만큼 제곱한 값을 할당.	a **= b → a = a ** b
# //=	왼쪽 변수에 오른쪽 값으로 나눈 몫을 할당.	a //= b → a = a // b
# %=	왼쪽 변수에 오른쪽 값으로 나눈 나머지를 할당.	a %= b → a = a % b

#-----------------------------------------------------------------------------------------------------
# 1-1. 숫자 자료형
# 정수(int) vs 소수(float)

# 반올림(3)
print(round(3.14))

# 올림(4)/내림(3)
from math import*
print(ceil(3.14))
print(floor(3.14))

# ceil, floor는 round와 달리 함수를 사용하기 앞서 from math import *라는 모듈을 실행시켜 주었습니다.
# 모듈이란 특정 기능들(함수, 변수, 클래스 등)이 구현되어 있는 파이썬 파일을 의미
# 파이썬에는 이미 만들어진 편리한 모듈과 라이브러리가 많습니다.
# ceil, floor는 round와 달리 파이썬 기본 내장 함수가 아니기 때문에 모듈을 먼저 실행해야 한다는 것!
# 숫자자료형의 연산

#-------------------------------------------------------------------------------------------------------
# 1-2. 문자 자료형(str)
a = 'Hello World!'
print(type(a)) # type함수: 자료형의 종류를 알려준다
# 문자자료형의 연산
a = 'Hello'
b = 'World'
c = '!'
print(a + b + c)
print(a + ' ' + b + c)
a = 'Hello'
print(a * 2)

# 문자열 인덱싱(Indexing)
# 문자열은 0개 이상의 문자가 모인것인데,
# 문자열의 특정 위치의 문자를 알고 싶을 때 사용하는 것
# 파이썬의 문자열은 0번부터 시작
a = '코사다마'
print(a[0]) # 결과: '코'
a[1] # 결과: '사'
a[2] # 결과: '다'
a[3] # 결과: '마'

a = '코사다마'
a[0] # 결과: '코'
a[-3] # 결과: '사'
a[-2] # 결과: '다'
a[-1] # 결과: '마'

# 문자열 슬라이싱
# 기본 형태 a[start : end : step]
a = '코딩을 사랑하는 다람쥐와 마요네즈'
print(a[1:4]) #결과: a문자열의 1번부터 3번까지 -> '딩을 '
a[:5] #결과: a문자열의 0번부터 4번까지
a[3:] #결과: a문자열의 3번부터 끝까지
a[:] #결과: a문자열 전체 다
print(a[-5:-1]) #결과: a문자열의 -5번부터 -2까지