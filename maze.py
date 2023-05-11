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
]# two dimensional array representing the maze map

start = 1,1
end = 2,5
def printMaze(maze):
    count = 0
    for i in range(len(maze)):
     for j in range(len(maze[i])):
        print("{}".format(maze[i][j]), end=" ")
        count += 1
        if count == 10:# count represents the number of columns
            print()
            count = 0
    if count != 0:
        print()


m = []
for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
i,j = start
m[i][j] = 1
print(m[i][j])




def checkSpaces(i,j,k):
  #         [up,down.left,right]
  choices = [0,0,0,0]
  if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:# Up Check
    choices[0] = 1

  if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:# Left Check
    choices[2] = 1


  if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0: #Down Check
    choices[1] = 1


  if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:# Right Check
      choices[3] = 1
  return choices
      


def make_step(k):

  decisionLocations = []
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == k:
        choiceIndexs = [index for index, value in enumerate(checkSpaces()) if value == 1]
        if len(choiceIndexs) > 1:
          print("split")
          # save choice to list and chose a path to go down

        elif len(choiceIndexs) is 0:
          print('Hit a Wall')
          # go back to last decision
        else:
           print('no Split and no wall')
          #  continue down path
         
         

        



make_step(1)
# make_step(2)
# make_step(3)
# make_step(4)
# make_step(5)
# make_step(6)
# make_step(7)
# make_step(8)
# make_step(9)
# make_step(10)
# make_step(11)
# make_step(12)
# make_step(13)
# make_step(14)
# make_step(15)
# make_step(16)
printMaze(m)
