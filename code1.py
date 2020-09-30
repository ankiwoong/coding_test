"""
문제 1: 암호 해독!

다루고 있는 개념 : 이전연산 / 인코딩
난이도 : 하하하
Type : 문제

모든 알고리즘을 해독할 수 있는 알고리즘 7 원석을 보유한 알고리즘 제왕 파이와 썬은 죽기 전,
이 보물에 '암호'를 걸어 세계 어딘가에 묻어놨다고 공표하였다.
그가 남긴 문자는 아래와 같다.

섬으로 향하라!
+ -- + - + -
+ --- + - +
+ -- + - + -
+ - + - + - +
"""

text = [
    " + -- + - + - ",
    " + --- + - + ",
    " + -- + - + - ",
    " + - + - + - + ",
]

# ord() : 문자 -> 숫자
# chr() : 숫자 -> 문자

l = []

for i in text:
    l.append(
        chr(int(i.strip().replace(" ", "").replace("+", "1").replace("-", "0"), 2))
    )

print("".join(l), "\n")

# print([i for i in text])
print(
    "".join(
        [
            chr(int(i.strip().replace(" ", "").replace("+", "1").replace("-", "0"), 2))
            for i in text
        ]
    ),
    "\n",
)

print([i for i in range(10) if i % 2 == 0], "\n")  # 짝수만 출력

print([f"{i} x {j} = {i*j}" for i in range(2, 10) for j in range(1, 10)])  # 구구단 출력
print()

print("011011011".replace("0", "!").replace("!", "+").replace("+", "~"), "\n")

print("1111".zfill(10), "\n")

s = [i.strip().replace(" ", "").replace("+", "1").replace("-", "0") for i in text]
print(s, "\n")

print(list(map(lambda x: chr(int(x, 2)), s)), "\n")


def f(x):
    return chr(int(x, 2))


print("".join(list(map(f, s))))
# zip