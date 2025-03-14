'''
전화번호 목록
해시 문제라는데 해시 안쓰고 푼 문제
'''

def solution(phone_book):
    answer = True
    n = len(phone_book)
    phone_book.sort()
    for i in range(n-1):
        if phone_book[i] in phone_book[i+1]:
            if phone_book[i+1][0:len(phone_book[i])] == phone_book[i]:
                answer = False
    
    return answer