from sys import stdin

N, M = map(int, stdin.readline().split())

matrix = [stdin.readline().split() for _ in range(M)]

#queue = [i+1 for i in range(N)]
queue = []
queue_idx = [[0] for _ in range(N)]
count = 0
exit = 0
count2 = 2

#for j in range(M):
while True:
    if not 1 <= N <= 32000 and not 1 <= M <= 100000:
        break
    A, B = matrix[count]
    A = int(A)
    B = int(B)
    #A_index = queue.index(A)
    #B_index = queue.index(B)
    #print(A_index, B_index)


    if A not in queue and B not in queue:
        queue.append(A)
        queue.append(B)
        #print("1:", queue)
    elif A not in queue and B in queue:
        queue.insert(queue.index(B), A)

        #print("2:", queue)
    elif A in queue and B not in queue:
        queue.insert(queue.index(A)+count2, B)
        count2 += 1
        #print("3:", queue)
    elif A in queue and B in queue:
        if queue.index(A) > queue.index(B):
            queue.append(queue.pop(queue.index(B)))
            #print("4:", queue)
        else:
            exit += 1
            if exit >= M:
                break

    count = (count + 1) % M
    # if A_index > B_index:
    #     queue.append(queue.pop(B_index))
    #print(queue)
#print(queue_idx)

for l in range(1, N+1):
    if l not in queue:
        queue.append(l)

for k in range(N):
    print(queue[k], end=" ")