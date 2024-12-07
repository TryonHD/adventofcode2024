from pathlib import Path

PROJECT_DIR = Path(__file__).parent

path = PROJECT_DIR / 'input-1'

input = path.open().readlines()

ans = 0

for i in range(len(input)):
    cur = input[i].split()

    print(cur)

    test = int(cur[0]) - int(cur[1])
    test2 = int(cur[0]) - int(cur[2])
    test3 = int(cur[1]) - int(cur[2])

    if test > 0:
        if test > 3 and test3 <= 3:
             cur.pop(0)
        elif test2 <= 3 and test > 3 and test3 > 3:
             cur.pop(1)
        print(cur)
        num = 0
        num2 = 0
        for i in range(len(cur) - 1):
            if int(cur[i-num2]) - int(cur[i+1]) > 0 and int(cur[i-num2]) - int(cur[i+1]) <= 3:
                num += 1
                if num == len(cur) - 1 - num2:
                    ans += 1
                if num2 == 1:
                    num2 = 0
            else:
                num2 +=1
                if num2 > 1:
                        break
    
    if test < 0:
        if test < -3 and test3 >= -3:
             cur.pop(0)
        elif test2 <= -3 and test < -3 and test3 < -3:
             cur.pop(1)
        print(cur)
        num = 0
        num2 = 0
        for i in range(len(cur) - 1):
            if int(cur[i-num2]) - int(cur[i+1]) < 0 and int(cur[i-num2]) - int(cur[i+1]) >= -3:
                num += 1
                if num == len(cur) - 1 - num2:
                    ans += 1
                if num2 == 1:
                    num2 = 0
            else:
                num2 +=1
                if num2 > 1:
                        break
    print(ans)

print(ans)