def solution(info, query):
    result = []
    qarr=[0]*5
    for j in range(len(query)):
        qarr[0], qarr[1], qarr[2], tmp = query[j].split('and')
        qarr[3], qarr[4]=tmp.split()
        for q in range(len(qarr)):
            qarr[q]=qarr[q].replace(' ','')
            if qarr[q]=='-':
                qarr[q]=True

        cnt = 0
        for i in range(len(info)):
            iarr = info[i].split()
            flag=True
            for idx in range(4):
                if qarr[idx]==True:
                    continue
                elif qarr[idx] != iarr[idx]:
                    flag=False
                    break
            if flag and (int(qarr[4]) <= int(iarr[4])):
                cnt+=1

        result.append(cnt)
    answer = result
    return answer
