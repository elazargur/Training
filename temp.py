
n = int(input().strip())
score = list(map(int, input().strip().split(' ')))

mini, minicnt = score[0], 0
maxi, maxicnt = score[0], 0

for x in score:
    if x < mini:
        mini = x
        minicnt += 1
    if x > maxi:
        maxi = x
        maxicnt += 1

print(maxicnt, minicnt)
