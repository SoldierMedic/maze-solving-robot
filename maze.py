from interface import *
from time import sleep


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

def createBlankMap(maze):
  m=[]
  for i in range(len(a)):
    m.append([])
    for j in range(len(a[i])):
        m[-1].append(0)
  return m

m = createBlankMap(a)
i,j = start
k=0
m[i][j] = 1
print(m[i][j])

k = 1

print(i)

  
 
def colorTile(i,j):
  m[i][j] = k
  sleep(0.1)
  window.changeCellColor(i,j,'red',k)
  

moveList= []
   
done = False
def make_step(i,j):
    global k, moveList, done
    print(f'Done: {done}')
    if done is True:
      return 
    elif (i,j) == end:
      done = True
      window.changeCellColor(i,j,'orange','all Done')
      print('all done')
    else:
       colorTile(i ,j)
       k+=1
       print(i,j)
       moveList.append([j,i])
       if i<len(m)-1 and m[i+1][j] == 0 and a[i+1][j] == 0: #Down Check
          print('down')
          make_step(i+1 ,j)
       if j>0 and m[i][j-1] == 0 and a[i][j-1] == 0:# Left Check
          print('left')
          make_step(i,j-1)
       if i>0 and m[i-1][j] == 0 and a[i-1][j] == 0:# Up Check
          print('up')
          make_step(i-1,j)
       if j<len(m[i])-1 and m[i][j+1] == 0 and a[i][j+1] == 0:# Right Check
          print('right')
          make_step(i,j+1)
         
         
def startMaze():
   global i,j
   m[i][j] = 'start'
   print(i,j)
   make_step(i,j)
  
def resetMaze():
  global i,j,k,done,moveList,m
  i,j = start
  k=0
  done = False
  moveList=[]
  m=createBlankMap(a)
  window.resetMaze(start,end,a)
global window
window = MazeWindow(a,start,end,startMaze,resetMaze)
window.mainloop()
# # m[2][5] = 'done'
# startMaze()
# # make_step(2)
# # make_step(3)
# # make_step(4)
# # make_step(5)
# # make_step(6)
# # make_step(7)
# # make_step(8)
# # make_step(9)
# # make_step(10)
# # make_step(11)
# # make_step(12)
# # make_step(13)
# # make_step(14)
# # make_step(15)
# # make_step(16)
# printMaze(m)
print(moveList)
