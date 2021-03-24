N, M = map(int, input().split())
result = []
def solve(depth, N, M):

    if depth == M:
        print(' '.join(map(str, result))) #join으로 공백구분 , result list의전체 출력 map
        return
    for i in range(N): # 수열의 깊이=row
        result.append(i+1)
        solve(depth+1, N, M)
        print("pop/ depth=",depth)
        result.pop()
solve(0, N, M)