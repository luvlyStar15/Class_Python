# 람다 표현식
# 람다 표현식을 이용하면 함수를 간단하게 작성할 수 있습니다. 
# 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있다는 점이 특징입니다.

# ex1
def add(a:int,b:int)->int:
    return a+b

print(add(3,7))                 # 10이 출력됨.

# ex2
print((lambda a,b:a+b)(3,7))    # 10이 출력됨.

# 람다 표현식 예시
array = [('홍길동',50),('이순신',32),('아무개',74)]

def my_key(x):
    return x[1]

print(sorted(array, key = my_key))
print(sorted(array, key = lambda x: x[1]))
# 기준을 lambda 표현식을 통해서 정렬함.
