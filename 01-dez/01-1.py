from pathlib import Path

PROJECT_DIR = Path(__file__).parent

path = PROJECT_DIR / 'input-1'

input = path.open().readlines()

ans = 0

in1 = [None] * len(input)
in2 = [None] * len(input)

for i in range(len(input)):

    in1[i] = int(input[i][0:5])
    in2[i] = int(input[i][8:13])

in1.sort()
in2.sort()

for i in range(len(input)):
    cur = in1[i] - in2[i]

    if cur < 0:
        cur *= -1
    
    ans += cur

print(ans)