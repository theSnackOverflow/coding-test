import sys
input = sys.stdin.readline

# 입력 : 곡의 개수, 평균값(올림)
a, b = map(int, input().split())

# 평균값(올림)  = (멜로디의 개수(최솟값) / 곡의 개수)(올림)
# 멜로디의 개수 =  곡의 개수 * (평균값 - 1)

print(a * (b - 1) + 1)