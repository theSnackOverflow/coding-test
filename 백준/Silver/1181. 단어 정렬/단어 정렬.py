import sys

n = int(input())
words = {input().strip() for _ in range(n)}

for word in sorted(words, key=lambda x: (len(x), x)):
    print(word)