def get_cds(n, limit, power):
    # 약수 개수
    cnt = 0
    # 약수 제곱근 이하까지만 나눠보면 된다.
    for i in range(1, int(n**(1/2))+1):
        if n % i == 0:
            # 제곱근일 경우 -> 1개만 카운트하기
            if i == n//i:
                cnt += 1
            else:
                cnt += 2
        if cnt > limit:
            return power
    return cnt


def solution(number, limit, power):
    answer = 1
    for i in range(2, number+1):
        count = get_cds(i, limit, power)
        answer += count
    return answer

