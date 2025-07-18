"""
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.

입출력 예
s	return
"1 2 3 4"	"1 4"
"-1 -2 -3 -4"	"-4 -1"
"-1 -1"	"-1 -1"
"""

def solution(s): 
    answer = []  # 전체 배열을 담을 리스트
    answer2 = [] # 최소, 최대 값을 담을 리스트
    
    s_s = s.split() # 하나의 문자열로 되어있던 s를 하나씩 끊어서 분리
    print(s_s) 
    
    for i in s_s:   # 배열에서 하나씩 분리
        i = int(i)
        answer.append(i)
        print(answer)
    
    mi = min(answer)    # 최소값
    answer2.append(mi)
    print(f'{answer2} min')

    ma = max(answer)    # 최대값
    answer2.append(ma)
    print(f'{answer2} min,max') 
    
    # 리스트 컴프레헨션: ex) [-1, -4] -> ['-1', '-4'] 리스트 요소에 문자열 추가.
    ans = [str(num) for num in answer2]
    print(ans)
    ans2 = " ".join(ans)    # 분리한 배열에서 []을 제거 하고 " "으로 연결
    print(ans2)
    
    return ans2