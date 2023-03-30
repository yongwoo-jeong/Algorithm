def solution(s):
    answer = []
    char = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # 문자열이 시작되면 숫자가 나올때까지 매칭되는애들만 계속 훑도록
    number = []
    word = []
    for c in s:
        if c.isdigit():
            number.append(c)
            continue
        else:
            if number != []:
                answer.append("".join(number))
                number = []
            word.append(c)
            if 3 <= len(word) <= 5:
                tem_word = "".join(word)
                try:
                    answer.append(str(char[tem_word]))
                    word = []
                except:
                    continue
    if number != []:
        answer.append("".join(number))
        number = []
    if word != []:
        answer.append(str(char[tem_word]))
        word = []

    return int("".join(answer))