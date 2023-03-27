from collections import defaultdict


def solution(keymap, targets):
    answer = []
    key_dic = defaultdict(lambda: 1000)
    for keys in keymap:
        for i, key in enumerate(keys):
            key_dic[key] = min(i+1, key_dic[key])

    for string in targets:
        cnt = 0
        impossible = False
        for c in string:
            if key_dic[c] == 1000:
                impossible = True
                break
            else:
                cnt += key_dic[c]
        if impossible:
            answer.append(-1)
        else:
            answer.append(cnt)

    return answer