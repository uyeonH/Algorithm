# 톱니바퀴
# https://www.acmicpc.net/problem/14891
'''
옆 바퀴를 돌리고 그 옆바퀴를 확인하는게 아니라
처음 상태에서 맞물려있는 곳을 모두 검사했어야하는..
그런데 한번 돌린 상태에서 옆바퀴를 검사해 나가도 예시는 다 맞더라는..
기준이 되는 인덱스도 주의할 것,,
문제를 잘읽자!

'''
from pprint import PrettyPrinter

p = PrettyPrinter(indent=4, width=40)


def rotate(name, dir):
    global arr

    if dir == 1:
        x = arr[name].pop(-1)
        arr[name].insert(0, x)
    else:
        x = arr[name].pop(0)
        arr[name].append(x)

    #print("name: ",name, " ", arr[name])

def start():
    #p.pprint(arr)
    for name, dir in com:  # 톱니바퀴 넘버, 방향
        right = []
        left = []

        # 모든 바퀴의 왼쪽, 오른쪽 상태를 저장해둠
        for i in range(4):
            left.append(arr[i][6])
            right.append(arr[i][2])
        #print("l: ",left)
        #print("r: ",right)

        # 회전
        rotate(name, dir)

        # 임시 저장
        tmp = name
        tmpdir = dir

        # 오른쪽 검사
        while tmp < 3:

            if right[tmp] != left[tmp + 1]:  # 서로 다른 극이면
                #print(right[tmp] , left[tmp + 1])
                rotate(tmp + 1, -tmpdir)  # 오른쪽 톱니바퀴가 반대쪽으로 회전

            else:
                break  # 같은 극이면 스탑

            # right = arr[tmp + 1][2]
            tmp += 1
            tmpdir = -tmpdir

        # 임시 저장
        tmp = name
        tmpdir = dir

        # 왼쪽 검사
        while tmp >= 1:

            if left[tmp] != right[tmp - 1]:  # 서로 다른 극이면
                rotate(tmp - 1, -tmpdir)  # 반대쪽으로 회전

            else:
                break
            # left = arr[tmp - 1][6]

            tmp -= 1
            tmpdir = -tmpdir


if __name__ == '__main__':

    arr = [list(map(int, list(input()))) for _ in range(4)]
    # p.pprint(arr)
    n = int(input())
    com = []
    answer = 0

    for i in range(n):
        a, b = map(int, input().split())
        com.append([a - 1, b])

    start()

    if arr[0][0] == 1:
        answer += 1
    if arr[1][0] == 1:
        answer += 2
    if arr[2][0] == 1:
        answer += 4
    if arr[3][0] == 1:
        answer += 8

print(answer)
