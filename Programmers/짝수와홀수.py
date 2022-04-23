def solution(num):
    # 입력받은 숫자 num을 2로 나눈 나머지가 0이면 짝수이므로 Even을 1이면 홀수이므로 Odd를 출력
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'