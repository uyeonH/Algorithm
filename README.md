# 코딩테스트 준비


## dictionary 활용

체크용 / 누적용

- 체크용 dic[key]=1, dic2[key]=0 
- 누적용 dic[key]=dic.get(x,0)+1

get()은 key값이 있으면 그 val값을, 없으면 0을 리턴하는 함수

## for-else문

for문에서 break 없이 실행되었다면 else 실행

## 내장함수

- isupper(): 대문자인지 확인
- islower(): 소문자인지 확인
- ord(): 아스키넘버로 변환
- sorted(): 정렬된 리스트 반환 / x=sorted(x,reverse=True) reverse=True이면 내림차순, reverse=False면 오름차순
- sort(): 리스트 자체를 정렬(메소드지만 비교) / x.sort(reverse=True) reverse=True이면 내림차순, reverse=False면 오름차순

## enumerate 함수
이 함수는 (list, set, tuple, dictionary, string)을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.

#### 예시
```
data = enumerate((1, 2, 3))
print(data, type(data))

for i, value in data:
    print(i, ":", value)
print()

data = enumerate({1, 2, 3})
for i, value in data:
    print(i, ":", value)
print()

data = enumerate([1, 2, 3])
for i, value in data:
    print(i, ":", value)
print()

dict1 = {'이름': '뭉자', '나이': 5}
data = enumerate(dict1)
for i, key in data:
    print(i, ":", key, dict1[key])
print()

data = enumerate("안녕하세요")
for i, value in data:
    print(i, ":", value)
print()
```

## map
- map(함수, 리스트)

ex) map(int,['1','2','3'])

## lambda
- lambda 인자 : 표현식

ex) >>list(map(lambda x: x ** 2, range(5)))     
        [0, 1, 4, 9, 16]

