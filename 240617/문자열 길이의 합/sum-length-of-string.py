n = int(input())
a = [input() for _ in range(n)]
sum_lengths = 0
alpha = 0
for length in a:
    sum_lengths += len(length)
    if length[0] == 'a':
        alpha += 1
print(sum_lengths, alpha)