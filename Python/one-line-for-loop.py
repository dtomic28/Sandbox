
def solution(num):
    return sum(x for x in range(num) if x%3==0 or x % 5 == 0)

def method(i):
    print(i)




method(solution(123))