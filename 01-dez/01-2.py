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

for i in range(len(in1)):
    cur = 0
    for j in range(len(in2)):
        if in1[i] == in2[j]:
            cur += 1
    
    ans += in1[i] * cur

print(ans)