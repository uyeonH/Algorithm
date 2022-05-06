# https://programmers.co.kr/learn/courses/30/lessons/92334
def solution(id_list, report, k):
    answer = []
    singo = {} # 신고
    junggi = {} # 정지
    acc = {} # 누적
    for id in id_list:
        singo[id] = []
        junggi[id] = []
    for r in report:
        a, b = r.split()
        if b not in singo[a]:
            singo[a].append(b)
            if b in acc.keys():
                x = acc[b]
                acc[b] = x + 1
            else:
                acc[b] = 1

    junggi_list = []
    for key, v in acc.items():
        if v >= k:
            junggi_list.append(key)

    for key,v in singo.items():
        for x in junggi_list:
            if x in v:
                junggi[key].append(x)
    for key,v in junggi.items():
        answer.append(len(v))

    return answer
