def valid(move, x, y):
    # if move=='d1':
    #     x+=1
    #     y+=1
    if move == 'r':
        y += 1
    elif move == 'd':
        x += 1
    elif move == 'l':
        y -= 1
    elif move == 'u':
        x -= 1
    return (x, y)
# Complete the minimumMoves function below.


def minimumMoves(grid, startX, startY, goalX, goalY):
    c = 0
    visited = set()
    path=[]
    queue = [[startX, startY, c]]
    while queue:
        x, y, c = queue.pop()
        path.append(grid[x][y])
        c += 1
        if (x, y) == (goalX, goalY):
            return c
        for i in ['l', 'r', 'u', 'd']:
            x, y = valid(i, x, y)
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 'X':
                if (x, y) not in visited:
                    visited.add((x, y))
                    queue.append([x, y, c])
    return c


def findpath(m, path, i, j):
    r, c = len(m), len(m[0])
    if i == r-1 and j == c-1:
        print(path+[m[i][j]])
        return
    path.append(m[i][j])
    # down
    if 0 <= i+1 < r and 0 <= j < c:
        findpath(m, path, i+1, j)
        # right
    if 0 <= i < r and 0 <= j+1 < c:
        findpath(m, path, i, j+1)
        # diagonal
    if 0 <= i+1 < r and 0 <= j+1 < c:
        findpath(m, path, i+1, j+1)
    path.pop()


if __name__ == "__main__":
    M = [i for i in range(9)]
    # matrix=[M[i*3:(i+1)*3] for i in range(3)]
    matrix = [[1, 2, 3],
              [5, 'X', 7],
              [8, 'X', 0]]
    # print(*matrix)
    # travel=bfs(matrix)
    # print(travel)
    # findpath(matrix,[],0,0)
    a = minimumMoves(matrix, 2, 0, 2, 2)
    print(a)
