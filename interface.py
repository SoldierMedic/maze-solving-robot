import customtkinter as ctk
import tkinter as tk


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
]
start = 1,1
end = 2,5



class MazeWindow(ctk.CTk ):
    def __init__(self, maze, start, end, startMazeFunction,resetMazeFunction):
        super().__init__()
        self.start = start
        self.end = end

        self.geometry('1000x1000')
        ctk.set_appearance_mode('dark')
        self.title('Shit Maze that works like 4 times a year')
        self.labelLocations = {}
        for listIndex, list in enumerate(maze):
            print(f'List {listIndex}')
            for cellIndex, value in enumerate(list):
                if value is 1:
                    backgroundColor = 'black'
                elif value is 0:
                    backgroundColor = 'white'
                if (listIndex,cellIndex) == end:
                    backgroundColor = 'green'
                if (listIndex,cellIndex) == start:
                    backgroundColor = 'blue'
                print(cellIndex, value) 
                self.label = ctk.CTkLabel(self,text ='',bg_color=backgroundColor, width=100,height=75)
                self.label.grid(row=listIndex, column=cellIndex)
                self.labelLocations[(listIndex,cellIndex)] = self.label
        
        button = ctk.CTkButton(self,text='Start Maze', command=startMazeFunction)
        button.place(relx=.425, rely=.85, anchor=tk.CENTER)
        button1 = ctk.CTkButton(self,text='Reset Maze', command=resetMazeFunction)
        button1.place(relx=.575, rely=.85, anchor=tk.CENTER)

    def resetMaze(self,start,end,maze):
        for listIndex, list in enumerate(maze):
            print(f'List {listIndex}')
            for cellIndex, value in enumerate(list):
                if value is 1:
                    backgroundColor = 'black'
                elif value is 0:
                    backgroundColor = 'white'
                if (listIndex,cellIndex) == end:
                    backgroundColor = 'green'
                if (listIndex,cellIndex) == start:
                    backgroundColor = 'blue'
                label = self.labelLocations[(listIndex,cellIndex)]
                label.configure(bg_color= backgroundColor, text='')
                self.update_idletasks()

    def changeCellColor(self, row, column, color, stepNumber):
            label = self.labelLocations[(row,column)]
            label.configure(bg_color= color, text=f'{stepNumber}')
            self.update_idletasks()
       


    def button_click(self):
        print("button click")

