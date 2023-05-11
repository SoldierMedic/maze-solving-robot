a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]  # two dimensional array representing the maze map

start = 1, 1
end = 2, 5
descision_list = []


def printMaze(maze):
    count = 0
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            print("{}".format(maze[i][j]), end=" ")
            count += 1
            if count == 10:  # count represents the number of columns
                print()
                count = 0
    if count != 0:
        print()


m = []  # m is the two dimensional array representing the maze map
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i, j = start  # i and j are the coordinates of the current position
m[i][j] = 1  # Places one in the starting position
print(m[i][j])


def make_step(k):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == k:  # k is the current step number
                check_surroundings(k)
                


def check_surroundings(k):
    if i > 0 and m[i-1][j] == 0 and a[i-1][j] == 0:  # Up Check
        m[i-1][j] = k + 1
        printMaze(m)
        print()

    if j > 0 and m[i][j-1] == 0 and a[i][j-1] == 0:  # Left Check
        m[i][j-1] = k + 1
        printMaze(m)
        print()

    if i < len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0:  # Down Check
        m[i+1][j] = k + 1
        printMaze(m)
        print()
    if j < len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:  # Right Check
        m[i][j+1] = k + 1
        printMaze(m)
        print()

make_step(1)
make_step(2)
make_step(3)
make_step(4)
make_step(5)
make_step(6)
make_step(7)
make_step(8)
make_step(9)
make_step(10)
make_step(11)
make_step(12)
make_step(13)
make_step(14)
make_step(15)
make_step(16)
printMaze(m)
