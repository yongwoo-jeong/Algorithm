def solution(s, skip, index):
    answer = ''

    alphabet = [chr(x) for x in range(ord('a'), ord('z')+1)]
    for c in skip:
        alphabet.remove(c)

    for c in s:
        target = alphabet.index(c)+index
        if target >= len(alphabet):
            answer += alphabet[target % len(alphabet)]
        else:
            answer += alphabet[target]

    return answer