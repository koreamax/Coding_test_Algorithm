import sys

input = sys.stdin.readline
N = int(input())

arr = [int(input()) for _ in range(N)]
arr.sort() 
# .sort()는 배열 자체를 바꾸고
# sorted()는 새로운 배열을 만들어서 할당해줘야 함

print('\n'.join(map(str, arr))) 
# 배열 사이사이에 \n 조인하라
# 리스트의 모든 요소에 함수를 한 번씩 적용
# 또한 map은 주소만 있기 때문에 list로 감싸줘야함