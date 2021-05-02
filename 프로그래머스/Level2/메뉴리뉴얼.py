result = ''
dict = {}


def dfs(begain, c, order):
    global result

    if len(result) == c:
        li = sorted(list(result))
        result = ''.join(li)
        if result not in dict.keys():
            dict[result] = 1
        else:
            dict[result] += 1

        return
    for i in range(begain, len(order)):
        if order[i] not in result:
            result += order[i]
            dfs(i + 1, c, order)
            result = result.replace(order[i],'')


def solution(orders, course):
    global dict
    answer = []

    for c in course:
        dict = {}
        max_=0
        for order in orders:
            dfs(0, c, order)
        dict=sorted(dict.items(), key=lambda x: x[1], reverse=True)



        for key,value in dict:
            if value>=max_ and value>1:
                max_=value
                answer.append(key)
            else: break
    answer.sort()
    return answer
