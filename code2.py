"""
문제 2: JAVA독과 함께!

다루고 있는 개념 : JSON 처리
난이도 : 하하
Type : 문제

첫 문제를 푼 라이캣은 자신의 한계가 어디인지 궁금했어요.
그렇지만 높은 곳은 혼자 갈 수 없죠.
그래서 동료를 모으기로 결심했습니다.

하지만 선뜻 멀고 험한길을 듣보잡 라이캣과 함께 해줄 친구들은 없었답니다.

라이캣은 랩처럼 대사를 외우고 다녔어요.

> 내 동료가 되어라냥!
> 뭐지! 명령문인가?
> '냥'이라니, 자연어처리가 힘들겠는걸?
> 동료는 sum인가, concat인가? axis 0인가, 1인가?

동물 친구들은 수근거렸습니다.
혼자 코딩하기 좋아하는 동물 친구들은 동료라는 말도 이해하지 못했어요.
그러던 중 동물 친구들 중에서 가장 빠르고, 영리한 JAVA 독이 말했습니다.
사실 자바독은 늘 Python을 해보고 싶었거든요.
그래서 라이캣이 파이와 썬의 보물을 찾으러 가는 도구로 파이썬을 사용한다고 하였을 때 눈여겨 보고 있었어요.

> 내가 동료되길 원해? 그렇다면 검증필!?

라이캣은 거절할 이유가 없었죠.

> 좋아냥!

저기 징검다리가 보이지?
내 친구들이 징검다리를 건널거야! 하지만 징검다리는 버틸수 있는 내구도가 한계가 있지!
내 친구들의 몸무게, 돌의 내구도, 친구들의 점프력을 고려하여 내 친구 루비독, 피치피독, 씨-독, 코볼독이 각각 다리를 건널 수 있는지 알아봐줘!
친구들은 더 추가 될 수도, 덜 건널 수도 있어!

1. 각 돌들이 얼마나 버틸 수 있는지 배열로 주어집니다.

2. 각 독들의 개인정보가 JSON(JSON은 큰 따옴표로 묶어야 합니다. 가능하다면 json을 import하여 풀어보세요!)으로 주어집니다.
   개인정보는 보호되지 않습니다.

3. 각 돌에 독들이 착지할 때 돌의 내구도는 몸무게만큼 줄어듭니다.
    ex) [1,2,3,4] 각 돌마다 몸무게 1인 독 2마리 1마리 4마리의 착지를 버틸 수 있습니다.

4. 독들의 점프력이 각자 다릅니다.
    ex) 점프력이 2라면 2칸씩 점프하여 착지합니다.

5. 각 독들은 순서대로만 다리를 건넙니다.

입력>
돌의 내구도 = [1, 2, 1, 4]
독 = [
{
    '이름': '루비독',
    '나이': '95년생',
    '점프력': '3',
    '몸무게': '4',
},{
    '이름': '피치독',
    '나이': '95년생',
    '점프력': '3',
    '몸무게': '3',
},{
    '이름': '씨-독',
    '나이': '72년생',
    '점프력': '2',
    '몸무게': '1',
}{
    '이름': '루코볼독비독',
    '나이': '59년생',
    '점프력': '1',
    '몸무게': '1',
},
]

출력>
생존자: ['씨-독']
"""
# 공통
돌의내구도 = [1, 2, 1, 4]
독 = [
    {
        "이름": "루비독",
        "나이": "95년생",
        "점프력": "3",
        "몸무게": "4",
    },
    {
        "이름": "피치독",
        "나이": "95년생",
        "점프력": "3",
        "몸무게": "3",
    },
    {
        "이름": "씨-독",
        "나이": "72년생",
        "점프력": "2",
        "몸무게": "1",
    },
    {
        "이름": "루코볼독비독",
        "나이": "59년생",
        "점프력": "1",
        "몸무게": "1",
    },
]

# case 1
def 징검다리를건너라(돌의내구도, 독):
    # answer = [독[i]["이름"] for i in range(len(독))]
    answer = [i["이름"] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i["점프력"])
            돌의내구도[독의위치 - 1] -= int(i["몸무게"])
            if 돌의내구도[독의위치 - 1] < 0:
                answer[answer.index(i["이름"])] = "fail"
                break

    return [i for i in answer if i != "fail"]


print(징검다리를건너라(돌의내구도.copy(), 독.copy()), "\n")

# 전역변수 지역변수 리트스 이해

ll = [1, 2, 3, 4, 5]


def change(l):
    l[0] = 1000


change(ll)

print(ll, "\n")

xx = 100


def change(x):
    x += 1000


change(xx)

print(xx, "\n")

# case 2
# remove O(N)
# del O(1)


def 징검다리를건너라(돌의내구도, 독):
    # answer = [독[i]["이름"] for i in range(len(독))]
    answer = [i["이름"] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i["점프력"])
            돌의내구도[독의위치 - 1] -= int(i["몸무게"])
            if 돌의내구도[독의위치 - 1] < 0:
                del answer[answer.index(i["이름"])]
                break

    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()), "\n")

# case 3
# remove O(N)
# del O(1)

돌의내구도 = [10, 20, 10, 40, 10, 10, 10]


def 징검다리를건너라(돌의내구도, 독):
    # answer = [독[i]["이름"] for i in range(len(독))]
    answer = [i["이름"] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i["점프력"])
            돌의내구도[독의위치 - 1] -= int(i["몸무게"])
            if 돌의내구도[독의위치 - 1] < 0:
                del answer[answer.index(i["이름"])]
                break

    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()), "\n")


# case 4
# remove O(N)
# del O(1)
돌의내구도 = [5, 3, 4, 1, 3, 8, 3]


def 징검다리를건너라(돌의내구도, 독):
    # answer = [독[i]["이름"] for i in range(len(독))]
    answer = [i["이름"] for i in 독]
    for i in 독:
        독의위치 = 0
        while 독의위치 < len(돌의내구도) - 1:
            독의위치 += int(i["점프력"])
            돌의내구도[독의위치 - 1] -= int(i["몸무게"])
            if 돌의내구도[독의위치 - 1] < 0:
                del answer[answer.index(i["이름"])]
                break

    return answer


print(징검다리를건너라(돌의내구도.copy(), 독.copy()), "\n")

# json 처리방법
import json

JSON독 = json.dumps(독, ensure_ascii=False)  # 문자열
print(JSON독, "\n")
print(JSON독[0], "\n")
print(JSON독[:10], "\n")

JSON독 = json.loads(JSON독)  # 리스트
print(JSON독, "\n")
print(JSON독[0], "\n")