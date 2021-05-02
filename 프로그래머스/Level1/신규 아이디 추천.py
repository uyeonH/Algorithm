# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    # 1
    new_id = new_id.lower()
    print(1, new_id)
    # 2
    tmp = new_id
    for s in tmp:
        if s in ['-', '_', '.'] or 'a' <= s <= 'z' or '0' <= s <= '9':
            continue
        else:
            new_id = new_id.replace(s, '')
    print(2, new_id)

    # 3
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    print(3, new_id)

    # 4
    list_ = list(new_id)
    if list_:
        if list_[0] == '.':
            list_ = list_[1:]
            print(list_)
    if list_:

        if list_[-1] == '.':
            list_ = list_[:-1]


    new_id = ''.join(list_)
    print(4, new_id)

    # 5
    if new_id == '':
        new_id = 'a'
    print(5, new_id)

    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    print(6, new_id)

    # 7
    while len(new_id) < 3:
        new_id += new_id[-1]
    answer = str(new_id)
    print(7, new_id)
    print(answer)

    return answer
