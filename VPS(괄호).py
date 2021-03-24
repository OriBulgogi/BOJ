a=int(input()) #반복 횟수입력
result=[]
data = list(input() for _ in range(int(a))) #괄호 데이터 입력
for i in range(a):
    count = 0
    for j in range(len(data[i])):
        if data[i][j] == "(":
            count += 1
        elif data[i][j] == ")":
            count -= 1
        if count < 0:
            result.append("NO")
            break
    if count > 0:
        result.append("NO")
    elif count == 0:
        result.append("YES")
    print(result[i])

