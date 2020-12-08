
'''
뮤직비디오(결정알고리즘)
- 문제: 동영상을 DVD로 말들 때, 총 N개의 곡이 들어가는데 순서가 바뀌지 않도록 한다. 한 노래를 쪼갤 수 없다. 
 M개의 DVD에 모든 동영상을 녹화하는데 DVD의 크기를 최소로 하려고 한다. M개의 DVD는 모두 같은 크기여야한다. 
첫째 줄에 N(1<=N<=1000), M(1<=M<<=N)이 주어진다. 다음 줄에 부른 순서대로 부른 곡의 길이가 분 단위(자연수)로 주어진다. 

# input 예시
9 3
1 2 3 4 5 6 7 8 9

'''
import sys
sys.stdin = open("input.txt", "r")


def Count(capacity):
    sum_ = 0
    cnt = 1
    for x in li:
        #print(x,cnt)
        if sum_ + x <= capacity:
            sum_ += x
        else:
            cnt += 1
            sum_ = x
    return cnt


k, n = map(int, input().split())
li = list(map(int, input().split()))

lt = 1
rt = sum(li)
largest=max(li)
while lt <= rt:

    mid = (lt + rt) // 2
    #print("======",mid)
    if mid>=largest and Count(mid) <= n:
        res = mid
        rt = mid - 1

    else:
        lt = mid + 1

print(res)
