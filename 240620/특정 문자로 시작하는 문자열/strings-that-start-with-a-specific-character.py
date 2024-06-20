n = int(input())
words = [input() for _ in range(n)]
a = input()
cnt = 0
count = 0

for word in words:
    if word[0] == a:
        cnt += len(word)
        count += 1


print(f'{count} {(cnt / count):.2f}')