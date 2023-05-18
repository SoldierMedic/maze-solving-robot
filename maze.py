a = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
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
k=0
m[i][j] = 1
print(m[i][j])

k = 1

print(i)
def checkSpaces(i,j):

  
  #    [up,down.left,right]
  # choices = [0,0,0,0]
  if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:# Up Check
    i = i - 1
    print('up')
    make_step(i,j)
  
  if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0: #Down Check
    i = i + 1
    print('down')
    make_step(i,j)

  if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:# Left Check
    j = j -1
    print('left')
    make_step(i,j)

  if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:# Right Check
    j = j +1
    print('right')
    make_step(i,j)
 
      

   
   

def make_step(i,j):
    global k
    if (i,j) == end:
      m[i][j] = "Completed"
      
      print('all done')
      return 0
    else:
      m[i][j] = k=k+1
       print(len(m), len(m[i]))
       print(i,j)
       checkSpaces(i,j)
    # if m[i][j] == k:
        # choiceIndexs = [value for  value in checkSpaces(i,j) if value != 0]
        # if len(choiceIndexs) > 1:
        #   print("split")
        #   # save choice to list and chose a path to go down
        #   decisionLocations.append(m[i][j])
        # elif len(choiceIndexs) is 0:
        #   print('Hit a Deadend')
        #   # go back to last decision
        # else:
        #    print('no Split and no wall')
        #   #  continue down path
         
         
def startMaze():
   global i,j
   m[i][j] = 'start'

   make_step(i,j)
  


# m[2][5] = 'done'
startMaze()
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
