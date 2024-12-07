from pathlib import Path

PROJECT_DIR = Path(__file__).parent

path = PROJECT_DIR / 'input-1'

input = path.open().readlines()

ans = 0

for i in range(len(input)):
    cur = input[i].split()

    test = int(cur[0]) - int(cur[1])

    if test > 0 and test <= 3:
        num = 0
        for i in range(len(cur) - 1):
            if int(cur[i]) - int(cur[i+1]) > 0 and int(cur[i]) - int(cur[i+1]) <= 3:
                num += 1
                if num == len(cur) - 1:
                    ans += 1
            else:
                break
    
    if test < 0 and test >= -3:
        num = 0
        for i in range(len(cur) - 1):
            if int(cur[i]) - int(cur[i+1]) < 0 and int(cur[i]) - int(cur[i+1]) >= -3:
                num += 1
                if num == len(cur) - 1:
                    ans += 1
            else:
                break